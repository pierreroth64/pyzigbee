pyzigbee is a library that lets to talk to Legrand zigbee devices through gateways

[![Build Status](https://travis-ci.org/pierreroth64/pyzigbee.svg?branch=master)](https://travis-ci.org/pierreroth64/pyzigbee)
[![Build status](https://ci.appveyor.com/api/projects/status/gnccdbmn420v6fo7/branch/master?svg=true)](https://ci.appveyor.com/project/pierreroth64/pyzigbee) [![Build status](https://readthedocs.org/projects/pyzigbee/badge/)](http://pyzigbee.readthedocs.org/en/latest/) [![Code Health](https://landscape.io/github/pierreroth64/pyzigbee/master/landscape.svg?style=flat)](https://landscape.io/github/pierreroth64/pyzigbee/master) [![Coverage Status](https://coveralls.io/repos/pierreroth64/pyzigbee/badge.svg?branch=master&service=github)](https://coveralls.io/github/pierreroth64/pyzigbee?branch=master)


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

Other formats and older versions: https://readthedocs.org/projects/pyzigbee/

To build the documentation:

    make doc

Contributing
------------

You may want to submit some pull requests. Make sure the following command runs without any error:

    make check
