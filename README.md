pyzigbee is a library that enables to talk to Legrand zigbee devices through gateways

[![Build Status](https://travis-ci.org/pierreroth/pyzigbee.svg?branch=master)](https://travis-ci.org/pierreroth/pyzigbee)


Installation
------------

Use the python installer to install dependencies:

    pip install -r requirements.txt

Testing
-------

To run the full test suite, from the top directory:

    PYTHONPATH=. nosetests

Refer to nosetests documentation for more information

Documentation
-------------

Full documentation is built with sphinx:

    cd docs
    PYTHONPATH=.. make html
