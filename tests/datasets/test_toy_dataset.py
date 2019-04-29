# -*- coding: utf-8 -*-

# Copyright 2018 yukoga. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================


from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import pytest
from recommend_sample.datasets.toy_dataset import load_toydataset


@pytest.fixture(scope="module")
def correct():
    return {
        'data': {
            0: [3, 2, 3, 3, 1, 3, 3, 2, 4, 3, 4, 2, 3, 2, 1, 2, 3, 4, 2, 1],
            1: [3, 0, 4, 2, 4, 3, 2, 0, 0, 0, 0, 2, 4, 4, 3, 0, 4, 3, 0, 4],
            2: [0, 1, 0, 4, 1, 4, 0, 0, 0, 3, 1, 1, 3, 3, 4, 3, 1, 0, 0, 4],
            3: [2, 1, 0, 4, 2, 2, 2, 2, 1, 2, 0, 4, 4, 4, 1, 0, 2, 0, 2, 1],
            4: [3, 2, 0, 2, 2, 3, 0, 3, 3, 2, 3, 1, 3, 2, 1, 3, 1, 2, 0, 0]
        },
        'shape': (5, 20)
    }


def test_init():
    toy_data = load_toydataset(seed=123)
    assert isinstance(toy_data, dict)


def test_shape(correct):
    toy_data = load_toydataset(seed=123)
    assert toy_data.shape == correct['shape']


def test_all_elements(correct):
    toy_data = load_toydataset(seed=123)
    assert toy_data == correct['data']
