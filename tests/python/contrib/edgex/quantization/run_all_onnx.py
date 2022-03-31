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
import sys
import shutil
import traceback
import onnx
import numpy
import tvm
import tvm.relay as relay
import tvm.relay.quantization


def _run(
    model_name,
    mod,
    params,
    quantize_config,
    input_name,
    mean,
    std,
    axis,
    root_path,
):
    mod = relay.transform.InferType()(mod)
    single_data = {}
    for param in mod["main"].params:
        name_hint = param.name_hint
        dtype = param.checked_type.dtype
        shape = [int(_) for _ in param.checked_type.shape]
        if params is not None and name_hint in params:
            continue  # skip model weight params
        data = numpy.random.randint(0, 256, shape).astype(dtype)
        single_data[name_hint] = data

    def eval_nothing():
        return 0.0

    norm = {}
    if isinstance(input_name, list):
        for tmp1, tmp2, tmp3, tmp4 in zip(input_name, mean, std, axis):
            norm[tmp1] = {"mean": tmp2, "std": tmp3, "axis": tmp4}
    else:
        norm[input_name] = {"mean": mean, "std": std, "axis": axis}

    quantize_search = relay.quantization.QuantizeSearch(
        model_name=model_name,
        mod=mod,
        params=params,
        dataset=lambda: iter([single_data]),
        calibrate_num=1,
        eval_func=eval_nothing,
        ctx=tvm.cpu(),
        target="llvm",
        root_path=root_path,
        norm=norm,
        quantize_config=quantize_config,
        compare_statistics=True,
        verbose=True,
    )

    config = quantize_search.get_default_config()
    quantize_search.quantize(config)
    print(quantize_search.results[0]["other"]["similarity"][0][-1][1] >= 0.99)


