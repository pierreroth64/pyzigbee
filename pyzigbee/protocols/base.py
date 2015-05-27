#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2015 Legrand France
# All rights reserved


class BaseProtocol(object):
    """Base protocol inherited by all the protocols
    """

    def __init__(self):
        pass

    def encode_scan(self):
        """Return an encoded frame to be sent to driver for scanning the Zigbee network"""

        return ""

    def decode_scan(self, data):
        """Return a list of Zigbee IDs retrieved from the received data"""

        return []
