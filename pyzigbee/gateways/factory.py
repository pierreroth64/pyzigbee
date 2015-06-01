#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2015 Legrand France
# All rights reserved

from pyzigbee.core.exceptions import PyZigBeeBadArgument
from pyzigbee.protocols.openwebnet import OWNProtocol
from pyzigbee.drivers.serialdriver import SerialDriver
from pyzigbee.gateways.gateway import Gateway

SUPPORTED_GW = {
    '088328': {
        'description': "088328 USB/Zigbee dongle",
        'protocol': {
            'class': OWNProtocol,
        },
        'driver': {
            'class': SerialDriver,
            'args': {
                'port': '/dev/ttyUSB0',
                'baudrate': 19200,
            },
        },
    },
}

class GatewayFactory(object):
    """Gateway factory which creates GW instances from a product reference"""

    @classmethod
    def _sanitize_ref(cls, ref):
        return ref.replace(" ", "")

    @classmethod
    def create_gateway(cls, ref):

        ref = cls._sanitize_ref(ref)

        if ref in SUPPORTED_GW.keys():
            try:
                driver = SUPPORTED_GW[ref]['driver']['class'](**SUPPORTED_GW[ref]['driver']['args'])
                protocol = SUPPORTED_GW[ref]['protocol']['class']()
                description = SUPPORTED_GW[ref]['description']
                return Gateway(driver, protocol, description)
            except KeyError as error:
                raise PyZigBeeBadFormatError("Entry for %s is malformed (%s)" % (ref, error))
        else:
            raise PyZigBeeBadArgument("%s is not supported" % ref)


    @classmethod
    def get_supported_refs(cls):

        supported = {}
        for gw_k, gw_v in SUPPORTED_GW.items():
            supported[gw_k] = gw_v['description']
        return supported
