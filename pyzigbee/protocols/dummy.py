#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2015 Legrand France
# All rights reserved

from pyzigbee.protocols.baseprotocol import BaseProtocol

class DummyProtocol(BaseProtocol):
    """Dummy protocol mainly used for testing"""

    def __init__(self):
        pass

    def handle_error(expected, received):
        """Handler called on error when expected data differs from received one"""
        pass

    def get_info(self):
        return { "description": "Dummy protocol" }

    def get_end_of_frame_sep(self):
        return "|"

    def encode_get_dev_number(self, delay=5):
        return []

    def decode_dev_number(self, data):
        return "12"

    def encode_get_dev_id(self, dev_index):
        return []

    def decode_dev_id(self, data):
        return "45600021"

    def encode_get_firmware_version(self, zigbee_id=None):
        return []

    def encode_get_hardware_version(self, zigbee_id=None):
        return []

    def decode_firmware_version(self, data, zigbee_id=None):
        return "1.0.0"

    def decode_hardware_version(self, data, zigbee_id=None):
        return "1.0.0"
