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

import glob
import os


class SqlLoader(object):
    @classmethod
    def load_sql(cls, source_dir, ext='sql'):
        """
        Load sqls from multiple files in source_dir.
        Args:
            source_dir (str): directory path where sql files are located.
                required, make sure it end with slash '/'.
            ext (str): a file extension. Default: sql

        Returns:

        """
        ext = '*.{ext}'.format(ext=ext)
        files = glob.glob(source_dir + '{ext}'.format(ext=ext))
        sqls = {}
        for file in files:
            root, _ = os.path.splitext(file)
            root = root.split('/')[-1]
            with open(file, 'r') as f:
                sqls[root] = f.read().replace('\n', '')

        return sqls