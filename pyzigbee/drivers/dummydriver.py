#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2015 Legrand France
# All rights reserved

from pyzigbee.core.exceptions import PyZigBeeDenied
from pyzigbee.drivers.basedriver import BaseDriver

class DummyDriver(BaseDriver):
    """
    Dummy driver mainly used for testing

    When reading data, this driver returns the data written at previous write
    """

    def __init__(self, **kwargs):
        super(DummyDriver, self).__init__(**kwargs)
        self.data = None

    def get_info(self):
        return {"description": "Dummy driver (reading from it what you previously wrote to it)"}

    def on_open(self):
        pass

    def on_close(self):
        pass

    def on_write(self, data):
        self.data = data

    def on_read(self, to_read=None, stop_on=None):
        return self.data

    def set_blocking(self):
        pass

    def set_unblocking(self, timeout=0):
        pass
