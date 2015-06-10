#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2015 Legrand France
# All rights reserved

import os.path
from pyzigbee.core.exceptions import PyZigBeeResourceNotFound
from pyzigbee.core.exceptions import PyZigBeeBadFormat
from pyzigbee.conf.jsonreader import JSONConfReader
from pyzigbee.conf.donothingreader import DoNothingConfReader

SUPPORTED_FORMATS = {
    ".json": JSONConfReader
}


class ConfReaderFactory(object):
    """
    ConfReader factory which creates Configuration readers according
    to passed configuration filename
    """

    @classmethod
    def create_conf_reader(cls, conf_filename=None):
        if conf_filename is None:
            return DoNothingConfReader()

        if not os.path.exists(conf_filename):
            raise PyZigBeeResourceNotFound("Could not find configuration file: %s"
                                           % conf_filename)
        extension = os.path.splitext(conf_filename)[1]
        try:
            return SUPPORTED_FORMATS[extension](conf_filename)
        except KeyError:
            raise PyZigBeeBadFormat("%s extension for configuration file"
                                    " is not supported (supported ones: %s)"
                                    % (extension, SUPPORTED_FORMATS.keys()))
