#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2015 Legrand France
# All rights reserved
from nose.tools import assert_raises, assert_true, assert_false, assert_equal
from pyzigbee.drivers.dummydriver import DummyDriver
from pyzigbee.core.exceptions import PyZigBeeDenied, PyZigBeeBadFormat


class TestDummyDriver:

    def setup(self):
        self.drv = DummyDriver()

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

    def test_set_blocking(self):
        self.drv.open()
        self.drv.set_blocking_mode()

    def test_set_blocking_but_not_open(self):
        assert_raises(PyZigBeeDenied, self.drv.set_blocking_mode)

    def test_set_unblocking(self):
        self.drv.open()
        self.drv.set_unblocking_mode(timeout=3)

    def test_set_unblocking_wrong_format(self):
        self.drv.open()
        assert_raises(PyZigBeeBadFormat,
                      self.drv.set_unblocking_mode,
                      timeout="bad format")

    def test_set_unblocking_but_not_open(self):
        assert_raises(PyZigBeeDenied,
                      self.drv.set_unblocking_mode,
                      timeout=3)
