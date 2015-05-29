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

    def get_info(self):

        return { "description": "Dummy protocol" }

    def get_end_of_frame_sep(self):

        return "|"

    def encode_get_dev_number(self):

        return []

    def decode_dev_number(self, data):

        return "12"

    def encode_get_dev_id(self, dev_index):

        return []

    def decode_dev_id(self, data):

        return "45600021"

    def encode_get_version(self):

        return []

    def decode_version(self, data):

        return "1.0.0"
