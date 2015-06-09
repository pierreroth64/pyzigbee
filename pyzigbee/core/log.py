#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2015 Legrand France
# All rights reserved

import logging


class NullHandler(logging.Handler):
    def emit(self, record):
        pass
