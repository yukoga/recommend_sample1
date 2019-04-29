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

import pandas as pd
from recommend_sample.utils.filedirs import is_file_exists, create_dir


class DataLoader(object):
    @classmethod
    def load_data_from_bq(cls,
                          query=None,
                          project_id=None,
                          dialect='standard',
                          filepath=None, force_update=False):
        """ Fetch data from BigQuery.
        Args:
            query (str): SQL.
            project_id (str): Google Cloud project id \
                on which given SQL will be executed.
            dialect (str): SQL dialect of BigQuery. Turn to be 'legacy' \
                if you'd like to execute legacy SQL. Default: 'standard'.
            filepath (str): The path to file which contains data \
                previously loaded from BigQuery.
            force_update (bool): The flag to specify if \
                force to access API to get data. If set it to True, then you \
                will get data from API no matter what the data exists \
                in local file or not.  Default: False.

        Returns:
            dataframe (pandas.DataFrame): DataFrame object which contains data \
                resulted in executing given SQL.

        """
        if filepath:
            if not is_file_exists(filepath) or force_update:
                dataframe = pd.read_gbq(
                    query,
                    project_id=project_id,
                    dialect=dialect)
                create_dir(filepath)
                dataframe.to_csv(filepath, index=False)
            else:
                dataframe = pd.read_csv(filepath)
        else:
            dataframe = pd.read_gbq(
                query,
                project_id=project_id,
                dialect=dialect)

        return dataframe
