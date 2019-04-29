#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import yaml
from dotmap import DotMap


class Config(object):

    @classmethod
    def setup(clf, config_dict=None, config_file=None):
        if config_dict:
            cfg = DotMap(config_dict)
        else:
            with open(config_file, 'r') as f:
                cfg = yaml.load(f)
            cfg = DotMap(cfg)
        return cfg
