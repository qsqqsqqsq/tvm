# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

import os
import numpy
import tqdm
import torch
import torchvision
from timm.models import create_model
import tvm
from tvm import relay
import tvm.relay.quantization

torch.manual_seed(0)

os.environ["CUDA_VISIBLE_DEVICES"] = "0"

ctx = tvm.cpu()
target = "llvm"

batch_size = 1
calibrate_num = 1
num_workers = 8
model_name = "vit_base_patch32_224"
performance = {
    "f32": 80.7160,
    "gelu用sigmoid近似": 79.6120,
    "gelu用tanh近似": 80.7340,
    "sigmoid的f16": 74.9,
    "tanh的f16": None,
    "int8": None,
}
root_path = os.path.join(os.path.expanduser("~"), "Documents/quantize_result")

all_op = [
    "conv2d_bias_add",
    "reshape",
    "transpose",
    "concatenate",
    "add",
    "nn.layer_norm",
    "high_dimension_dense_add",
    "take",
    "nn.batch_matmul",
    "multiply",
    "nn.softmax",
    "GELU",
    "dense_bias_add",
]


def prepare_data_loaders(data_path, batch_size):
    dataset = torchvision.datasets.ImageFolder(
        os.path.join(data_path, "val"),
        torchvision.transforms.Compose(
            [
                torchvision.transforms.Resize(
                    248, interpolation=torchvision.transforms.functional.InterpolationMode.BICUBIC
                ),
                torchvision.transforms.CenterCrop(224),
                torchvision.transforms.ToTensor(),
                # torchvision.transforms.Normalize(
                #     mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5]
                # ),
            ]
        ),
    )

    sampler = torch.utils.data.RandomSampler(dataset)
    data_loader = torch.utils.data.DataLoader(
        dataset, batch_size=batch_size, num_workers=num_workers, sampler=sampler
    )
    return data_loader


data_path = "/data/zhaojinxi/data/imagenet"
data_loader = prepare_data_loaders(data_path, batch_size)

calibrate_data = []
for i, (image, label) in enumerate(data_loader):
    if i >= (calibrate_num // batch_size):
        break
    image = (image.numpy() * 255).astype(numpy.uint8)
    calibrate_data.append({"input": image})


def yield_calibrate_data():
    for i in calibrate_data:
        yield i


def evaluate(runtime):
    correct = 0
    total = 0

    t = tqdm.tqdm(data_loader)
    for image, label in t:
        image = (image.numpy() * 255).astype(numpy.uint8)
        data = {"input": image}
        label = label.numpy()
        runtime.set_input(**data)
        runtime.run()
        output = runtime.get_output(0).asnumpy()
        result = output.argmax(axis=1) == label
        correct = correct + result.astype(numpy.float32).sum()
        total = total + label.shape[0]
        acc = correct / total * 100
        t.set_postfix({"accuracy": "{:.4f}".format(acc)})
    return acc


path = os.path.join(root_path, model_name, "origin_mod.json")
if os.path.exists(path):
    mod = None
    params = None
else:
    x = torch.randn([1, 3, 224, 224])
    model = create_model(
        model_name,
        pretrained=True,
        num_classes=None,
        in_chans=3,
        global_pool=None,
        scriptable=False,
    )
    scripted_model = torch.jit.trace(model.eval(), x)
    shape_list = [("input", x.numpy().shape)]
    mod, params = relay.frontend.from_pytorch(scripted_model, shape_list)
quantize_config = {"skip_conv_layers": [i for i in range(9999)]}
quantize_search = relay.quantization.QuantizeSearch(
    model_name=model_name,
    mod=mod,
    params=params,
    dataset=yield_calibrate_data,
    calibrate_num=calibrate_num,
    eval_func=evaluate,
    ctx=ctx,
    target=target,
    root_path=root_path,
    mean=[0.5 * 255, 0.5 * 255, 0.5 * 255],
    scale=[0.5 * 255, 0.5 * 255, 0.5 * 255],
    compare_statistics=False,
    quantize_config=quantize_config,
)

config = quantize_search.get_default_config()
quantize_search.quantize(config)
# quantize_search.visualize("post_processed", config)
quantize_search.evaluate("post_process", config)
