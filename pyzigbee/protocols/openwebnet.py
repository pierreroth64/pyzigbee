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
    """OWN protocol is in charge of decoding/encoding OpenWebNet frames
    """

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def get_info(self):

        return { "description": "OpenWebNet protocol" }

    def get_end_of_frame_sep(self):
        return "##"

    def encode_get_dev_number(self):
        sequence = [ { "tx": "*13*65*##" },
                     { "rx": "*#*1##" },
                     { "delay": 5 },
                     { "answer": ""}
                   ]
        return sequence

    def decode_dev_number(self, data):
        m = re.match("\*\#13\*\*67\*(\S+)\#\#", data)
        if m is not None:
            dev_nb = int(m.group(1))
            self.logger.debug("device number: %d", dev_nb)
            return dev_nb
        else:
            raise PyZigBeeBadFormatError("OWN: could not extract device number from frame: %s" % data)

    def encode_get_dev_id(self, dev_index):
        sequence = [ { "tx": "*#13**73#%d##" % dev_index},
                     { "rx": "*#*1##" },
                     { "answer": ""},
                   ]
        return sequence

    def decode_dev_id(self, data):
        m = re.match("\*\#13\*(\S+)\#9\*73\#\S+\#\#", data)
        if m is not None:
            dev_id = m.group(1)
            self.logger.debug("device ID: %s", dev_id)
            return dev_id
        else:
            raise PyZigBeeBadFormatError("OWN: could not extract device ID from frame: %s" % data)
