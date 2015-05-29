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
        self.gw = Gateway(driver, protocol)

    def test_set_protocol_robustness(self):

        assert_raises(PyZigBeeBadArgument, self.gw.set_protocol, "invalid object")

    def test_set_driver_robustness(self):

        assert_raises(PyZigBeeBadArgument, self.gw.set_driver, "invalid object")
