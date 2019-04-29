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

import numpy as np


class ToyDataset(dict):
    def __init__(self, keys, n_per_item, seed):
        super().__init__()
        if seed:
            np.random.seed(seed)
        for key in keys:
            cand = list(set(keys).difference([key]))
            self.update({key: np.random.choice(cand, n_per_item).tolist()})

    @property
    def shape(self):
        return (len(self.keys()), len(list(self.values())[0]))


def load_toydataset(keys=list(range(5)), n_per_item=20, seed=None):
    return ToyDataset(keys=keys, n_per_item=n_per_item, seed=seed)
