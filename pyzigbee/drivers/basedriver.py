#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2015 Legrand France
# All rights reserved

from pyzigbee.core.exceptions import PyZigBeeDenied
from pyzigbee.core.exceptions import PyZigBeeFailed
from pyzigbee.core.exceptions import PyZigBeeBadFormat
from pyzigbee.core.exceptions import PyZigBeeNotSupported


class BaseDriver(object):
    """
    Base driver inherited by all the drivers
    """

    def __init__(self, **kwargs):
        self.is_open = False

    def on_open(self):
        raise PyZigBeeNotSupported("on_open: This method must be"
                                   " implemented by your driver")

    def on_close(self):
        raise PyZigBeeNotSupported("on_close: This method must be"
                                   " implemented by your driver")

    def on_write(self, data):
        data = data
        raise PyZigBeeNotSupported("on_write: This method must be"
                                   " implemented by your driver")

    def on_read(self, to_read, stop_on):
        to_read = to_read
        stop_on = stop_on
        raise PyZigBeeNotSupported("on_read: This method must be"
                                   " implemented by your driver")

    def set_blocking(self):
        raise PyZigBeeNotSupported("set_blocking: This method must be"
                                   " implemented by your driver")

    def set_unblocking(self, timeout=0):
        timeout = timeout
        raise PyZigBeeNotSupported("set_unblocking: This method must be"
                                   " implemented by your driver")

    def open(self):
        if not self.is_open:
            self.is_open = True
            self.on_open()
        else:
            raise PyZigBeeDenied("Driver is already open")

    def close(self):
        if self.is_open:
            self.is_open = False
            self.on_close()
        else:
            raise PyZigBeeDenied("Driver is already closed")

    def write(self, data):
        if not self.is_open:
            raise PyZigBeeDenied("Driver is closed")
        try:
            self.on_write(data)
        except Exception as error:
            raise PyZigBeeFailed("failed to write data to driver (%s)"
                                 % error)

    def read(self, to_read=None, stop_on=None):
        if not self.is_open:
            raise PyZigBeeDenied("Driver is closed")
        try:
            return self.on_read(to_read=to_read, stop_on=stop_on)
        except Exception as error:
            raise PyZigBeeFailed("failed to read data from driver (%s)"
                                 % error)

    def get_info(self):
        raise PyZigBeeNotSupported("get_info: This method must be"
                                   " implemented by your driver")

    def set_blocking_mode(self):
        if not self.is_open:
            raise PyZigBeeDenied("Driver is closed")

        self.set_blocking()

    def set_unblocking_mode(self, timeout=0):
        if not self.is_open:
            raise PyZigBeeDenied("Driver is closed")

        try:
            timeout = int(timeout)
        except ValueError as error:
            raise PyZigBeeBadFormat("timeout passed to"
                                    "set_unblocking_mode must be an integer (%s)"
                                    % error)

        self.set_unblocking(timeout=timeout)
