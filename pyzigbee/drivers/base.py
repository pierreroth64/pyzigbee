#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2015 Legrand France
# All rights reserved

from pyzigbee.core.exceptions import PyZigBeeDenied

class BaseDriver(object):
    """Base driver inherited by all the drivers
    """

    def __init__(self, **kwargs):

        self.is_open = False

    def on_open(self):
        raise PyZigBeeOperationNotSupported("BaseDriver cannot be used directly: inherit from it")

    def on_close(self):
        raise PyZigBeeOperationNotSupported("BaseDriver cannot be used directly: inherit from it")

    def on_write(self, data):
        raise PyZigBeeOperationNotSupported("BaseDriver cannot be used directly: inherit from it")

    def on_read(self, to_read):
        raise PyZigBeeOperationNotSupported("BaseDriver cannot be used directly: inherit from it")

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

    def read(self, to_read=10):

        if not self.is_open:
            raise PyZigBeeDenied("Driver is closed")

        return self.on_read(to_read)
