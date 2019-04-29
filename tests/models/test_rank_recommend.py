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
from recommend_sample.models.rank_recommend import RankRecommend
from recommend_sample.datasets.toy_dataset import load_toydataset


@pytest.fixture(scope="module")
def correct():
    return {
        'data': {
            0: [2, 1, 3, 5, 4],
            1: [5, 2, 4, 3, 0],
            2: [3, 4, 5, 0, 1],
            3: [1, 4, 5, 0, 2],
            4: [3, 1, 0, 2, 5],
            5: [4, 3, 1, 0]
        },
        'shape': (5, 5)
    }


def test_fit():
    train_set = load_toydataset(keys=list(range(6)), seed=123)
    rec = RankRecommend()
    rec.fit(train_set)
    assert isinstance(rec.trained, dict)


def test_predict(correct):
    train_set = load_toydataset(keys=list(range(6)), seed=123)
    rec = RankRecommend()
    rec.fit(train_set)
    assert rec.predict(0) == correct['data'][0]
    assert rec.predict(1, top_n=3) == correct['data'][1][:3]
