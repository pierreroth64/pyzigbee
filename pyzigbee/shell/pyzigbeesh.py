#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2015 Legrand France
# All rights reserved

import cmd
import sys
import logging
import pprint
import os
from optparse import OptionParser
from contextlib import closing
from pyzigbee.gateways.factory import GatewayFactory
from pyzigbee.core.exceptions import PyZigBeeException
from pyzigbee import __version__
from pyzigbee.shell.platform_srvc import create_platform_service

try:
    from colorlog import basicConfig
    FORMAT = '%(log_color)s%(asctime)s:%(name)s:%(levelname)s: %(message)s'
except ImportError:
    from logging import basicConfig
    FORMAT = '%(asctime)s:%(name)s:%(levelname)s: %(message)s'


def handle_exception(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except PyZigBeeException as error:
            print "Error:", error.msg
    inner.__doc__ = func.__doc__
    return inner


class PyZigBeeShell(cmd.Cmd):
    """

    PyZigBeeShell is the Cmd class of the pyzigbee shell app
    """

    intro = "###################################\n" \
            "# Welcome to the PyZigBee shell!  #\n" \
            "#       (pyzigbee lib: %s)       #\n" \
            "# Type help or ? to list commands.#\n" \
            "###################################\n" % __version__
    prompt = '(pyzigbeesh) '

    def __init__(self, conf_filename=None):
        cmd.Cmd.__init__(self)
        self.conf_filename = conf_filename
        self.gateway = GatewayFactory(conf_filename=self.conf_filename) \
            .create_gateway(ref="088328")
        self.logger = logging.getLogger("pyzigbee.shell")
        self.pp = pprint.PrettyPrinter(indent=4)
        self.platform_srvc = create_platform_service()
        PyZigBeeShell.intro += "\ngateway: %s \n" % self.gateway.get_info()["description"]
        PyZigBeeShell.intro += "conf file: %s \n" % self.conf_filename
        PyZigBeeShell.intro += "platform: %s \n" % self.platform_srvc

    def do_clear(self, arg):
        """
        Clear screen
        """
        self.platform_srvc.clear()

    @handle_exception
    def do_gw_info(self, arg):
        """
        Print information about the current gateway
        """
        self.pp.pprint(self.gateway.get_info())

    @handle_exception
    def do_gw_supported(self, arg):
        """
        Print list of currently supported gateways
        """
        self.pp.pprint(GatewayFactory.get_supported_refs())

    @handle_exception
    def do_gw_change(self, ref):
        """
        Change the current gateway

        arg: gateway reference
        """
        self.gateway = GatewayFactory(conf_filename=self.conf_filename)\
            .create_gateway(ref=ref)

    @handle_exception
    def do_scan(self, arg):
        """
        Scan the network and print the found zigbee devices

        Optional arg: number of seconds to wait for an answer
        """
        if arg == "":
            arg = 5

        with closing(self.gateway.open()) as gateway:
            ids = gateway.scan(delay=arg)

        for id in ids:
            print id

    @handle_exception
    def do_receive(self, arg):
        """
        Receive frame from the network

        Optional arg: number of seconds to block (no arg means infinite)
        """
        with closing(self.gateway.open()) as gateway:
            print gateway.receive(timeout=arg)

    @handle_exception
    def do_bind(self, arg):
        """
        Bind procecure

        arg: is the zigbee ID to bind with
        """
        with closing(self.gateway.open()) as gateway:
            print gateway.bind(zigbee_id=arg)

    @handle_exception
    def do_version(self, arg):
        """
        Request the device for its firmware/hardware version numbers

        Optional arg: zigbee ID (if unset request the gateway version numbers)
        """
        with closing(self.gateway.open()) as gateway:
            print "firmware:", gateway.get_firmware_version(zigbee_id=arg)
            print "hardware:", gateway.get_hardware_version(zigbee_id=arg)

    @handle_exception
    def do_drv_read(self, arg):
        """
        Read data trough the gateway driver (bypassing protocol decoding)

        Optional arg: number of bytes to read
        """
        print self.gateway.driver.read(to_read=arg)

    @handle_exception
    def do_drv_write(self, arg):
        """
        Write data to the gateway driver (bypassing protocol encoding)

        example: drv_write 12345
        """
        self.gateway.driver.write(arg)

    @handle_exception
    def do_drv_open(self, arg):
        """
        Open the gateway driver
        """
        self.gateway.driver.open()

    @handle_exception
    def do_drv_close(self, arg):
        """
        Close the gateway driver
        """
        self.gateway.driver.close()


def get_conf_filename(options):
    """
    Return a configuration filename according to given options
    """
    if options.conf_filename is None:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        default_conf = os.path.join(current_dif, "conf.json")
        if os.path.exists(default_conf):
            conf_filename = default_conf
        else:
            conf_filename = None
    else:
        if os.path.exists(options.conf_filename):
            conf_filename = options.conf_filename
        else:
            print "Error: %s does not exist" % options.conf_filename
            sys.exit(1)
    return conf_filename


def main():
    parser = OptionParser()
    parser.add_option("-d", "--debug", dest="debug_level",
                      help="set log level to LEVEL", metavar="LEVEL")
    parser.add_option("-c", "--conf", dest="conf_filename",
                      help="configuration FILENAME", metavar="FILENAME")
    (options, args) = parser.parse_args()
    if options.debug_level is not None:
        level = int(options.debug_level)
    else:
        level = logging.CRITICAL

    basicConfig(level=level, format=FORMAT)

    try:
        PyZigBeeShell(conf_filename=get_conf_filename(options)).cmdloop()
    except KeyboardInterrupt:
        print "Bye!"
        sys.exit(0)

if __name__ == '__main__':
    main()
