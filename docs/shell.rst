Shell
=====

When installing the pyzgbee library, a shell script called **pyzigbeesh** is also installed.

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

  You may need to gain priviledges on your machine to access the serial com port. A *sudo pyzigbeesh* should do the trick.
