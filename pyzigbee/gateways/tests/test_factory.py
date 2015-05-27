#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2015 Legrand France
# All rights reserved
from nose.tools import assert_raises, assert_true

from pyzigbee.core.exceptions import PyZigBeeBadArgument
from pyzigbee.gateways.factory import GatewayFactory
from pyzigbee.drivers.serial import SerialDriver
from pyzigbee.protocols.openwebnet import OWNProtocol

class TestFactory:

    def test_create(self):
        gateway = GatewayFactory.create_gateway("088328")
        assert_true(isinstance(gateway.driver, SerialDriver))
        assert_true(isinstance(gateway.protocol, OWNProtocol))

    def test_unsupported(self):
        assert_raises(PyZigBeeBadArgument, GatewayFactory.create_gateway, "0000000")
