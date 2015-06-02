#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2015 Legrand France
# All rights reserved

from nose.tools import assert_equal

from pyzigbee.conf.donothingreader import DoNothingConfReader

class TestDoNothingConfReader:

    def setup(self):
        self.conf_reader = DoNothingConfReader()
        self.conf = {
                        "088328": {
                            "driver": {
                                "args": {
                                    "port": "/dev/ttyUSB0",
                                    "baudrate": "19200"
                                }
                            }
                        }
                    }

    def test_conf_reader_no_arg_overriden(self):

        args = self.conf["088328"]["driver"]["args"]
        assert_equal(args, self.conf_reader.override_args_with_conf("088328", args))


