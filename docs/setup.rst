Specific setup instructions
===========================

Before playing with real hardware, you may need to run some manual setup. Depending on your hardware the steps may be different. This section maintains instructions for the supported gateways


088328 USB/Zigbee dongle
------------------------

driver
^^^^^^

This dongle embeds a CP2102 USB to UART transceiver. This driver is included in latest *Linux* kernels.
For *Windows* users, install the driver first:

 * `for Windows 32 bits <_static/088328/CP210x_VCP_Windows/CP210xVCPInstaller_x86.exe>`_
 * `for Windows 64 bits <_static/088328/CP210x_VCP_Windows/CP210xVCPInstaller_x64.exe>`_

configuration
^^^^^^^^^^^^^^

 * Open or create a Zigbee network on a device (NETW led blinking)
 * Press the button on the 088328 USB key (NETW led should start blinking slowly)
 * Press the NETW button on the device which has open the network
 * All the NETW leds should turn off excepted the one of the device which created the network


.. note::
    For gateways relying on a serial line drive (such as 088328), you can list the available ports of your system by running: *python -m serial.tools.list_ports*
