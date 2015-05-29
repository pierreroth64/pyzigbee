#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2015 Legrand France
# All rights reserved

import cmd, sys, logging, pprint
from optparse import OptionParser

from pyzigbee.gateways.factory import GatewayFactory
from pyzigbee.core.exceptions import PyZigBeeException
from pyzigbee import __version__

def handle_exception(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except PyZigBeeException as error:
            print "Error:", error.msg
    inner.__doc__= func.__doc__
    return inner

class PyZigBeeShell(cmd.Cmd):
    """PyZigBeeShell is the Cmd class of the pyzigbee shell app"""

    intro = "###################################\n" \
            "# Welcome to the PyZigBee shell!  #\n" \
            "#       (pyzigbee lib: %s)       #\n" \
            "# Type help or ? to list commands.#\n" \
            "###################################\n" % __version__
    prompt = '(pyzigbeesh) '
    gateway = GatewayFactory.create_gateway("088328")
    logger = logging.getLogger("pyzigbee.shell")
    pp = pprint.PrettyPrinter(indent=4)

    @handle_exception
    def do_gw_info(self, arg):
        """Print information about the current gateway"""

        self.pp.pprint(self.gateway.get_info())

    @handle_exception
    def do_gw_supported(self, arg):
        """Print list of currently supported gateways"""

        self.pp.pprint(GatewayFactory.get_supported_refs())

    @handle_exception
    def do_scan(self, arg):
        """Scan the network and print the found zigbee devices"""

        self.gateway.open()
        ids = self.gateway.scan()
        self.gateway.close()
        print ids

    @handle_exception
    def do_gw_version(self, arg):
        """Request the gateway for its firmware version"""

        self.gateway.open()
        version = self.gateway.get_version()
        self.gateway.close()
        print version

if __name__ == '__main__':

    parser = OptionParser()
    parser.add_option("-d", "--debug", dest="debug_level",
                      help="set log level to LEVEL", metavar="LEVEL")
    (options, args) = parser.parse_args()
    level = int(options.debug_level) if options.debug_level is not None else logging.CRITICAL
    format = '%(asctime)s:%(name)s:%(levelname)s: %(message)s'
    logging.basicConfig(level=level, format=format)
    PyZigBeeShell().cmdloop()
