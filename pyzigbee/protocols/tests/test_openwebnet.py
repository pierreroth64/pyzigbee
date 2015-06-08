#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2015 Legrand France
# All rights reserved

from nose.tools import assert_raises, assert_true, assert_false, assert_equal
from pyzigbee.protocols.openwebnet import OWNProtocol, OWN_ACK
from pyzigbee.core.exceptions import PyZigBeeDenied


class TestOWNProtocol:

    def setup(self):
        self.protocol = OWNProtocol()

    def tearDown(self):
        self.protocol = None

    def test_decode_dev_number(self):
        assert_equal("4", self.protocol.decode_dev_number("*#13**67*4##"))
        assert_equal("100", self.protocol.decode_dev_number("*#13**67*100##"))

    def test_decode_dev_number(self):
        decoded_id = self.protocol.decode_dev_id("*#13*709138701#9*66#0*256##")
        assert_equal("709138701", decoded_id)

    def test_decode_firmware_version(self):
        decoded_version = self.protocol.decode_firmware_version("*#13**16*1*2*3##")
        assert_equal("1.2.3", decoded_version)

        decoded_version = self.protocol.decode_firmware_version(data="*#13*123456*16*2*0*1##",
                                                                zigbee_id="123456")
        assert_equal("2.0.1", decoded_version)

    def test_encode_get_firmware_version(self):
        encoded_sequence = self.protocol.encode_get_firmware_version()[0]
        assert_equal({"tx": "*#13**16##"}, encoded_sequence)

        encoded_sequence = self.protocol.encode_get_firmware_version(zigbee_id="7123456")[0]
        assert_equal({"tx": "*#13*7123456*16##"}, encoded_sequence)

    def test_encode_get_hardware_version(self):
        encoded_sequence = self.protocol.encode_get_hardware_version()[0]
        assert_equal({"tx": "*#13**17##"}, encoded_sequence)

        encoded_sequence = self.protocol.encode_get_hardware_version(zigbee_id="7123456")[0]
        assert_equal({"tx": "*#13*7123456*17##"}, encoded_sequence)

    def test_decode_binding_id(self):
        assert_equal("412300024", self.protocol.decode_binding_id(data="*25*35*412300024#9##"))

    def test_encode_binding_request(self):
        encoded_sequence = self.protocol.encode_binding_request(zigbee_id="12335566")
        assert_equal([{"tx": "*25*33*12335566#9##"},
                      {"rx": OWN_ACK},
                      {"rx": "*25*36*12335566#9##"}], encoded_sequence)

    def test_encode_unbinding_request(self):
        encoded_sequence = self.protocol.encode_unbinding_request(zigbee_id="778123")
        assert_equal([{"tx": "*25*34*778123#9##"},
                      {"rx": OWN_ACK},
                      {"rx": "*25*36*778123#9##"}], encoded_sequence)
