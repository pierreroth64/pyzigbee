#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2015 Legrand France
# All rights reserved

import os
from nose.tools import assert_raises, assert_true
from pyzigbee.conf.factory import ConfReaderFactory
from pyzigbee.conf.donothingreader import DoNothingConfReader
from pyzigbee.conf.jsonreader import JSONConfReader
from pyzigbee.core.exceptions import PyZigBeeBadFormat
from pyzigbee.core.exceptions import PyZigBeeResourceNotFound


class TestConfReaderFactory:

    def setup(self):
        self.current_dir = os.path.dirname(os.path.abspath(__file__))

    def test_conf_reader_create_json(self):
        filename = os.path.join(self.current_dir, "conf.json")
        reader = ConfReaderFactory.create_conf_reader(conf_filename=filename)
        assert_true(isinstance(reader, JSONConfReader))

    def test_conf_reader_create_none(self):
        reader = ConfReaderFactory.create_conf_reader()
        assert_true(isinstance(reader, DoNothingConfReader))

    def test_conf_reader_create_missing_key(self):
        conf_filename = os.path.join(self.current_dir, "conf_missing.json")
        assert_raises(PyZigBeeBadFormat,
                      ConfReaderFactory.create_conf_reader,
                      conf_filename)

    def test_conf_reader_create_file_not_found(self):
        assert_raises(PyZigBeeResourceNotFound,
                      ConfReaderFactory.create_conf_reader,
                      "not_found.json")