classification = {
    "mobilenet-v1": {
        "input": "input:0",
        "shape": [1, 3, 224, 224],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "mobilenet-v1/mobilenet_v1_1.0_224.onnx",
    },
    "mobilenet-v2": {
        "input": "input",
        "shape": [1, 3, 224, 224],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "mobilenet-v2/mobilenetv2-7.onnx",
    },
    "mobilenet-v2_torchvision": {
        "input": "input.1",
        "shape": [1, 3, 224, 224],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "mobilenet-v2_torchvision/mobilenetv2_torchvision.onnx",
    },
    "mobilenet-v3-small": {
        "input": "input_image",
        "shape": [1, 3, 224, 224],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "mobilenet-v3-small/mobilenetv3_small_new.onnx",
    },
    "resnet18-v1": {
        "input": "data",
        "shape": [1, 3, 224, 224],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "resnet18-v1/resnet18-v1-7.onnx",
    },
    "resnet18-v2": {
        "input": "data",
        "shape": [1, 3, 224, 224],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "resnet18-v2/resnet18-v2-7.onnx",
    },
    "resnet34-v1": {
        "input": "data",
        "shape": [1, 3, 224, 224],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "resnet34-v1/resnet34-v1-7.onnx",
    },
    "resnet34-v2": {
        "input": "data",
        "shape": [1, 3, 224, 224],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "resnet34-v2/resnet34-v2-7.onnx",
    },
    "resnet50-caffe2-v1": {
        "input": "gpu_0/data_0",
        "shape": [1, 3, 224, 224],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "resnet50-caffe2-v1/resnet50-caffe2-v1-9.onnx",
    },
    "resnet50-v1": {
        "input": "data",
        "shape": [1, 3, 224, 224],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "resnet50-v1/resnet50-v1-7.onnx",
    },
    "resnet50-v2": {
        "input": "data",
        "shape": [1, 3, 224, 224],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "resnet50-v2/resnet50-v2-7.onnx",
    },
    "resnet101-v1": {
        "input": "data",
        "shape": [1, 3, 224, 224],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "resnet101-v1/resnet101-v1-7.onnx",
    },
    "resnet101-v2": {
        "input": "data",
        "shape": [1, 3, 224, 224],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "resnet101-v2/resnet101-v2-7.onnx",
    },
    "resnet152-v1": {
        "input": "data",
        "shape": [1, 3, 224, 224],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "resnet152-v1/resnet152-v1-7.onnx",
    },
    "resnet152-v2": {
        "input": "data",
        "shape": [1, 3, 224, 224],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "resnet152-v2/resnet152-v2-7.onnx",
    },
    "resnext50_32x4d_torchvision": {
        "input": "input.1",
        "shape": [1, 3, 224, 224],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "resnext50_32x4d_torchvision/resnext50_32x4d.onnx",
    },
    "resnest50": {
        "input": "input.1",
        "shape": [1, 3, 224, 224],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "resnest50/resnest50.onnx",
    },
    "wide_resnet50_torchvision": {
        "input": "input.1",
        "shape": [1, 3, 224, 224],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "wide_resnet50_torchvision/wide_resnet50_2.onnx",
    },
    "seresnet50": {
        "input": "input_image",
        "shape": [1, 3, 224, 224],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "seresnet50/seresnet50.onnx",
    },
    "squeezenet1.0": {
        "input": "data_0",
        "shape": [1, 3, 224, 224],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "squeezenet1.0/squeezenet1.0-9.onnx",
    },
    "squeezenet1.1": {
        "input": "data",
        "shape": [1, 3, 224, 224],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "squeezenet1.1/squeezenet1.1-7.onnx",
    },
    "vgg16": {
        "input": "data",
        "shape": [1, 3, 224, 224],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "vgg16/vgg16-7.onnx",
    },
    "vgg16-bn": {
        "input": "data",
        "shape": [1, 3, 224, 224],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "vgg16-bn/vgg16-bn-7.onnx",
    },
    "alexnet": {
        "input": "data_0",
        "shape": [1, 3, 224, 224],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "alexnet/bvlcalexnet-9.onnx",
    },
    "googlenet": {
        "input": "data_0",
        "shape": [1, 3, 224, 224],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "googlenet/googlenet-9.onnx",
    },
    "caffenet": {
        "input": "data_0",
        "shape": [1, 3, 224, 224],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "caffenet/caffenet-9.onnx",
    },
    "rcnn": {
        "input": "data_0",
        "shape": [1, 3, 224, 224],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "rcnn/rcnn-ilsvrc13-9.onnx",
    },
    "densnet121": {
        "input": "data_0",
        "shape": [1, 3, 224, 224],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "densnet121/densenet-9.onnx",
    },
    "inception-v1": {
        "input": "data_0",
        "shape": [1, 3, 224, 224],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "inception-v1/inception-v1-9.onnx",
    },
    "inception-v2": {
        "input": "data_0",
        "shape": [1, 3, 224, 224],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "inception-v2/inception-v2-9.onnx",
    },
    "inception_v3_torchvision": {
        "input": "x.1",
        "shape": [1, 3, 224, 224],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "inception_v3_torchvision/inception_v3.onnx",
    },
    "shufflenet-v1": {
        "input": "gpu_0/data_0",
        "shape": [1, 3, 224, 224],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "shufflenet-v1/shufflenet-9.onnx",
    },
    "shufflenet-v2": {
        "input": "input",
        "shape": [1, 3, 224, 224],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "shufflenet-v2/shufflenet-v2-10.onnx",
    },
    "zfnet512": {
        "input": "gpu_0/data_0",
        "shape": [1, 3, 224, 224],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "zfnet512/zfnet512-9.onnx",
    },
    "efficientnet-lite4": {
        "input": "images:0",
        "shape": [1, 224, 224, 3],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 3,
        "file": "efficientnet-lite4/efficientnet-lite4-11.onnx",
    },
    "efficientnet-b0": {
        "input": "input.1",
        "shape": [1, 3, 224, 224],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "efficientnet-b0/efficientnet_b0.onnx",
    },
    "EfficientNetV2: efficientnet_v2_m": {
        "input": "input.1",
        "shape": [1, 3, 224, 224],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "EfficientNetV2/efficientnet_v2_m.onnx",
    },
    "EfficientNetV2: efficientnet_v2_s": {
        "input": "input.1",
        "shape": [1, 3, 224, 224],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "EfficientNetV2/efficientnet_v2_s.onnx",
    },
    "mnist": {
        "input": "Input3",
        "shape": [1, 1, 28, 28],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "mnist/mnist-8.onnx",
    },
    "ghostnet": {
        "input": "input.1",
        "shape": [1, 3, 224, 224],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "ghostnet/ghostnet.onnx",
    },
    "condensenet-v2": {
        "input": "input.1",
        "shape": [1, 3, 224, 224],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "condensenet-v2/condensevetv2_a.onnx",
    },
    "mnasnet1_0_torchvision": {
        "input": "input.1",
        "shape": [1, 3, 224, 224],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "mnasnet1_0_torchvision/mnasnet1_0.onnx",
    },
    "DDRNet23_slim": {
        "input": "input_image",
        "shape": [1, 3, 224, 224],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "DDRNet23_slim/DDRNet23_slim.onnx",
    },
    "DDRNet23": {
        "input": "input_image",
        "shape": [1, 3, 224, 224],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "DDRNet23/DDRNet23.onnx",
    },
    "DDRNet39": {
        "input": "input_image",
        "shape": [1, 3, 224, 224],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "DDRNet39/DDRNet39.onnx",
    },
    "HRNet_W18": {
        "input": "input_image",
        "shape": [1, 3, 224, 224],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "HRNet_W18/HRNet-W18.onnx",
    },
    "vovnet19": {
        "input": "input_image",
        "shape": [1, 3, 224, 224],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "vovnet19/vovnet19.onnx",
    },
    "vovnet27_slim": {
        "input": "input_image",
        "shape": [1, 3, 224, 224],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "vovnet27_slim/vovnet27_slim.onnx",
    },
    "vovnet39": {
        "input": "input_image",
        "shape": [1, 3, 224, 224],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "vovnet39/vovnet39.onnx",
    },
    "convnext: convnext_tiny": {
        "input": "input.1",
        "shape": [1, 3, 224, 224],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "convnext/convnext_tiny.onnx",
    },
    "convnext: convnext_small": {
        "input": "input.1",
        "shape": [1, 3, 224, 224],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "convnext/convnext_small.onnx",
    },
    "convnext: convnext_base": {
        "input": "input.1",
        "shape": [1, 3, 224, 224],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "convnext/convnext_base.onnx",
    },
    "r3d_18_torchvision": {
        "input": "0",
        "shape": [1, 3, 16, 112, 112],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "r3d_18_torchvision/r3d_18.onnx",
    },
    "mc3_18_torchvision": {
        "input": "0",
        "shape": [1, 3, 16, 112, 112],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "mc3_18_torchvision/mc3_18.onnx",
    },
    "r2plus1d_18_torchvision": {
        "input": "0",
        "shape": [1, 3, 16, 112, 112],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "r2plus1d_18_torchvision/r2plus1d_18.onnx",
    },
}

