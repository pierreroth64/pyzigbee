Architecture
============

The big picture
---------------

::

     -------------------                  -----------------                 ------------------
    | Your host running |                || Zigbee Gateway || )))     ((( || Zigbee device #1 ||
    |   pyzigbee        | --- HW bus --- ||                ||               ------------------
    --------------------                  ------------------                     ...

                                                                           --------------------
                                                                      ((( || Zigbee device #N ||
                                                                           --------------------

The HW (hardware) bus can be a serial line, a SPI line,... or whatever depending on the zigbee gateway. The same way, the protocol used to talk with this gateway over the HW bus can vary.


Some more details
-----------------

To reflect reality, the library has the following classes:

  * Drivers: deal with low level communication with the underlying hardware
  * Protocols: deal with encoding and decoding frames for given protocols
  * Gateways: relying on Drivers and Protocols, they provide an API to talk to Zigbee devices

The UML diagram should look like:

::
  
           ___________                                                    __________
          |           |------------------------------------------------> |          |
          |  Gateway  |            ________                              | Protocol |
          |___________|---------> |        |                             |__________|
                                  | Driver |                                 ^ ^ ^
                                  |________|                                 | | |_____________________
                                    ^  ^  ^                            ______| |_______                |
                                    |  |  |                      _____|______    ______|_________      |
                                    |  |  |                     |            |  |                |
                                    |  |  |_________________    | OpenWebNet |  | Dummy protocol | ...etc
                            ________|  |________            |   |____________|  |________________|
                     ______|________     ________|_____     |
                    |               |   |              | 
                    | Serial Driver |   | Dummy driver | ...etc
                    |_______________|   |______________|


.. note::

  The *dummy* classes are used for testing

The client code (application side) only relies on Gateway objects which are created by the library.