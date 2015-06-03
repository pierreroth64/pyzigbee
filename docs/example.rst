Code example
============

Here is a simple example of pyzigbee library usage (see: *pyzigbee/examples/088328/scan.py*)

.. literalinclude:: ../pyzigbee/examples/088328/scan.py


You may need to pass a configuration file (see: :ref:`configuration`) to the factory to be override some driver arguments. Change gateway creation as following:

.. code-block:: python

	gateway = GatewayFactory.create_gateway(ref="088328", conf_filename="my_conf.json")
	