transformer = {
    "detr": {
        "input": "samples",
        "shape": [1, 3, 256, 256],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "detr/detr.onnx",
    },
    "CvT": {
        "input": "input.48",
        "shape": [1, 3, 224, 224],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "CvT/CvT-13-224x224-IN-1k.onnx",
    },
    "DINO: dino_deits8": {
        "input": "input",
        "shape": [1, 3, 224, 224],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "DINO/dino_deits8.onnx",
    },
    "DINO: dino_vitb8": {
        "input": "input",
        "shape": [1, 3, 224, 224],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "DINO/dino_vitb8.onnx",
    },
    "CaiT: cait_S24_224": {
        "input": "x",
        "shape": [1, 3, 224, 224],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "CaiT/cait_S24_224.onnx",
    },
    "DeiT: deit_base_patch16_224": {
        "input": "input.1",
        "shape": [1, 3, 224, 224],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "DeiT/deit_base_patch16_224.onnx",
    },
    "DeiT: deit_base_distilled_patch16_224": {
        "input": "x",
        "shape": [1, 3, 224, 224],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "DeiT/deit_base_distilled_patch16_224.onnx",
    },
    "PatchConvnet: S60": {
        "input": "x",
        "shape": [1, 3, 224, 224],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "PatchConvnet/S60.onnx",
    },
    "ResMLP: resmlp_S24_dist": {
        "input": "x",
        "shape": [1, 3, 224, 224],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "ResMLP/resmlp_S24_dist.onnx",
    },
    "loftr": {
        "input": ["data0.1", "data1.1"],
        "shape": [[1, 1, 480, 640], [1, 1, 480, 640]],
        "mean": [[123.675, 116.28, 103.53], [123.675, 116.28, 103.53]],
        "std": [[58.395, 57.12, 57.375], [58.395, 57.12, 57.375]],
        "axis": [1, 1],
        "file": "loftr/indoor_ds_script_sub.onnx",
    },
    "SuperGlue: superglue_v6": {
        "input": ["kpts0", "1", "2", "kpts1", "6", "7"],
        "shape": [[1, 1000, 2], [1, 1000], [1, 256, 1000], [1, 1000, 2], [1, 1000], [1, 256, 1000]],
        "mean": [None, None, None, None, None, None],
        "std": [None, None, None, None, None, None],
        "axis": [None, None, None, None, None, None],
        "file": "SuperGlue/superglue_v6.onnx",
    },
    "conformer": {
        "input": "input.1",
        "shape": [1, 3, 256, 256],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "conformer/conformer.onnx",
    },
}

