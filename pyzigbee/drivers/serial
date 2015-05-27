#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2015 Legrand France
# All rights reserved

import serial

class SerialDriver:
    """Serial driver to communicate with underlying hardware

    keyword args are:
    - port: the serial port such as /dev/tty3 or COM3
    - baudrate: the serial line speed
    """

    def __init__(self, **kwargs):

        self.port = self._get_or_default(kwargs, 'port', '/dev/ttymxc3')
        self.baudrate = self._get_or_default(kwargs, 'baudrate', 115200)
        self.parity = self._get_or_default(kwargs, 'parity', serial.PARITY_NONE)
        self.is_open = False
        self.serial = None

    def _get_or_default(self, params, key, default=None):

        return params['key'] if params.has_key('key') else default


    def open(self):

        if not self.is_open:
            self.serial = serial.Serial(port=self.port, baudrate=self.baudrate, parity=self.parity
                                        timeout=2, writeTimeout=2)
            self.is_open = True
        else:
            raise PyZigBeeDenied("Driver is already open")

    def close(self):

        if self.is_open:
            self.serial = None
            self.is_open = False
        else:
            raise PyZigBeeDenied("Driver is already closed")


    def write(self, data):

        if not self.is_open:
            raise PyZigBeeDenied("Driver is closed")

        try:
            self.serial.write(data)
        except serial.SerialTimeoutException:
            raise PyZigBeeTimedOut("Timeout when writing to device")

    def read(self, to_read=10):

        if not self.is_open:
            raise PyZigBeeDenied("Driver is closed")

        read_bytes = self.serial.read(size=to_read)
        return read_bytes
