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

READ_TIMEOUT = 3
WRITE_TIMEOUT = 5


class SerialDriver(BaseDriver):
    """
    Serial driver to communicate with underlying hardware

    keyword args are:
    - port: the serial port such as /dev/tty3 or COM3
    - baudrate: the serial line speed
    - parity: the serial line parity
    """

    def __init__(self, **kwargs):
        super(SerialDriver, self).__init__(kwargs=kwargs)
        self.port = self._get_or_default(kwargs, 'port', '/dev/ttyUSB0')
        self.baudrate = int(self._get_or_default(kwargs, 'baudrate', 115200))
        self.parity = self._get_or_default(kwargs, 'parity', 'N')
        self.dev = None
        self.logger = logging.getLogger(__name__)

    def _get_or_default(self, params, key, default=None):
        return params[key] if key in params.keys() else default

    def _is_blocking_mode(self):
        return True if self.dev.timeout is None else False

    def _is_blocking_mode_str(self):
        return "blocking mode" if self._is_blocking_mode() else "non-blocking mode"

    def on_open(self):
        try:
            self.logger.debug("opening serial port %s...", self.port)
            self.dev = serial.Serial(port=self.port,
                                     baudrate=self.baudrate,
                                     parity=self.parity,
                                     timeout=READ_TIMEOUT,
                                     writeTimeout=WRITE_TIMEOUT)
            self.logger.debug("serial port %s open (%s)",
                              self.port, self._is_blocking_mode_str())
        except (OSError, serial.serialutil.SerialException) as error:
            self.logger.error('error when opening serial port %s (%s)',
                              self.port, error)
            raise PyZigBeeFailed(msg="Failed to open serial port %s (%s)"
                                 % (self.port, error))

    def on_close(self):
        self.logger.debug("closed serial port %s.", self.port)
        self.dev = None

    def on_write(self, data):
        try:
            self.logger.debug("write data: %s", data)
            self.dev.write(data)
        except serial.SerialTimeoutException:
            raise PyZigBeeTimedOut("Timeout when writing to device")

    def on_read(self, to_read=None, stop_on=None):
        data = ""
        if to_read is not None and to_read != "":
            data = self.dev.read(size=int(to_read))
        else:
            if stop_on is not None:
                stop_pattern = re.escape(stop_on)
                self.logger.debug("next read will stop when receiving: %s", stop_on)
                endof = False
                while not endof:
                    byte = self.dev.read(size=1)
                    data += byte
                    # self.logger.debug("received byte: %s", byte)
                    if re.match(".*%s" % stop_pattern, data):
                        endof = True
            else:
                data = self.dev.read()

        self.logger.debug("read data: %s", data)
        return data

    def get_info(self):
        return {"description": "Serial driver",
                "port": self.port,
                "baudrate": self.baudrate,
                "parity": self.parity}

    def set_blocking(self):
        if self.dev.timeout is not None:
            self.dev.timeout = None
            self.logger.debug("serial port %s set to blocking mode", self.port)
        else:
            self.logger.debug("serial port %s already set to blocking mode", self.port)

    def set_unblocking(self, timeout=READ_TIMEOUT):
        try:
            if self.dev.timeout is None:
                self.dev.timeout = timeout
                self.logger.debug("serial port %s set to non-blocking mode (timeout: %s)",
                                  self.port, self.dev.timeout)
            else:
                self.logger.debug("serial port %s already set to non-blocking mode",
                                  self.port)
        except ValueError as error:
            raise PyZigBeeBadFormat("timeout must be an integer")
