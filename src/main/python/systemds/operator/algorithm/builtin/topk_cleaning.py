# -------------------------------------------------------------
#
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
#
# -------------------------------------------------------------

# Autogenerated By   : src/main/python/generator/generator.py
# Autogenerated From : scripts/builtin/topk_cleaning.dml

from typing import Dict, Iterable

from systemds.operator import OperationNode, Matrix, Frame, List, MultiReturn, Scalar
from systemds.script_building.dag import OutputType
from systemds.utils.consts import VALID_INPUT_TYPES


def topk_cleaning(dataTrain: Frame,
                  primitives: Frame,
                  parameters: Frame,
                  evaluationFunc: str,
                  evalFunHp: Matrix,
                  **kwargs: Dict[str, VALID_INPUT_TYPES]):
    """
    This function cleans top-K item (where K is given as input)for a given list of users.
    metaData[3, ncol(X)] : metaData[1] stores mask, metaData[2] stores schema, metaData[3] stores FD mask
    """
    params_dict = {'dataTrain': dataTrain, 'primitives': primitives, 'parameters': parameters, 'evaluationFunc': evaluationFunc, 'evalFunHp': evalFunHp}
    params_dict.update(kwargs)
    
    vX_0 = Frame(dataTrain.sds_context, '')
    vX_1 = Matrix(dataTrain.sds_context, '')
    vX_2 = Matrix(dataTrain.sds_context, '')
    vX_3 = Scalar(dataTrain.sds_context, '')
    vX_4 = Matrix(dataTrain.sds_context, '')
    vX_5 = Frame(dataTrain.sds_context, '')
    output_nodes = [vX_0, vX_1, vX_2, vX_3, vX_4, vX_5, ]

    op = MultiReturn(dataTrain.sds_context, 'topk_cleaning', output_nodes, named_input_nodes=params_dict)

    vX_0._unnamed_input_nodes = [op]
    vX_1._unnamed_input_nodes = [op]
    vX_2._unnamed_input_nodes = [op]
    vX_3._unnamed_input_nodes = [op]
    vX_4._unnamed_input_nodes = [op]
    vX_5._unnamed_input_nodes = [op]

    return op