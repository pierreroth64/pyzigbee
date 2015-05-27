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

class PyZigBeeAmbiguous(PyZigBeeException):
    """Raised when definition of a data does not lead to unique result as it should"""

    def __init__(self, msg, detail=None):
        super(PyZigBeeAmbiguous, self).__init__(msg=msg, detail=detail)

class PyZigBeeNotAvailable(PyZigBeeException):
    """Raised when a request is done on data  that is not available"""

    def __init__(self, msg, detail=None):
        super(PyZigBeeNotAvailable, self).__init__(msg=msg, detail=detail)

class PyZigBeeEntryAlreadyExists(PyZigBeeException):
    """Raised when an attempt is made to add data that already exists and must be unique"""

    def __init__(self, msg, detail=None):
        super(PyZigBeeEntryAlreadyExists, self).__init__(msg=msg, detail=detail)

class PyZigBeeBadFormatError(PyZigBeeException):
    """Raised when bad format is encountered"""

    def __init__(self, msg, detail=None):
        super(PyZigBeeBadFormatError, self).__init__(msg=msg, detail=detail)

class PyZigBeeResourceNotFound(PyZigBeeException):
    """Raised when a resource is not found"""

    def __init__(self, msg, detail=None):
        super(PyZigBeeResourceNotFound, self).__init__(msg=msg, detail=detail)

class PyZigBeeBadConfig(PyZigBeeException):
    """Raised when a bad configuration is provided"""

    def __init__(self, msg, detail=None):
        super(PyZigBeeBadConfig, self).__init__(msg=msg, detail=detail)

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

class PyZigBeeExceedLimit(PyZigBeeException):
    """Raised when a system limit is reached"""

    def __init__(self, msg, detail=None):
        super(PyZigBeeExceedLimit, self).__init__(msg=msg, detail=detail)

class PyZigBeeOperationNotSupported(PyZigBeeException):
    """Raised when a operation is not supported"""

    def __init__(self, msg, detail=None):
        super(PyZigBeeOperationNotSupported, self).__init__(msg=msg, detail=detail)

class PyZigBeeWarning(PyZigBeeException):
    """Raised to warn the calling code"""

    def __init__(self, msg, detail=None):
        super(PyZigBeeWarning, self).__init__(msg=msg, detail=detail)

class PyZigBeeNotEnough(PyZigBeeException):
    """Raised to warn not enough data"""

    def __init__(self, msg, detail=None):
        super(PyZigBeeNotEnough, self).__init__(msg=msg, detail=detail)

class PyZigBeeAborted(PyZigBeeException):
    """Raised when an abort is requested"""

    def __init__(self, msg, detail=None):
        super(PyZigBeeAborted, self).__init__(msg=msg, detail=detail)

class PyZigBeeDenied(PyZigBeeException):
    """Raised when an operation is requested but conditions required are not met"""

    def __init__(self, msg, detail=None):
        super(PyZigBeeDenied, self).__init__(msg=msg, detail=detail)

class PyZigBeeTimedOut(PyZigBeeException):
    """Raised when operation timed out"""

    def __init__(self, msg, detail=None):
        super(PyZigBeeTimedOut, self).__init__(msg=msg, detail=detail)

