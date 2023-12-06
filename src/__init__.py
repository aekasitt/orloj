#!/usr/bin/env python3.8
# coding:utf-8
# Copyright (C) 2023 All rights reserved.
# FILENAME:    ~~/src/__init__.py
# VERSION: 	   0.1.0
# CREATED: 	   2023-12-06 21:54
# AUTHOR: 	   Sitt Guruvanich <aekazitt+github@gmail.com>
# DESCRIPTION:
#
# HISTORY:
# *************************************************************
"""Scheduler middleware for ASGI frameworks
"""

__version__ = "0.1.0"


from src.core import OrlojMiddleware


__all__ = ["OrlojMiddleware"]
