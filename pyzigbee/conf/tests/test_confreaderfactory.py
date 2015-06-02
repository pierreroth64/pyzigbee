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
from pyzigbee.core.exceptions import PyZigBeeBadFormatError, PyZigBeeResourceNotFound

class TestConfReaderFactory:

    def test_conf_reader_create_json(self):

        conf_filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), "conf.json")
        assert_true(isinstance(ConfReaderFactory.create_conf_reader(conf_filename=conf_filename), JSONConfReader))

    def test_conf_reader_create_none(self):
        assert_true(isinstance(ConfReaderFactory.create_conf_reader(), DoNothingConfReader))

    def test_conf_reader_create_missing_key(self):
        conf_filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), "conf_missing.json")
        assert_raises(PyZigBeeBadFormatError, ConfReaderFactory.create_conf_reader, conf_filename)

    def test_conf_reader_create_file_not_found(self):
        assert_raises(PyZigBeeResourceNotFound, ConfReaderFactory.create_conf_reader, "not_found.json")
