#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2015 Legrand France
# All rights reserved

import serial
import logging
import re

from pyzigbee.core.exceptions import PyZigBeeFailed, PyZigBeeTimedOut
from pyzigbee.drivers.basedriver import BaseDriver

class SerialDriver(BaseDriver):
    """Serial driver to communicate with underlying hardware

    keyword args are:
    - port: the serial port such as /dev/tty3 or COM3
    - baudrate: the serial line speed
    - parity: the serial line parity
    """

    def __init__(self, **kwargs):

        super(SerialDriver, self).__init__(kwargs=kwargs)
        self.port = self._get_or_default(kwargs, 'port', '/dev/ttyUSB0')
        self.baudrate = self._get_or_default(kwargs, 'baudrate', 115200)
        self.parity = self._get_or_default(kwargs, 'parity', 'N')
        self.dev = None
        self.logger = logging.getLogger(__name__)

    def _get_or_default(self, params, key, default=None):

        return params[key] if key in params.keys() else default

    def on_open(self):

        try:
            self.logger.debug("opening serial port %s...", self.port)
            self.dev = serial.Serial(port=self.port, baudrate=self.baudrate, parity=self.parity,
                                     timeout=3)
            self.logger.debug("serial port %s open", self.port)
        except OSError as error:
            self.logger.error('error when opening serial port %s (%s)', self.port, error)
            raise PyZigBeeFailed(msg="Failed to open serial port %s" % self.port)

    def on_close(self):

        self.dev = None

    def on_write(self, data):

        try:
            self.logger.debug("write data: %s", data)
            self.dev.write(data)
        except serial.SerialTimeoutException:
            raise PyZigBeeTimedOut("Timeout when writing to device")

    def on_read(self, to_read=None, stop_on="None"):

        data = ""
        if to_read is not None:
            data = self.dev.read(size=to_read)
        else:
            if stop_on is not None:
                stop_pattern = re.escape(stop_on)
                #self.logger.debug("next read will stop when receiving: %s", stop_on)
                endof = False
                while not endof:
                    byte = self.dev.read(size=1)
                    data += byte
                    #self.logger.debug("received byte: %s", byte)
                    if re.match(".*%s" % stop_pattern, data):
                        endof = True
            else:
                data = self.dev.read()

        self.logger.debug("read data: %s", data)
        return data

    def get_info(self):

        return { "description": "Serial driver",
                 "port": self.port,
                 "baudrate": self.baudrate,
                 "parity": self.parity,
               }
