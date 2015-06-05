Hardware setup
==============

Before playing with real hardware, you may need to run some manual setup. Depending on your hardware the steps may be different. This section maintains instructions for the supported gateways


088328 USB/Zigbee dongle
------------------------

 * Open or create a Zigbee network on a device (NETW led blinking)
 * Press the button on the 088328 USB key (NETW led should start blinking slowly)
 * Press the NETW button on the device which has open the network
 * All the NETW leds should turn off excepted the one of the device which created the network


.. note::
    For gateways relying on a serial line drive (such as 088328), you can list the available ports of your system by running: *python -m serial.tools.list_ports*
