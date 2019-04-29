#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from recommend_sample.utils.config import Config


def test_init():
    test_config = {
        'max': 10,
        'min': 3,
        'test': 3,
        'project': 'gcp-jp',
        'dataset': '73156703',
        'boolean': True
    }

    config = Config.setup(config_file='./tests/workspace/config.yml')
    assert config.sanity_test.MAX == test_config['max']
    assert config.sanity_test.MIN == test_config['min']
    assert config.sanity_test.TEST == test_config['test']
    assert config.sanity_test.project == test_config['project']
    assert config.sanity_test.dataset == test_config['dataset']
    assert config.sanity_test.boolean == test_config['boolean']


def test_config_from_dict():
    test_config = {
        'max': 10,
        'min': 3,
        'test': 100,
        'nested': {
            'name': 'test_config',
            'number': 12345,
            'boolean': True
        }
    }

    config = Config.setup(config_dict=test_config)

    assert config.max == 10
    assert config.min == 3
    assert config.test == 100
    assert config.nested.name == 'test_config'
    assert config.nested.number == 12345
    assert config.nested.boolean
