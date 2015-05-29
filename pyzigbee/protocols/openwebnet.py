#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2015 Legrand France
# All rights reserved

import re
import logging
from pyzigbee.protocols.baseprotocol import BaseProtocol
from pyzigbee.core.exceptions import PyZigBeeBadFormatError

class OWNProtocol(BaseProtocol):
    """OWN protocol is in charge of decoding/encoding OpenWebNet frames"""

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def get_info(self):

        return { "description": "OpenWebNet protocol" }

    def get_end_of_frame_sep(self):

        return "##"

    def encode_get_dev_number(self):
        """Build the frames sequence to get the number of devices"""

        return [ { "tx": "*13*65*##" },
                 { "rx": "*#*1##" },
                 { "delay": 5 },
                 { "answer": ""} ]

    def decode_dev_number(self, data):
        """Decode the given data to find the number of devices"""

        m = re.match("\*\#13\*\*67\*(\S+)\#\#", data)
        if m is not None:
            dev_nb = int(m.group(1))
            self.logger.debug("number of devices: %d", dev_nb)
            return dev_nb
        else:
            raise PyZigBeeBadFormatError("OWN: could not extract device number from frame: %s" % data)

    def encode_get_dev_id(self, dev_index):
        """Build the frames sequence to get the device ID from a gievn device index"""

        return [ { "tx": "*#13**66#%d##" % dev_index},
                 { "answer": ""} ]

    def decode_dev_id(self, data):
        """Decode the given data to find the device ID"""

        m = re.match("\*\#13\*(.*)\#.*\#.*\#\#", data)
        if m is not None:
            dev_id = m.group(1)
            self.logger.debug("device ID: %s", dev_id)
            return dev_id
        else:
            raise PyZigBeeBadFormatError("OWN: could not extract device ID from frame: %s" % data)

    def encode_get_version(self):
        """Build the frames sequence to get the firmware version of the gateway"""

        return [ { "tx": "*#13**16##" },
                 { "answer": ""} ]

    def decode_version(self, data):
        """Decode the given data to find the gateway firmware version"""

        m = re.match("\*\#13\*\*16\*(\S+)\*(\S+)\*(\S+)\#\#", data)
        if m is not None:
            version = m.group(1) + "." + m.group(2) + "." + m.group(3)
            self.logger.debug("gateway version: %s", version)
            return version
        else:
            raise PyZigBeeBadFormatError("OWN: could not extract gateway version from frame: %s" % data)
