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

from recommend_sample.utils.sql_loader import SqlLoader


def test_load_sql():
    correct_sql = {}
    correct_sql['basic'] = str(
        'SELECT CONCAT(ein, CAST(tax_pd AS STRING)) AS id'
        ', ein, tax_pd, subseccd, totcntrbs, prgmservrev, othrinvstinc'
        ', grsamtsalesastothr, basisalesexpnsothr, grsincgaming, totrevnue '
        'FROM `bigquery-public-data.irs_990.irs_990_ez_20*` '
        'WHERE _TABLE_SUFFIX BETWEEN \'20180401\' AND \'20180501\''
        'ORDER BY id, ein, tax_pd')
    correct_sql['transaction'] = str(
        'SELECT (SUM(total_transactions_per_user) / COUNT(fullVisitorId)) '
        'AS avg_total_transactions_per_user '
        'FROM ('
        'SELECT'
        'fullVisitorId'
        ', SUM(totals.transactions) AS total_transactions_per_user'
        'FROM '
        '`bigquery-public-data.google_analytics_sample.ga_sessions_*` '
        'WHERE _TABLE_SUFFIX BETWEEN \'20170701\' AND \'20170731\' '
        'AND totals.transactions IS NOT NULL '
        'GROUP BY fullVisitorId)')

    source_dir = './tests/workspace/sql/'
    sqls = SqlLoader.load_sql(source_dir=source_dir)
    assert sqls['basic'] == correct_sql['basic']
    assert sqls['transaction'] == correct_sql['transaction']
