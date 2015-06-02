#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2015 Legrand France
# All rights reserved

import json
import logging

from pyzigbee.core.exceptions import PyZigBeeBadFormatError

class JSONConfReader(object):
    """Reader for configuration: JSON format"""

    def __init__(self, conf_filename):
        self.conf_filename = conf_filename
        self.conf = None
        self.logger = logging.getLogger(__name__)
        try:
            with open(conf_filename, 'r') as conf_file:
                self.conf = json.load(fp=conf_file, encoding='ascii')
                for ref in self.conf.keys():
                    self._check_format(self.conf[ref])
        except ValueError as error:
            raise PyZigBeeBadFormatError("Could not load JSON data from: %s" %  conf_filename)

    def _check_format(self, conf):
        if "driver" not in conf.keys() or "args" not in conf["driver"].keys():
            raise PyZigBeeBadFormatError("missing 'driver' and/or 'args' JSON keys in: %s" \
                                         % self.conf_filename)

    def override_args_with_conf(self, ref, args):
        if ref not in self.conf.keys():
            self.logger.warn("%s reference not found in %s", ref, self.conf_filename)
        else:
            for conf_k, conf_v in self.conf[ref]["driver"]["args"].items():
                args[conf_k] = conf_v
        return args