detection = {
    "ssd": {
        "input": "image",
        "shape": [1, 3, 1200, 1200],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "ssd/ssd-10.onnx",
    },
    "ssd_mobilenet_v1": {
        "input": "image_tensor:0",
        "shape": [1, 512, 512, 3],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 3,
        "file": "ssd_mobilenet_v1/ssd_mobilenet_v1_10.onnx",
    },
    "FasterRCNN": {
        "input": "image",
        "shape": [3, 512, 512],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 0,
        "file": "FasterRCNN/FasterRCNN-10.onnx",
    },
    "MaskRCNN": {
        "input": "image",
        "shape": [3, 512, 512],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 0,
        "file": "MaskRCNN/MaskRCNN-10.onnx",
    },
    "retinanet": {
        "input": "input",
        "shape": [1, 3, 480, 640],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "retinanet/retinanet-9.onnx",
    },
    "retinanet_resnet50_fpn_torchvision": {
        "input": "images",
        "shape": [1, 3, 256, 256],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "retinanet_resnet50_fpn_torchvision/retinanet_resnet50_fpn_torchvision.onnx",
    },
    "tiny-yolov2": {
        "input": "image",
        "shape": [1, 3, 416, 416],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "tiny-yolov2/tinyyolov2-8.onnx",
    },
    "yolov2": {
        "input": "input.1",
        "shape": [1, 3, 416, 416],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "yolov2/yolov2-coco-9.onnx",
    },
    "yolov3": {
        "input": ["input_1", "image_shape"],
        "shape": [[1, 3, 640, 640], [1, 2]],
        "mean": [[123.675, 116.28, 103.53], None],
        "std": [[58.395, 57.12, 57.375], None],
        "axis": [1, None],
        "file": "yolov3/yolov3-10.onnx",
    },
    "tiny-yolov3": {
        "input": ["input_1", "image_shape"],
        "shape": [[1, 3, 640, 640], [1, 2]],
        "mean": [[123.675, 116.28, 103.53], None],
        "std": [[58.395, 57.12, 57.375], None],
        "axis": [1, None],
        "file": "tiny-yolov3/tiny-yolov3-11.onnx",
    },
    "yolov3-lite": {
        "input": "input/input_data:0",
        "shape": [1, 416, 416, 3],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 3,
        "file": "yolov3-lite/model_float32.onnx",
    },
    "yolov3-nano": {
        "input": "input/input_data:0",
        "shape": [1, 416, 416, 3],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 3,
        "file": "yolov3-nano/model_float32.onnx",
    },
    "yolov4": {
        "input": "input_1:0",
        "shape": [1, 416, 416, 3],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 3,
        "file": "yolov4/yolov4.onnx",
    },
    "yolov4-Snapsort": {
        "input": "000_net",
        "shape": [1, 3, 416, 416],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "yolov4-Snapsort/yolov4_GIX_best-416.onnx",
    },
    "tiny-yolov4-Snapsort": {
        "input": "000_net",
        "shape": [1, 3, 416, 416],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "tiny-yolov4-Snapsort/yolov4-tiny_GIX-416.onnx",
    },
    "DUC": {
        "input": "data",
        "shape": [1, 3, 800, 800],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "DUC/ResNet101-DUC-7.onnx",
    },
    "yolov5s_from_customer: best_conv": {
        "input": "images",
        "shape": [1, 3, 640, 640],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "yolov5s_from_customer/best_conv.onnx",
    },
    "yolov5s_from_customer: yolo-rotation": {
        "input": "images",
        "shape": [1, 3, 640, 640],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "yolov5s_from_customer/yolo-rotation.onnx",
    },
    "deeplabv3": {
        "input": "ImageTensor:0",
        "shape": [1, 512, 512, 3],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 3,
        "file": "deeplabv3/deeplabv3_mnv2_pascal_train_aug.onnx",
    },
    "mobile-deeplabv3-plus: mv2": {
        "input": "Input:0",
        "shape": [1, 256, 256, 3],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 3,
        "file": "mobile-deeplabv3-plus/deeplabv3_plus_mnv2_aspp.onnx",
    },
    "mobile-deeplabv3-plus: mv3": {
        "input": "Input:0",
        "shape": [1, 256, 256, 3],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 3,
        "file": "mobile-deeplabv3-plus/deeplabv3_plus_mnv3.onnx",
    },
    "deeplabv3plus": {
        "input": "x.1",
        "shape": [1, 3, 512, 512],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "deeplabv3plus/best_model.onnx",
    },
    "deeplabv3_resnet50_torchvision": {
        "input": "input.1",
        "shape": [1, 3, 520, 520],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "deeplabv3_resnet50_torchvision/deeplabv3_resnet50.onnx",
    },
    "deeplabv3_mobilenet_v3_large_torchvision": {
        "input": "input.1",
        "shape": [1, 3, 520, 520],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "deeplabv3_mobilenet_v3_large_torchvision/deeplabv3_mobilenet_v3_large.onnx",
    },
    "PAN": {
        "input": "x.1",
        "shape": [1, 3, 512, 512],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "PAN/best_model.onnx",
    },
    "mv3_detection": {
        "input": "input",
        "shape": [1, 3, 224, 224],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "mv3_detection/mnv3_detection_opt.onnx",
    },
    "OneClassAnomalyDetection": {
        "input": "input_1_orig",
        "shape": [1, 96, 96, 3],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 3,
        "file": "OneClassAnomalyDetection/weights.onnx",
    },
    "pfld-106": {
        "input": "input",
        "shape": [1, 3, 112, 112],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "pfld-106/pfld-106-v3.onnx",
    },
    "retinaface": {
        "input": "input0",
        "shape": [1, 3, 640, 640],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "retinaface/retinaface_640x640_opt.onnx",
    },
    "retinaface_mnet025_v1": {
        "input": "data",
        "shape": [1, 3, 512, 512],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "retinaface_mnet025_v1/retinaface_mnet025_v1.onnx",
    },
    "retinaface_r50_v1": {
        "input": "data",
        "shape": [1, 3, 480, 640],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "retinaface_r50_v1/retinaface_r50_v1.onnx",
    },
    "rfbnet": {
        "input": "inputdata",
        "shape": [1, 3, 300, 300],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "rfbnet/rfbnet_v2.onnx",
    },
    "UltraLightFaceDetection": {
        "input": "input",
        "shape": [1, 3, 480, 640],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "UltraLightFaceDetection/ultra_light_640.onnx",
    },
    "unet": {
        "input": "0",
        "shape": [1, 3, 256, 256],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "unet/onnx_model_name.onnx",
    },
    "UnetPlusPlus": {
        "input": "x.1",
        "shape": [1, 3, 512, 512],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "UnetPlusPlus/best_model.onnx",
    },
    "yolov5s": {
        "input": "images",
        "shape": [1, 3, 640, 640],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "yolov5s/yolov5s.onnx",
    },
    "yolov5_ultralytics": {
        "input": "images",
        "shape": [1, 3, 640, 640],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "yolov5_ultralytics/yolov5s.onnx",
    },
    "tiny-yolox": {
        "input": "inputs",
        "shape": [1, 3, 416, 416],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "tiny-yolox/yolox_tiny.onnx",
    },
    "yolox": {
        "input": "inputs",
        "shape": [1, 3, 416, 416],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "yolox/yolox_nano.onnx",
    },
    "yolox_series: yolox_s": {
        "input": "images",
        "shape": [1, 3, 640, 640],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "yolox_series/yolox_s.onnx",
    },
    "3d-unet": {
        "input": "input",
        "shape": [1, 4, 224, 224, 160],
        "mean": [123.675, 116.28, 103.53, 123],
        "std": [58.395, 57.12, 57.375, 55],
        "axis": 1,
        "file": "3d-unet/224_224_160.onnx",
    },
    "centernet": {
        "input": "input.1",
        "shape": [1, 3, 1056, 1920],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "centernet/centerface.onnx",
    },
    "dla": {
        "input": "input.1",
        "shape": [1, 3, 512, 512],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "dla/ctdet_coco_dla_2x.onnx",
    },
    "yolor: yolor_csp_x": {
        "input": "input",
        "shape": [1, 3, 512, 512],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "yolor/yolor_csp_x.onnx",
    },
    "yolor: yolor_p6": {
        "input": "input_image",
        "shape": [1, 3, 1280, 1280],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "yolor/yolor_p6.onnx",
    },
    "yolop": {
        "input": "images",
        "shape": [1, 3, 640, 640],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "yolop/yolop-320-320.onnx",
    },
    "SafetyHelmet_yolov3": {
        "input": "input",
        "shape": [1, 3, 416, 416],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "SafetyHelmet_yolov3/SafetyHelmet_YOLOV3.onnx",
    },
    "SafetyHelmet_ssd": {
        "input": "input",
        "shape": [1, 3, 512, 512],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "SafetyHelmet_ssd/SafetyHelmet_SSD.onnx",
    },
    "pointnet_classification": {
        "input": "input_1:0",
        "shape": [2048, 2048, 3],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 2,
        "file": "pointnet_classification/pointnet_classification.onnx",
    },
    "pointpillars": {
        "input": ["input.1", "indices_input"],
        "shape": [[1, 10, 30000, 20], [1, 30000, 2]],
        "mean": [None, None],
        "std": [None, None],
        "axis": [None, None],
        "file": "pointpillars/pointpillars_trt.onnx",
    },
    "lanenet": {
        "input": "input_tensor",
        "shape": [1, 256, 512, 3],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 3,
        "file": "lanenet/model_float32.onnx",
    },
    "M-LSD": {
        "input": "input_image_with_alpha:0",
        "shape": [1, 320, 320, 4],
        "mean": [123.675, 116.28, 103.53, 123],
        "std": [58.395, 57.12, 57.375, 55],
        "axis": 3,
        "file": "M-LSD/tiny_model_float32.onnx",
    },
    "road-segmentation-adas": {
        "input": "data",
        "shape": [1, 512, 896, 3],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 3,
        "file": "road-segmentation-adas/model_float32.onnx",
    },
    "Selfie_Segmentation": {
        "input": "input_1:0",
        "shape": [1, 256, 256, 3],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 3,
        "file": "Selfie_Segmentation/model_float32.onnx",
    },
    "SFA3D": {
        "input": "input.1",
        "shape": [1, 3, 608, 608],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "SFA3D/sfa3d_608x608_float32.onnx",
    },
    "fcn_resnet50": {
        "input": "input",
        "shape": [1, 3, 320, 480],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "fcn_resnet50/fcn-resnet50-11.onnx",
    },
    "fcn_resnet50_torchvision": {
        "input": "input.1",
        "shape": [1, 3, 224, 224],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "fcn_resnet50_torchvision/fcn_resnet50.onnx",
    },
    "yolact": {
        "input": "input.1",
        "shape": [1, 3, 256, 256],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "yolact/yolact_edge_mobilenetv2_54_800000_256x256.onnx",
    },
    "yolact_edge": {
        "input": "input_1",
        "shape": [1, 3, 550, 550],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "yolact_edge/model_float32.onnx",
    },
    "nanodet": {
        "input": "i",
        "shape": [1, 3, 320, 320],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "nanodet/nanodet_320x320.onnx",
    },
    "ENet": {
        "input": "imgs_ph:0",
        "shape": [1, 512, 1024, 3],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 3,
        "file": "ENet/model_float32.onnx",
    },
    "U2Net": {
        "input": "x:0",
        "shape": [1, 320, 320, 3],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 3,
        "file": "U2Net/model_float32.onnx",
    },
    "BiSeNet": {
        "input": "input",
        "shape": [1, 3, 512, 512],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "BiSeNet/my_param.onnx",
    },
    "BiSeNetV2": {
        "input": "input_tensor:0",
        "shape": [1, 480, 640, 3],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 3,
        "file": "BiSeNetV2/model_float32.onnx",
    },
    "BiSeNetV1_coco": {
        "input": "input_image",
        "shape": [1, 3, 512, 512],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "BiSeNetV1_coco/bisenetv1_coco.onnx",
    },
    "BiSeNetV1_city": {
        "input": "input_image",
        "shape": [1, 3, 1024, 1024],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "BiSeNetV1_city/bisenetv1_city.onnx",
    },
    "BiSeNetV2_coco": {
        "input": "input_image",
        "shape": [1, 3, 640, 640],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "BiSeNetV2_coco/bisenetv2_coco.onnx",
    },
    "BiSeNetV2_city": {
        "input": "input_image",
        "shape": [1, 3, 1024, 1024],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "BiSeNetV2_city/bisenetv2_city.onnx",
    },
    "TextBoxes++": {
        "input": "input_1:0",
        "shape": [1, 256, 256, 3],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 3,
        "file": "TextBoxes++/dstbpp512fl_sythtext_256x256_float32.onnx",
    },
    "East_Text_Detection": {
        "input": "input_images:0",
        "shape": [1, 320, 320, 3],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 3,
        "file": "East_Text_Detection/model_float32.onnx",
    },
    "Person_Reidentification": {
        "input": "inputs:0 ",
        "shape": [1, 256, 128, 3],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 3,
        "file": "Person_Reidentification/model_float32.onnx",
    },
    "SpineNet": {
        "input": "Placeholder:0",
        "shape": [1, 384, 384, 3],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 3,
        "file": "SpineNet/model_float32.onnx",
    },
    "mtcnn: det1": {
        "input": "input",
        "shape": [1, 3, 12, 12],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "mtcnn/det1.onnx",
    },
    "mtcnn: det2": {
        "input": "input",
        "shape": [1, 3, 24, 24],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "mtcnn/det2.onnx",
    },
    "mtcnn: det3": {
        "input": "input",
        "shape": [1, 3, 48, 48],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "mtcnn/det3.onnx",
    },
    "efficientdet-d0": {
        "input": "data",
        "shape": [1, 3, 512, 512],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "efficientdet-d0/efficientdet-d0.onnx",
    },
    "efficientdet-d1": {
        "input": "data",
        "shape": [1, 3, 640, 640],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "efficientdet-d1/efficientdet-d1.onnx",
    },
    "DDRNet23_slim_seg": {
        "input": "input_image",
        "shape": [1, 3, 1024, 1024],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "DDRNet23_slim_seg/DDRNet23_slim_seg.onnx",
    },
    "DDRNet23_seg": {
        "input": "input_image",
        "shape": [1, 3, 1024, 1024],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "DDRNet23_seg/DDRNet23_seg.onnx",
    },
    "HRNet_W48_ocr_seg": {
        "input": "input_image",
        "shape": [1, 3, 520, 520],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "HRNet_W48_ocr_seg/HRNet_W48_OCR_coco.onnx",
    },
    "FCOS": {
        "input": "input_image",
        "shape": [1, 3, 800, 1216],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "FCOS/fcos_imprv_R_50_FPN_1x.onnx",
    },
    "faceboxes": {
        "input": "input_image",
        "shape": [1, 3, 1024, 1024],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "faceboxes/faceboxes.onnx",
    },
    "CascadeTableNet": {
        "input": "input",
        "shape": [1, 3, 320, 320],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "CascadeTableNet/CascadeTableNet.onnx",
    },
    "efficientdet_lite": {
        "input": "serving_default_images:0",
        "shape": [1, 320, 320, 3],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 3,
        "file": "efficientdet_lite/efficientdet_lite.onnx",
    },
    "knift": {
        "input": "rgb_to_grayscale_1:0",
        "shape": [200, 32, 32, 1],
        "mean": 123,
        "std": 55,
        "axis": 3,
        "file": "knift/knift.onnx",
    },
    "object_detection_mobile_object_localizer": {
        "input": "normalized_input_image_tensor",
        "shape": [1, 3, 192, 192],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "object_detection_mobile_object_localizer/object_detection_mobile_object_localizer.onnx",
    },
    "pedestrian_and-vehicle_detector_adas": {
        "input": "data",
        "shape": [1, 3, 384, 672],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "pedestrian_and-vehicle_detector_adas/pedestrian-and-vehicle-detector-adas-0001.onnx",
    },
    "pedestrian_detection_adas": {
        "input": "data",
        "shape": [1, 3, 384, 672],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "pedestrian_detection_adas/pedestrian-detection-adas-0002.onnx",
    },
    "person_detection": {
        "input": "image",
        "shape": [1, 3, 512, 512],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "person_detection/person-detection-0202.onnx",
    },
    "person_detection_asl": {
        "input": "image",
        "shape": [1, 3, 320, 320],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "person_detection_asl/person-detection-asl.onnx",
    },
    "person_vehicle_bike_detection_crossroad": {
        "input": "input_1",
        "shape": [1, 3, 512, 512],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "person_vehicle_bike_detection_crossroad/person-vehicle-bike-detection-crossroad-1016.onnx",
    },
    "spaghettinet_edgetpu": {
        "input": "normalized_input_image_tensor",
        "shape": [1, 3, 320, 320],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "spaghettinet_edgetpu/spaghettinet_edgetpu.onnx",
    },
    "text_detection_db": {
        "input": "input",
        "shape": [1, 3, 480, 640],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "text_detection_db/text_detection_db.onnx",
    },
    "vehicle_detection": {
        "input": "image",
        "shape": [1, 3, 256, 256],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "vehicle_detection/vehicle-detection-0200.onnx",
    },
    "vehicle_license_plate_detection_barrier": {
        "input": "Placeholder",
        "shape": [1, 3, 300, 300],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "vehicle_license_plate_detection_barrier/vehicle-license-plate-detection-barrier-0106.onnx",
    },
    "yolact_resnet50_fpn": {
        "input": "input.1",
        "shape": [1, 3, 550, 550],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "yolact_resnet50_fpn/yolact-resnet50-fpn.onnx",
    },
    "YOLOF": {
        "input": "inputs",
        "shape": [1, 3, 608, 608],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "YOLOF/YOLOF.onnx",
    },
    "BackgroundMattingV2": {
        "input": ["src", "bgr"],
        "shape": [[1, 3, 720, 1280], [1, 3, 720, 1280]],
        "mean": [[123.675, 116.28, 103.53], [123.675, 116.28, 103.53]],
        "std": [[58.395, 57.12, 57.375], [58.395, 57.12, 57.375]],
        "axis": [1, 1],
        "file": "BackgroundMattingV2/BackgroundMattingV2.onnx",
    },
    "BodyPix": {
        "input": "sub_2",
        "shape": [1, 240, 320, 3],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 3,
        "file": "BodyPix/BodyPix.onnx",
    },
    "DeeplabV3_plus": {
        "input": "input_1:0",
        "shape": [1, 200, 400, 3],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 3,
        "file": "DeeplabV3_plus/DeeplabV3_plus.onnx",
    },
    "ERFNet": {
        "input": "input_1:0",
        "shape": [1, 256, 512, 3],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 3,
        "file": "ERFNet/ERFNet.onnx",
    },
    "Fast_SCNN": {
        "input": "input.1",
        "shape": [1, 3, 192, 384],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "Fast_SCNN/Fast_SCNN.onnx",
    },
    "human_segmentation_pphumanseg": {
        "input": "x",
        "shape": [1, 3, 192, 192],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "human_segmentation_pphumanseg/human_segmentation_pphumanseg.onnx",
    },
    "MediaPipe_Meet_Segmentation": {
        "input": "input_1:0",
        "shape": [1, 96, 160, 3],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 3,
        "file": "MediaPipe_Meet_Segmentation/MediaPipe_Meet_Segmentation.onnx",
    },
    "MODNet": {
        "input": "input",
        "shape": [1, 3, 512, 512],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "MODNet/MODNet.onnx",
    },
    "SUIM_Net": {
        "input": "input_1",
        "shape": [1, 3, 240, 320],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "SUIM_Net/SUIM_Net.onnx",
    },
    "vision_segmentation_default_argmax": {
        "input": "serving_default_input_2:0",
        "shape": [1, 3, 512, 512],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "vision_segmentation_default_argmax/models_edgetpu_checkpoint_and_tflite_vision_segmentation-edgetpu_tflite_default_argmax.onnx",
    },
    "vision_segmentation_fused_argmax": {
        "input": "serving_default_input_2:0",
        "shape": [1, 3, 512, 512],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "vision_segmentation_fused_argmax/models_edgetpu_checkpoint_and_tflite_vision_segmentation-edgetpu_tflite_fused_argmax.onnx",
    },
    "BASNet": {
        "input": "input_image",
        "shape": [1, 3, 256, 256],
        "mean": [123.675, 116.28, 103.53],
        "std": [58.395, 57.12, 57.375],
        "axis": 1,
        "file": "BASNet/basnet.onnx",
    },
}

