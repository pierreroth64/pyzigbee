#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2015 Legrand France
# All rights reserved

import time
import logging

from pyzigbee.core.exceptions import *
from pyzigbee.drivers.basedriver import BaseDriver
from pyzigbee.protocols.baseprotocol import BaseProtocol

class Gateway(object):
    """Gateway base class to be inherited from when implementing a real GW
    """

    def __init__(self, driver, protocol, description=""):

        self.set_driver(driver)
        self.set_protocol(protocol)
        self.description = description
        self.logger = logging.getLogger(__name__)

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

    def get_info(self):

        info = {}
        info['description'] = self.description
        info['driver'] = self.driver.get_info()
        info['protocol'] = self.protocol.get_info()
        return info

    def get_firmware_version(self, zigbee_id=None):

        sequence = self.protocol.encode_get_firmware_version(zigbee_id)
        answer = self._get_answer(sequence)
        return self.protocol.decode_firmware_version(answer, zigbee_id)

    def get_hardware_version(self, zigbee_id=None):

        sequence = self.protocol.encode_get_hardware_version(zigbee_id)
        answer = self._get_answer(sequence)
        return self.protocol.decode_hardware_version(answer, zigbee_id)

    def open(self):

        self.driver.open()
        return self

    def close(self):

        self.driver.close()
        return self

    def _get_answer(self, sequence):

        answer =  None
        for seq in sequence:
            if "tx" in seq.keys():
                self.driver.write(seq["tx"])
            if "rx" in seq.keys():
                data = self.driver.read(to_read=len(seq["rx"]))
                if data != seq["rx"]:
                    self.protocol.handle_error(expected=seq["rx"], received=data)
            if "delay" in seq.keys():
                delay = int(seq["delay"])
                self.logger.debug("sleeping for %d seconds...", delay)
                time.sleep(delay)
            if "answer" in seq.keys():
                answer = self.driver.read(stop_on=self.protocol.get_end_of_frame_sep())

        if answer is not None:
            return answer
        else:
            raise PyZigBeeFailed("Device did not reply")

    def scan(self):
        """Scan the network and return a list of ZigBee IDs"""

        self.logger.debug("getting number of devices...")
        sequence = self.protocol.encode_get_dev_number()
        answer = self._get_answer(sequence)
        dev_nb = self.protocol.decode_dev_number(answer)
        self.logger.debug("%d device(s) on the network", dev_nb)

        dev_ids = []
        # we can now loop over the devices
        for i in range(0, dev_nb):
            self.logger.debug("getting device ID at index %d...", i)
            sequence = self.protocol.encode_get_dev_id(dev_index=i)
            answer = self._get_answer(sequence)
            dev_id = self.protocol.decode_dev_id(answer)
            self.logger.debug("device ID at index %d: %s", i, dev_id)
            dev_ids.append(dev_id)

        return dev_ids

