#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2015 Legrand France
# All rights reserved

from nose.tools import assert_raises, assert_true, assert_false, assert_equal

from pyzigbee.protocols.openwebnet import OWNProtocol
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

        assert_equal("709138701", self.protocol.decode_dev_id("*#13*709138701#9*66#0*256##"))

    def test_decode_version(self):

        assert_equal("1.2.3", self.protocol.decode_version("*#13**16*1*2*3##"))

