#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2015 Legrand France
# All rights reserved

import os
import platform


class PlatformService(object):
    """
    Abstract Platform service to be implemented by concrete services
    """

    def __init__(self):
        pass

    def __repr__(self):
        return "%s (%s)" % (platform.system(), platform.release())

    def clear(self):
        raise Exception("clear must be implemented by your service")


class LinuxService(PlatformService):
    """
    Linux services
    """

    def __init__(self):
        super(LinuxService, self).__init__()

    def clear(self):
        os.system('clear')


class WindowsService(PlatformService):
    """
    Windows services
    """

    def __init__(self):
        super(WindowsService, self).__init__()

    def clear(self):
        os.system('cls')


def create_platform_service():
    """
    Create a platform service according to underlying system
    """
    if platform.system() == 'Linux':
        return LinuxService()
    else:
        return WindowsService()
