#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2015 Legrand France
# All rights reserved

from nose.tools import assert_raises, assert_true, assert_false, assert_equal
from pyzigbee.protocols.baseprotocol import BaseProtocol
from pyzigbee.core.exceptions import PyZigBeeNotSupported


class TestBaseProtocol:

    def setup(self):
        self.protocol = BaseProtocol()

    def tearDown(self):
        self.protocol = None

    def test_check_answer(self):
        assert_raises(PyZigBeeNotSupported, self.protocol.check_answer, "")

    def test_get_info(self):
        assert_raises(PyZigBeeNotSupported, self.protocol.get_info)

    def test_get_end_of_frame_sep(self):
        assert_raises(PyZigBeeNotSupported, self.protocol.get_end_of_frame_sep)

    def test_encode_get_dev_number(self):
        assert_raises(PyZigBeeNotSupported, self.protocol.encode_get_dev_number)

    def test_decode_dev_number(self):
        assert_raises(PyZigBeeNotSupported, self.protocol.decode_dev_number, "")

    def test_encode_get_dev_id(self):
        assert_raises(PyZigBeeNotSupported, self.protocol.encode_get_dev_id, 2)

    def test_decode_dev_id(self):
        assert_raises(PyZigBeeNotSupported, self.protocol.decode_dev_id, "")

    def test_encode_get_firmware_version(self):
        assert_raises(PyZigBeeNotSupported, self.protocol.encode_get_firmware_version, 1)

    def test_encode_get_hardware_version(self):
        assert_raises(PyZigBeeNotSupported, self.protocol.encode_get_hardware_version, 1)

    def test_decode_firmware_version(self):
        assert_raises(PyZigBeeNotSupported, self.protocol.decode_firmware_version, "", 1)

    def test_decode_hardware_version(self):
        assert_raises(PyZigBeeNotSupported, self.protocol.decode_hardware_version, "", 1)

    def test_decode_binding_id(self):
        assert_raises(PyZigBeeNotSupported, self.protocol.decode_binding_id, "")

    def test_encode_binding_request(self):
        assert_raises(PyZigBeeNotSupported, self.protocol.encode_binding_request, 1)

    def test_encode_unbinding_request(self):
        assert_raises(PyZigBeeNotSupported, self.protocol.encode_unbinding_request, 1)

