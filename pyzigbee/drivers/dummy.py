#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2015 Legrand France
# All rights reserved

from pyzigbee.core.exceptions import PyZigBeeDenied

class DummyDriver:
    """Dummy driver mainly used for testing

    When reading data, this driver returns the data written at previous write
    """

    def __init__(self, **kwargs):

        self.is_open = False
        self.data = None

    def open(self):

        if not self.is_open:
            self.is_open = True
        else:
            raise PyZigBeeDenied("Driver is already open")

    def close(self):

        if self.is_open:
            self.is_open = False
        else:
            raise PyZigBeeDenied("Driver is already closed")


    def write(self, data):

        if not self.is_open:
            raise PyZigBeeDenied("Driver is closed")

        self.data =  data

    def read(self, to_read=10):

        if not self.is_open:
            raise PyZigBeeDenied("Driver is closed")

        return self.data
