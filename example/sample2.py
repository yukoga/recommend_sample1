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

import argparse
from recommend_sample.datasets.toy_dataset import load_toydataset
from recommend_sample.models.rank_recommend import RankRecommend


def main(args):
    train_set = load_toydataset(keys=list(range(6)), seed=123)
    print('Training data loaded.')

    rec = RankRecommend()
    rec.fit(train_set)
    print('Finish training for recommendations')

    key = args.key if args.key else 0
    top_n = args.top_n if args.top_n else train_set.shape[1]

    results = rec.predict(key, top_n)

    print(f'Top {top_n} recommendations for item {key}'
          f' is {results}.')

    if args.all:
        print('\n')
        print('/*** training dataset ***/')
        for k, v in train_set.items():
            print(k, v)
        print('\n')

        print('/*** recommendation results ***/')
        for k in train_set.keys():
            res = rec.predict(k)
            print(f'Recommendations for item {k} is {res}.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--key',
                        type=int,
                        # default=0,
                        help='Identifier for getting recommend.')
    parser.add_argument('--top_n',
                        type=int,
                        # default=1,
                        help='The number of recommendations.')
    parser.add_argument('--all',
                        action='store_true',
                        help='The flag to specify if show all recommendations.')
    args = parser.parse_args()
    main(args)
