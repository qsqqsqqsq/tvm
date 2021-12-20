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
# pylint: disable=unused-argument,inconsistent-return-statements
"""convert multiply to conv2d"""
import tvm
from tvm import relay
from tvm.relay.expr_functor import ExprMutator


@relay.transform.function_pass(opt_level=3)
class ConvertMultiplyToConv(ExprMutator):
    """ConvertMultiplyToConv"""

    def visit_call(self, call):
        visited = super().visit_call(call)
        if visited.op == tvm.relay.op.get("multiply") and isinstance(
            visited.args[1], tvm.relay.Constant
        ):

            shape0 = call.args[0].checked_type.shape
            shape1 = call.args[1].checked_type.shape
            if len(shape0) != 4:
                return visited

            if len(shape1) == 1 and shape1[0].value == shape0[3].value:
                layout = "NHWC"
                c_idx = 3
                kernel_layout = "HWOI"
                r_shape = [1, 1, shape1[0].value, 1]
            elif (
                len(shape1) == 3
                and shape1[0].value == shape0[1].value
                and shape1[1].value == shape1[2].value == 1
            ):
                layout = "NCHW"
                c_idx = 1
                kernel_layout = "OIHW"
                r_shape = [shape1[0].value, 1, 1, 1]
            else:
                return visited

            channels = shape0[c_idx].value
            assert channels == shape1[0].value
            conv2d_arg = relay.Constant(
                tvm.nd.array(visited.args[1].data.asnumpy().reshape(r_shape))
            )
            return relay.nn.conv2d(
                visited.args[0],
                conv2d_arg,
                data_layout=layout,
                kernel_layout=kernel_layout,
                groups=channels,
                kernel_size=(1, 1),
            )

        return visited

    def transform_function(self, func, mod, ctx):
        return self.visit(func)
