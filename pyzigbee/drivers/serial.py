#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2015 Legrand France
# All rights reserved

import serial
from pyzigbee.drivers.base import BaseDriver

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
        self.serial = None

    def _get_or_default(self, params, key, default=None):

        return params[key] if key in params.keys() else default

    def on_open(self):

        self.serial = serial.Serial(port=self.port, baudrate=self.baudrate,
                                    timeout=2, writeTimeout=2)
    def on_close(self):

        self.serial = None

    def on_write(self, data):

        try:
            self.serial.write(data)
        except serial.SerialTimeoutException:
            raise PyZigBeeTimedOut("Timeout when writing to device")

    def on_read(self, to_read=10):

        read_bytes = self.serial.read(size=to_read)
        return read_bytes
