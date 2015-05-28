Installation
============

Library only
------------

If you only want to install the pyzigbee library, just run:

::

    pip install -r requirements.txt

Note: that this will also install sphinxdoc generator which is not strictly needed.

For minimal installation (you won't be able to build the documentation or run tests):

::

    pip install -r requirements_mini.txt


Qt application
--------------

There's a Qt application which can be run on top of the pyzigbee library.
Here are the steps to install Qt and PyQt on Linux:


* Install the python headers

::

    sudo apt-get install python-dev

* Install Qt5: download and run the Qt installer
* Install SIP: download it `here <http://www.riverbankcomputing.com/software/sip/download/>`_

::

  tar zxf sip-4.16.7.tar.gz
  cd sip-4.16.7
  python configure
  make
  sudo make install

* Set QT5 by default
::

  sudo apt-get install qt5-default.

* Install PyQt: download it `here <http://www.riverbankcomputing.com/software/pyqt/download5/>`_

::

  tar zxf PyQt-gpl-5.4.1.tar.gz
  cd PyQt-gpl-5.4.1
  python configure
  make
  sudo make install

* Finally, run the application

::

  cd pyzigbee/gui
  ./pyzigbeegui.py &
