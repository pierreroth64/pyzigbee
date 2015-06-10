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
        expected = expected
        received = received
        raise PyZigBeeNotSupported("handle_error: This method must be"
                                   " implemented by your protocol")

    def check_answer(self, answer):
        """
        Handler called to check answer
        """
        answer = answer
        raise PyZigBeeNotSupported("check_answer: This method must be"
                                   " implemented by your protocol")

    def get_info(self):
        raise PyZigBeeNotSupported("get_info: This method must be"
                                   " implemented by your protocol")

    def get_end_of_frame_sep(self):
        raise PyZigBeeNotSupported("get_end_of_frame_sep: This method must be"
                                   " implemented by your protocol")

    def encode_get_dev_number(self, delay=5):
        delay = delay
        raise PyZigBeeNotSupported("encode_get_dev_number: This method must be"
                                   " implemented by your protocol")

    def decode_dev_number(self, data):
        data = data
        raise PyZigBeeNotSupported("decode_dev_number: This method must be"
                                   " implemented by your protocol")

    def encode_get_dev_id(self, dev_index):
        dev_index = dev_index
        raise PyZigBeeNotSupported("encode_get_dev_id: This method must be"
                                   " implemented by your protocol")

    def decode_dev_id(self, data):
        data = data
        raise PyZigBeeNotSupported("decode_dev_id: This method must be"
                                   " implemented by your protocol")

    def encode_get_firmware_version(self, zigbee_id=None):
        zigbee_id = zigbee_id
        raise PyZigBeeNotSupported("encode_get_firmware_version: This method must be"
                                   " implemented by your protocol")

    def encode_get_hardware_version(self, zigbee_id=None):
        zigbee_id = zigbee_id
        raise PyZigBeeNotSupported("encode_get_hardware_version: This method must be"
                                   " implemented by your protocol")

    def decode_firmware_version(self, data, zigbee_id=None):
        data = data
        zigbee_id = zigbee_id
        raise PyZigBeeNotSupported("decode_firmware_version: This method must be"
                                   " implemented by your protocol")

    def decode_hardware_version(self, data, zigbee_id=None):
        data = data
        zigbee_id = zigbee_id
        raise PyZigBeeNotSupported("decode_hardware_version: This method must be"
                                   " implemented by your protocol")

    def decode_binding_id(self, data):
        data = data
        raise PyZigBeeNotSupported("decode_binding_id: This method must be"
                                   " implemented by your protocol")

    def encode_binding_request(self, zigbee_id):
        zigbee_id = zigbee_id
        raise PyZigBeeNotSupported("encode_binding_request: This method must be"
                                   " implemented by your protocol")

    def encode_unbinding_request(self, zigbee_id):
        zigbee_id = zigbee_id
        raise PyZigBeeNotSupported("encode_unbinding_request: This method must be"
                                   " implemented by your protocol")
