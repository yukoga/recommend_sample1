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


class ToyRecommend:
    def __init__(self):
        self.trained = None

    def fit(self, dataset):
        '''The method for fit model for given training dataset.

        Args:
            dataset (SimpleToy): Training dataset
                as an instance of SimpleToy class.

        '''
        self.trained = dataset

    def predict(self, key, top_n=None):
        '''The method for predict top_n recommendations for given key
        based on trained model.

        Args:
            key (int): The key for which the model predict recommendations.
            top_n (int): Number of predicted recommendations. Default: None.
                if not specify top_n, then you'll get all recommendations for
                given key.

        Returns:
            pred (list): Recommendations for a given key.

        '''
        if not top_n:
            top_n = self.trained.shape[1]
        return self.trained[key][:top_n]
