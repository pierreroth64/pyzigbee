#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2015 Legrand France
# All rights reserved
from nose.tools import assert_raises, assert_true, assert_equal, assert_not_equal

from pyzigbee.core.exceptions import PyZigBeeDenied, PyZigBeeBadArgument
from pyzigbee.gateways.gateway import Gateway
from pyzigbee.drivers.dummydriver import DummyDriver
from pyzigbee.protocols.dummy import DummyProtocol
from pyzigbee.protocols.openwebnet import OWNProtocol

class TestGateway:

    def setup(self):
        driver = DummyDriver()
        protocol = DummyProtocol()
        self.gw = Gateway(driver, protocol, "my gateway")

    def tearDown(self):
        self.gw = None

    def test_set_protocol_robustness(self):
        assert_raises(PyZigBeeBadArgument, self.gw.set_protocol, "invalid object")

    def test_set_driver_robustness(self):
        assert_raises(PyZigBeeBadArgument, self.gw.set_driver, "invalid object")

    def test_get_info(self):
        assert_equal("my gateway", self.gw.get_info()["description"])
        assert_equal({'description': 'Dummy driver (reading from it what you previously wrote to it)'},
                     self.gw.get_info()["driver"])
        assert_equal({'description': 'Dummy protocol'},
                     self.gw.get_info()["protocol"])

    def test_get_firmware_version(self):
        def my_get_answer(*args, **kwargs):
            return "nothing"
        self.gw._get_answer = my_get_answer
        assert_equal("1.0.0", self.gw.get_firmware_version())

    def test_get_hardware_version(self):
        def my_get_answer(*args, **kwargs):
            return "nothing"
        self.gw._get_answer = my_get_answer
        assert_equal("1.2.0", self.gw.get_hardware_version())
