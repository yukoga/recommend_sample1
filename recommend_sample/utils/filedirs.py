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

import os
from shutil import rmtree


def is_dir(filepath):
    return os.path.isdir(filepath)


def is_file(filepath):
    return os.path.isfile(filepath)


def is_file_exists(filepath):
    dir, file = os.path.split(filepath)
    _ = create_dir(dir)
    if not os.path.isfile(filepath):
        filepath = False
    return filepath


def create_dir(dirname, force=False):
    dir, file = os.path.split(dirname)

    if not os.path.isdir(dir) or force:
        os.makedirs(dir, exist_ok=True)
    return dir


def delete_dir(dirname):
    _dir = os.path.isdir(dirname)
    _file = os.path.isfile(dirname)
    if _dir:
        rmtree(dirname)
    elif _file:
        os.unlink(dirname)
    else:
        pass
