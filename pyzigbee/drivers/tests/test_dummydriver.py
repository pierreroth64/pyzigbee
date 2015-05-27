#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2015 Legrand France
# All rights reserved
from nose.tools import assert_raises

from pyzigbee.drivers.dummy import DummyDriver
from pyzigbee.core.exceptions import PyZigBeeDenied

class TestDummyDriver:

    def setup(self):
        self.drv =  DummyDriver()

    def tearDown(self):
        self.drv = None

    def test_initially_open(self):
        assert False == self.drv.is_open

    def test_open(self):
        self.drv.open()
        assert True == self.drv.is_open

    def test_close(self):
        self.drv.open()
        self.drv.close()
        assert False == self.drv.is_open

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
        assert "my data" == self.drv.read()

        self.drv.write("another data")
        assert "another data" == self.drv.read()