body = {}

manipulation = {}

nlp = {}

quant = {}

test = {}

meta = {}
meta.update(classification)
meta.update(transformer)
meta.update(detection)
# meta.update(body)
# meta.update(manipulation)
# meta.update(nlp)
# meta.update(quant)
# meta.update(test)

source_path = "/data/share/demodels-lfs/onnx"
target_path = "/home/zhaojinxi/Documents/onnx_result"

models = {}
for name in os.listdir(source_path):
    model_path = os.path.join(source_path, name)
    tmp1 = []
    for file in os.listdir(model_path):
        if os.path.splitext(file)[1] == ".onnx":
            tmp1.append(file)
    models[name] = {"file": tmp1}
for k, v in meta.items():
    if ": " in k:
        tmp1, tmp2 = k.split(": ")
        for i in models[tmp1]["file"]:
            print(os.path.join(k, i))
    else:
        for i in models[k]["file"]:
            print(os.path.join(k, i))

for name, v in meta.items():
    save_path = os.path.join(target_path, name)
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    log_path = os.path.join(save_path, "log.txt")

    rerun = True
    if os.path.exists(log_path):
        with open(log_path, "r") as f:
            line = f.readlines()
            if line != [] and line[-1] != "finished\n":
                for i in line:
                    print(i)
                print(name)
                print()

