#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2015 Legrand France
# All rights reserved

import os
import platform

class PlatformService(object):

    def __init__(self):
        pass

    def __repr__(self):
        return "%s (%s)" % (platform.system(), platform.release())

    def clear(self):
        raise Exception("clear must be implemented by your service")

class LinuxService(PlatformService):

    def __init__(self):
        super(LinuxService, self).__init__()

    def clear(self):
        os.system('clear')

class WindowsService(PlatformService):

    def __init__(self):
        super(WindowsService, self).__init__()

    def clear(self):
        os.system('cls')


def get_platform_service():

    if platform.system() == 'Linux':
        return LinuxService()
    else:
        return WindowsService()
