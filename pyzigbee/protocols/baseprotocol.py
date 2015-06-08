#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2015 Legrand France
# All rights reserved

from pyzigbee.core.exceptions import PyZigBeeNotSupported


class BaseProtocol(object):
    """
    Base protocol inherited by all the protocols
    """

    def __init__(self):
        pass

    def handle_error(self, expected, received):
        """
        Handler called on error when expected data differs from received one
        """
        raise PyZigBeeNotSupported("handle_error: This method must be"
                                   " implemented by your protocol")

    def check_answer(self, answer):
        """
        Handler called to check answer
        """
        raise PyZigBeeNotSupported("check_answer: This method must be"
                                   " implemented by your protocol")

    def get_info(self):
        raise PyZigBeeNotSupported("get_info: This method must be"
                                   " implemented by your protocol")

    def get_end_of_frame_sep(self):
        raise PyZigBeeNotSupported("get_end_of_frame_sep: This method must be"
                                   " implemented by your protocol")

    def encode_get_dev_number(self, delay=5):
        raise PyZigBeeNotSupported("encode_get_dev_number: This method must be"
                                   " implemented by your protocol")

    def decode_dev_number(self, data):
        raise PyZigBeeNotSupported("decode_dev_number: This method must be"
                                   " implemented by your protocol")

    def encode_get_dev_id(self, dev_index):
        raise PyZigBeeNotSupported("encode_get_dev_id: This method must be"
                                   " implemented by your protocol")

    def decode_dev_id(self, data):
        raise PyZigBeeNotSupported("decode_dev_id: This method must be"
                                   " implemented by your protocol")

    def encode_get_firmware_version(self, zibgee_id=None):
        raise PyZigBeeNotSupported("encode_get_firmware_version: This method must be"
                                   " implemented by your protocol")

    def encode_get_hardware_version(self, zibgee_id=None):
        raise PyZigBeeNotSupported("encode_get_hardware_version: This method must be"
                                   " implemented by your protocol")

    def decode_firmware_version(self, data, zigbee_id=None):
        raise PyZigBeeNotSupported("decode_firmware_version: This method must be"
                                   " implemented by your protocol")

    def decode_hardware_version(self, data, zigbee_id=None):
        raise PyZigBeeNotSupported("decode_hardware_version: This method must be"
                                   " implemented by your protocol")

    def decode_binding_id(self, data):
        raise PyZigBeeNotSupported("decode_binding_id: This method must be"
                                   " implemented by your protocol")

    def encode_binding_request(self, zigbee_id):
        raise PyZigBeeNotSupported("encode_binding_request: This method must be"
                                   " implemented by your protocol")

    def encode_unbinding_request(self, zigbee_id):
        raise PyZigBeeNotSupported("encode_unbinding_request: This method must be"
                                   " implemented by your protocol")
