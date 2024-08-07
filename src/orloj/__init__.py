#!/usr/bin/env python3.9
# coding:utf-8
# Copyright (C) 2023-2024 All rights reserved.
# FILENAME:    ~~/orloj/__init__.py
# VERSION:     0.1.4
# CREATED:     2023-12-06 21:54
# AUTHOR:      Sitt Guruvanich <aekazitt+github@gmail.com>
# DESCRIPTION: https://www.w3docs.com/snippets/python/what-is-init-py-for.html
#
# HISTORY:
# *************************************************************
"""Scheduler middleware for ASGI frameworks"""

__version__ = "0.1.4"


from orloj.core import OrlojMiddleware


__all__ = ("OrlojMiddleware",)
