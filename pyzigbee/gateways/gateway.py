#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2015 Legrand France
# All rights reserved

from pyzigbee.core.exceptions import PyZigBeeBadArgument
from pyzigbee.drivers.basedriver import BaseDriver
from pyzigbee.protocols.baseprotocol import BaseProtocol

class Gateway(object):
    """Gateway base class to be inherited from when implementing a real GW
    """

    def __init__(self, driver, protocol, description=""):
        self.set_driver(driver)
        self.set_protocol(protocol)
        self.description = description

    def set_driver(self, driver):

        if isinstance(driver, BaseDriver):
            self.driver = driver
        else:
            raise PyZigBeeBadArgument("%s is not a subclass of BaseDriver" % driver)

    def set_protocol(self, protocol):

        if isinstance(protocol, BaseProtocol):
            self.protocol = protocol
        else:
            raise PyZigBeeBadArgument("%s is not a subclass of BaseProtocol" % protocol)

    def get_description(self):
        return self.description

    def open(self):
        self.driver.open()

    def close(self):
        self.driver.close()

    def scan(self):
        """Scan the network and return a list of ZigBee IDs"""

        self.driver.write(self.protocol.encode_scan())
        data = self.driver.read()
        return self.protocol.decode_scan(data)
