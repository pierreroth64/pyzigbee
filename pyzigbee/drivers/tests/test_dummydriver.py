#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2015 Legrand France
# All rights reserved
from nose.tools import assert_raises, assert_true, assert_false, assert_equal

from pyzigbee.drivers.dummy import DummyDriver
from pyzigbee.core.exceptions import PyZigBeeDenied

class TestDummyDriver:

    def setup(self):
        self.drv =  DummyDriver()

    def tearDown(self):
        self.drv = None

    def test_initially_open(self):
        assert_false(self.drv.is_open)

    def test_open(self):
        self.drv.open()
        assert_true(self.drv.is_open)

    def test_close(self):
        self.drv.open()
        self.drv.close()
        assert_false(self.drv.is_open)

    def test_already_open(self):
        self.drv.open()
        assert_raises(PyZigBeeDenied, self.drv.open)

    def test_already_close(self):
        self.drv.open()
        self.drv.close()
        assert_raises(PyZigBeeDenied, self.drv.close)

    def test_write_read(self):
        self.drv.open()
        self.drv.write("my data")
        assert_equal("my data", self.drv.read())

        self.drv.write("another data")
        assert_equal("another data", self.drv.read())
