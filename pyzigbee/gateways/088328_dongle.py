#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2015 Legrand France
# All rights reserved

from pyzigbee.gateways.gateway import Gateway

class Gw088328(Gateway):
    """088328 dongle is an USB to Zigbee gateway
    """

    def __init__(self, driver, protocol):
        pass

    def encode_scan(self):
        """Return an OWN frame to be sent to driver for scanning the Zigbee network"""
        return "##30#12*35#"

    def decode_scan(self, data):
        """Return a list of Zigbee IDs retrieved from the network"""

        return [1234, 1521, 1230]
