#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2015 Legrand France
# All rights reserved

from pyzigbee.core.exceptions import PyZigBeeBadArgument
from pyzigbee.protocols.openwebnet import OWNProtocol
from pyzigbee.drivers.serial import SerialDriver
from pyzigbee.gateways.gateway import Gateway

SUPPORTED_GW = {
    '088328': {
        'protocol': {
            'class': OWNProtocol,
        },
        'driver': {
            'class': SerialDriver,
            'args': {
                'port': '/dev/ttyUSB0',
                'baudrate': 115200,
            },
        },
    },
}

class GatewayFactory:
    """Gateway factory which creates GW instances from a product reference"""

    @staticmethod
    def create_gateway(ref):

        if SUPPORTED_GW.has_key(ref):
            driver = SUPPORTED_GW[ref]['driver']['class'](**SUPPORTED_GW[ref]['driver']['args'])
            protocol = SUPPORTED_GW[ref]['protocol']['class']()
            return Gateway(driver, protocol)
        else:
            raise PyZigBeeBadArgument("%s is not supported" % ref)

