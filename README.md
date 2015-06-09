pyzigbee is a library that lets to talk to Legrand zigbee devices through gateways

[![Build Status](https://travis-ci.org/pierreroth/pyzigbee.svg?branch=master)](https://travis-ci.org/pierreroth/pyzigbee) [![Build status](https://ci.appveyor.com/api/projects/status/pxiciuj8ikefmx1b?svg=true)](https://ci.appveyor.com/project/pierreroth/pyzigbee)

Installation
------------

If you only want to install the library:

    python setup.py install

or with python installer:

    pip install .

Use the python installer to install other dependencies that may be needed to run tests or build documentation:

    pip install -r requirements.txt

Testing
-------

To run the full test suite, from the top directory:

    make test

Documentation
-------------

Latest documentattion can be found here: http://pyzigbee.readthedocs.org/en/latest/

To build the documentation:

    make doc

Contributing
------------

You may want to submit some pull requests. Make sure the following command runs without any error:

    make check
