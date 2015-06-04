#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2015 Legrand France
# All rights reserved

from pyzigbee.core.exceptions import PyZigBeeOperationNotSupported

class BaseProtocol(object):
    """Base protocol inherited by all the protocols"""

    def __init__(self):
        pass

    def handle_error(self, expected, received):
        """Handler called on error when expected data differs from received one"""
        raise PyZigBeeOperationNotSupported("handle_error: This method must be implemented by your protocol")

    def check_answer(self, answer):
        """Handler called to check answer"""
        raise PyZigBeeOperationNotSupported("check_answer: This method must be implemented by your protocol")

    def get_info(self):
        raise PyZigBeeOperationNotSupported("get_info: This method must be implemented by your protocol")

    def get_end_of_frame_sep(self):
        raise PyZigBeeOperationNotSupported("get_end_of_frame_sep: This method must be implemented by your protocol")

    def encode_get_dev_number(self, delay=5):
        raise PyZigBeeOperationNotSupported("encode_get_dev_number: This method must be implemented by your protocol")

    def decode_dev_number(self, data):
        raise PyZigBeeOperationNotSupported("decode_dev_number: This method must be implemented by your protocol")

    def encode_get_dev_id(self, dev_index):
        raise PyZigBeeOperationNotSupported("encode_get_dev_id: This method must be implemented by your protocol")

    def decode_dev_id(self, data):
        raise PyZigBeeOperationNotSupported("decode_dev_id: This method must be implemented by your protocol")

    def encode_get_firmware_version(self, zibgee_id=None):
        raise PyZigBeeOperationNotSupported("encode_get_firmware_version: This method must be implemented by your protocol")

    def encode_get_hardware_version(self, zibgee_id=None):
        raise PyZigBeeOperationNotSupported("encode_get_hardware_version: This method must be implemented by your protocol")

    def decode_firmware_version(self, data, zigbee_id=None):
        raise PyZigBeeOperationNotSupported("decode_firmware_version: This method must be implemented by your protocol")

    def decode_hardware_version(self, data, zigbee_id=None):
        raise PyZigBeeOperationNotSupported("decode_hardware_version: This method must be implemented by your protocol")
