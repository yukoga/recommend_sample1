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

from collections import OrderedDict, Counter


class OrderedCounter(Counter, OrderedDict):
    pass


class RankRecommend:
    def __init__(self):
        self.trained = None

    def fit(self, dataset):
        """The method for fit model for given training dataset based on
        frequencies.

        Args:
            dataset (ToyDataset): Training dataset
                as an instance of SimpleToy class.

        """
        self.trained = self.sort_by_occurence(dataset)

    def predict(self, key, top_n=None):
        """The method for predict top_n recommendations for given key
        based on trained model.

        Args:
            key (int): The key for which the model predict recommendations.
            top_n (int): Number of predicted recommendations. Default: None.
                if not specify top_n, then you'll get all recommendations for
                given key.

        Returns:
            pred (list): Recommendations for a given key.

        """
        if not top_n:
            top_n = len(self.trained[0])
        return self.trained[key][:top_n]

    def sort_by_occurence(self, dataset):
        output = dict()
        keys = dataset.keys()
        data_list = sum(list(dataset.values()), [])
        c = OrderedCounter(data_list)
        for k in keys:
            l = c.copy()
            _ = l.pop(k)
            ks = list(l)
            output.update({
                k: sorted(l, key=lambda x: (-l[x], ks.index(x)))
            })
        return output
