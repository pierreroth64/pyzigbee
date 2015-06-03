Code example
============

Here is a simple example of pyzigbee library usage.

.. code-block:: python

    #!/usr/bin/env python
    # -*- coding: utf-8 -*-

    from pyzigbee.gateways.factory import GatewayFactory

	gateway = GatewayFactory.create_gateway(ref="088328")

	with closing(self.gateway.open()) as gateway:
        ids = gateway.scan()

    print "Zigbee devices on the network:", ids

You may need to pass a configuration file to the factory to be override some driver arguments. Change gateway creation as following:

.. code-block:: python

	gateway = GatewayFactory.create_gateway(ref="088328", conf_filename="my_conf.json")
	