for name, v in meta.items():
    save_path = os.path.join(target_path, name)
    log_path = os.path.join(save_path, "log.txt")

    rerun = True
    if os.path.exists(log_path):
        with open(log_path, "r") as f:
            line = f.readlines()
            if line != [] and line[-1] == "finished\n":
                rerun = False

    if rerun:
        if os.path.exists(save_path):
            shutil.rmtree(save_path)
        os.makedirs(save_path)

        log = open(log_path, "w")
        sys.stdout = log

        file_path = os.path.join(source_path, v["file"])
        model = onnx.load(file_path)
        log.write("input shape:\n" + str(v["shape"]) + "\n\n")

        quantize_config = {}
        quantize_config["calib_method"] = "percentile_0.9999"

        try:
            if isinstance(v["input"], list):
                input_shape = {}
                for tmp1, tmp2 in zip(v["input"], v["shape"]):
                    input_shape[tmp1] = tmp2
            else:
                input_shape = {v["input"]: v["shape"]}

            mod, params = relay.frontend.from_onnx(model, shape=input_shape)
            log.write("ir:\n" + str(v["shape"]) + "\n\n")
            log.write(mod["main"].__str__() + "\n\n")

            _run(
                name,
                mod,
                params,
                quantize_config,
                v["input"],
                v["mean"],
                v["std"],
                v["axis"],
                target_path,
            )

            log.write("finished\n")
        except Exception:
            log.write(traceback.format_exc())

        log.close()
