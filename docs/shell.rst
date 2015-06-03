Shell
=====

When :doc:`installing </install>` the pyzgbee library, a shell script called **pyzigbeesh** is also installed.

You can call it from command line:

::

  pyzigbeesh

To display currenly supported arguments:

::

  pyzigbeesh --help

For example, to activate logs:

::

  pyzigbeesh -d 10


.. warning::

  You may need to gain priviledges on your machine to access the underlying hardware (such as the serial com port). A *sudo pyzigbeesh* should do the trick.


.. _configuration:

Configuration
-------------

The pyzigbee library has a default configuration for each supported gateway. This configuration (mainly driver settings) may be overriden by a JSON config file that can be passed to the shell using the *--conf* option.

Here is an example of such a **conf.json** configuration file:

.. code::

	{
	    "088328": {
	        "driver": {
	            "args": {
	                "port": "/dev/ttyUSB0",
	                "baudrate": "19200"
	            }
	        }
	    }
	}

This configuration file could be changed to the following to work on Windows machines:

.. code::

	{
	    "088328": {
	        "driver": {
	            "args": {
	                "port": "COM1",
	                "baudrate": "19200"
	            }
	        }
	    }
	}
