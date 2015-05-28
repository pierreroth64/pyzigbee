#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2015 Legrand France
# All rights reserved

import cmd, sys, logging
from optparse import OptionParser

from pyzigbee.gateways.factory import GatewayFactory

class PyZigBeeShell(cmd.Cmd):
    intro = 'Welcome to the PyZigBee shell. Type help or ? to list commands.\n'
    prompt = '(pyzigbeesh) '
    gateway = GatewayFactory.create_gateway("088328")
    logger = logging.getLogger(__name__)

    # ----- basic turtle commands -----
    def do_gw_info(self, arg):
        'Print current information about the current gateway'
        print self.gateway.get_description()

    def do_scan(self, arg):
        'Scan the network and print the found zigbee devices'
        self.logger.debug('scanning...')
        self.gateway.open()
        ids = self.gateway.scan()
        self.gateway.close()
        print ids

if __name__ == '__main__':

    parser = OptionParser()
    parser.add_option("-d", "--debug", dest="debug_level",
                      help="set log level to LEVEL", metavar="LEVEL")
    (options, args) = parser.parse_args()
    level = int(options.debug_level) if options.debug_level else logging.INFO
    logging.basicConfig(level=level)
    PyZigBeeShell().cmdloop()
