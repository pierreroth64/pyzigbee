#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2015 Legrand France
# All rights reserved

import os.path

from pyzigbee.core.exceptions import PyZigBeeResourceNotFound, PyZigBeeBadFormatError
from pyzigbee.conf.jsonreader import JSONConfReader
from pyzigbee.conf.donothingreader import DoNothingConfReader

class ConfReaderFactory(object):
    """ConfReader factory which creates Configuration readers according
       to passed configuration filename"""

    @classmethod
    def create_conf_reader(cls, conf_filename=None):
        if conf_filename is None:
            return DoNothingConfReader()

        if not os.path.exists(conf_filename):
            raise PyZigBeeResourceNotFound("Could not find configuration file: %s" \
                                           % conf_filename)

        extension = os.path.splitext(conf_filename)[1]

        if extension == ".json":
            return JSONConfReader(conf_filename)
        else:
            raise PyZigBeeBadFormatError("%s extensions for configuration file is not supported" \
                                         % extension)
