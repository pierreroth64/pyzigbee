#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2015 Legrand France
# All rights reserved

import serial
import logging

from pyzigbee.core.exceptions import PyZigBeeFailed
from pyzigbee.drivers.basedriver import BaseDriver

class SerialDriver(BaseDriver):
    """Serial driver to communicate with underlying hardware

    keyword args are:
    - port: the serial port such as /dev/tty3 or COM3
    - baudrate: the serial line speed
    """

    def __init__(self, **kwargs):

        super(SerialDriver, self).__init__(kwargs=kwargs)
        self.port = self._get_or_default(kwargs, 'port', '/dev/ttymxc3')
        self.baudrate = self._get_or_default(kwargs, 'baudrate', 115200)
        self.dev = None
        self.logger = logging.getLogger(__name__)

    def _get_or_default(self, params, key, default=None):

        return params[key] if key in params.keys() else default

    def on_open(self):

        try:
            self.logger.debug("opening serial port %s...", self.port)
            self.dev = serial.Serial(port=self.port, baudrate=self.baudrate)
            self.logger.debug("serial port %s open", self.port)
        except OSError as error:
            self.logger.error('error when opening serial port %s (%s)', self.port, error)
            raise PyZigBeeFailed(msg="Failed to open serial port %s" % self.port)

    def on_close(self):

        self.dev = None

    def on_write(self, data):

        try:
            self.dev.write(data)
        except serial.SerialTimeoutException:
            raise PyZigBeeTimedOut("Timeout when writing to device")

    def on_read(self, to_read=10):

        read_bytes = self.dev.read(size=to_read)
        return read_bytes
