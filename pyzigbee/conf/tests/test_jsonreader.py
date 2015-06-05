#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2015 Legrand France
# All rights reserved

import os
from nose.tools import assert_equal
from pyzigbee.conf.jsonreader import JSONConfReader


class TestJSONConfReader:

    def setup(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        conf_filename = os.path.join(current_dir, "conf.json")
        self.conf_reader = JSONConfReader(conf_filename)

    def test_conf_reader_arg_override(self):

        # read conf from file
        assert_equal("/dev/ttyUSB0",
                     self.conf_reader.conf["088328"]["driver"]["args"]["port"])
        args = self.conf_reader.override_args_with_conf("088328",
                                                        args={"port": "COM1"})

        # args should be changed with values overriden by file values
        assert_equal("/dev/ttyUSB0", args["port"])
