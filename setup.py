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

from distutils.core import setup
import recommend_sample

setup(
    name='recommend_sample',
    version=recommend_sample.__version__,
    description='Recommendations engine sample code.',
    license='Apache License 2.0',
    author='yukoga',
    author_email='yukoga@gmail.com',
    url='https://github.com/yukoga/recommend_sample1.git',
    packages=[
        'recommend_sample',
        'recommend_sample.datasets',
        'recommend_sample.models',
    ],
    install_requires=open('requirements.txt').read().splitlines(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Intended Audience :: Developers',
        'Topic :: Utilities',
        'License :: Apache License 2.0',
        'Operating System :: OS Independent',
    ])
