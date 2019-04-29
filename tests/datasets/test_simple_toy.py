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
from recommend_sample.datasets.simple_toy import load_simpletoy


@pytest.fixture(scope="module")
def correct():
    return {
        'data': {
            0: [4, 1, 4, 4, 3],
            1: [4, 2, 4, 3, 2],
            2: [4, 1, 3, 0, 0],
            3: [1, 0, 2, 1, 1],
            4: [3, 0, 1, 1, 0]
        },
        'shape': (5, 5)
    }


def test_init():
    toy_data = load_simpletoy()
    assert isinstance(toy_data, dict)


def test_shape(correct):
    toy_data = load_simpletoy()
    assert toy_data.shape == correct['shape']


def test_all_elements(correct):
    toy_data = load_simpletoy()
    assert toy_data == correct['data']
