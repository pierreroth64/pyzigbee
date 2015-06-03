#!/usr/bin/env python
# -*- coding: utf-8 -*-

from contextlib import closing
from pyzigbee.gateways.factory import GatewayFactory

gateway = GatewayFactory.create_gateway(ref="088328")

with closing(gateway.open()) as gateway:
    ids = gateway.scan()

print "Zigbee devices on the network:", ids