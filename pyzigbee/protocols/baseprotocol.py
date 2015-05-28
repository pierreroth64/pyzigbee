#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2015 Legrand France
# All rights reserved

from pyzigbee.core.exceptions import PyZigBeeOperationNotSupported

class BaseProtocol(object):
    """Base protocol inherited by all the protocols
    """

    def __init__(self):
        pass

    def encode_scan(self):
        """Return an encoded frame to be sent to driver for scanning the Zigbee network"""

        raise PyZigBeeOperationNotSupported("encode_scan: This method must be implemented by your protocol")

    def decode_scan(self, data):
        """Return a list of Zigbee IDs retrieved from the received data"""

        raise PyZigBeeOperationNotSupported("decode_scan: This method must be implemented by your protocol")

    def get_info(self):

        raise PyZigBeeOperationNotSupported("get_info: This method must be implemented by your protocol")
