#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2015 Legrand France
# All rights reserved


class DoNothingConfReader(object):
    """
    Reader for configuration: does not impact args
    """

    def __init__(self):
        pass

    def override_args_with_conf(self, ref, args):
        ref = ref
        return args
