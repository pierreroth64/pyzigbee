#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2015 Legrand France
# All rights reserved

"""This module contains all the exceptions that may raise
    when using the pyzigbee library"""

class PyZigBeeException(Exception):
    """Base class for pyzigbee exceptions"""

    def __init__(self, msg, detail=None):
        super(PyZigBeeException, self).__init__(msg)
        self.msg = msg
        self.detail = detail

    def __unicode__(self):
        return unicode(self.msg)

    def __repr__(self):
        return self.msg

class PyZigBeeBadFormatError(PyZigBeeException):
    """Raised when bad format is encountered"""

    def __init__(self, msg, detail=None):
        super(PyZigBeeBadFormatError, self).__init__(msg=msg, detail=detail)

class PyZigBeeResourceNotFound(PyZigBeeException):
    """Raised when a resource is not found"""

    def __init__(self, msg, detail=None):
        super(PyZigBeeResourceNotFound, self).__init__(msg=msg, detail=detail)

class PyZigBeeBadArgument(PyZigBeeException):
    """Raised when a bad argument is provided to a method"""

    def __init__(self, msg, detail=None):
        super(PyZigBeeBadArgument, self).__init__(msg=msg, detail=detail)

class PyZigBeeImportError(PyZigBeeException):
    """Raised when an import fails"""

    def __init__(self, msg, detail=None):
        super(PyZigBeeImportError, self).__init__(msg=msg, detail=detail)

class PyZigBeeFailed(PyZigBeeException):
    """Raised when a command/routine fails"""

    def __init__(self, msg, detail=None):
        super(PyZigBeeFailed, self).__init__(msg=msg, detail=detail)

class PyZigBeeOperationNotSupported(PyZigBeeException):
    """Raised when a operation is not supported"""

    def __init__(self, msg, detail=None):
        super(PyZigBeeOperationNotSupported, self).__init__(msg=msg, detail=detail)

class PyZigBeeDenied(PyZigBeeException):
    """Raised when an operation is requested but conditions required are not met"""

    def __init__(self, msg, detail=None):
        super(PyZigBeeDenied, self).__init__(msg=msg, detail=detail)

class PyZigBeeTimedOut(PyZigBeeException):
    """Raised when operation timed out"""

    def __init__(self, msg, detail=None):
        super(PyZigBeeTimedOut, self).__init__(msg=msg, detail=detail)

