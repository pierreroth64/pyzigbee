#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2015 Legrand France
# All rights reserved

from pyzigbee.core.exceptions import PyZigBeeDenied

class BaseDriver(object):
    """Base driver inherited by all the drivers"""

    def __init__(self, **kwargs):

        self.is_open = False

    def on_open(self):

        raise PyZigBeeOperationNotSupported("on_open: This method must be implemented by your driver")

    def on_close(self):

        raise PyZigBeeOperationNotSupported("on_close: This method must be implemented by your driver")

    def on_write(self, data):

        raise PyZigBeeOperationNotSupported("on_write: This method must be implemented by your driver")

    def on_read(self, to_read, stop_on):

        raise PyZigBeeOperationNotSupported("on_read: This method must be implemented by your driver")

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

        self.on_write(data)

    def read(self, to_read=None, stop_on=None):

        if not self.is_open:
            raise PyZigBeeDenied("Driver is closed")

        return self.on_read(to_read=to_read, stop_on=stop_on)

    def get_info(self):

        raise PyZigBeeOperationNotSupported("get_info: This method must be implemented by your driver")

