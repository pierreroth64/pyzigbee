#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2015 Legrand France
# All rights reserved

from pyzigbee.protocols.base import BaseProtocol

class DummyProtocol(BaseProtocol):
    """Dummy protocol mainly used for testing
    """

    def __init__(self):
        pass

    def encode_scan(self):
        """Return an OWN frame to be sent to driver for scanning the Zigbee network"""
        return ""

    def decode_scan(self, data):
        """Return a list of Zigbee IDs retrieved from the network"""

        return []
