#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2015 Legrand France
# All rights reserved

from pyzigbee.core.exceptions import PyZigBeeBadArgument
from pyzigbee.core.exceptions import PyZigBeeBadFormat
from pyzigbee.protocols.openwebnet import OWNProtocol
from pyzigbee.drivers.serialdriver import SerialDriver
from pyzigbee.gateways.gateway import Gateway
from pyzigbee.conf.factory import ConfReaderFactory

SUPPORTED_GW = {
    "088328": {
        "description": "088328 USB/Zigbee dongle",
        "protocol": {
            "class": OWNProtocol,
        },
        "driver": {
            "class": SerialDriver,
            "args": {
                "port": "/dev/ttyUSB0",
                "baudrate": "19200",
            },
        },
    },
}


class GatewayFactory(object):
    """
    Gateway factory which creates GW instances from a product reference
    """

    def __init__(self, conf_filename=None):
        self.conf_reader = ConfReaderFactory.create_conf_reader(conf_filename)

    def _sanitize_ref(self, ref):
        return ref.replace(" ", "")

    def create_gateway(self, ref):
        ref = self._sanitize_ref(ref)
        if ref in SUPPORTED_GW.keys():
            try:
                default_args = SUPPORTED_GW[ref]['driver']['args']
                args = self.conf_reader.override_args_with_conf(ref, default_args)
                driver = SUPPORTED_GW[ref]['driver']['class'](**args)
                protocol = SUPPORTED_GW[ref]['protocol']['class']()
                description = SUPPORTED_GW[ref]['description']
                return Gateway(driver, protocol, description)
            except KeyError as error:
                raise PyZigBeeBadFormat("Entry for %s is malformed (%s)" % (ref, error))
        else:
            raise PyZigBeeBadArgument("%s is not supported" % ref)

    @classmethod
    def get_supported_refs(cls):
        supported = {}
        for gw_k, gw_v in SUPPORTED_GW.items():
            supported[gw_k] = gw_v['description']
        return supported
