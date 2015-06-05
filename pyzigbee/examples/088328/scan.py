#!/usr/bin/env python
# -*- coding: utf-8 -*-

from contextlib import closing
from pyzigbee.gateways.factory import GatewayFactory


def scan():
    """
    Scan the network looking for zigbee devices and print the found IDs
    """
    # Note that you may need to pass a configuration file to
    # the GatewayFactory since your low level device may be different
    # from the default one. Please read the 'Configuration' section
    # of the documentation
    gateway = GatewayFactory().create_gateway(ref="088328")

    with closing(gateway.open()) as gateway:
        ids = gateway.scan()

    print "Zigbee devices on the network:", ids

if __name__ == '__main__':
    scan()
