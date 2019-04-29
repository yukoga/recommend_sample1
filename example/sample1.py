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
from recommend_sample.models.toy_recommend import ToyRecommend
from recommend_sample.datasets.simple_toy import load_simpletoy


def main(args):
    train_set = load_simpletoy()
    print('Training data loaded.')

    rec = ToyRecommend()
    rec.fit(train_set)
    print('Finish training for recommendations')

    key = args.key if args.key else 0
    top_n = args.top_n if args.top_n else train_set.shape[1]

    results = rec.predict(key, top_n)

    print(f'Top {top_n} recommendations for item {key}'
          f' is {results}.')


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
    args = parser.parse_args()
    main(args)
