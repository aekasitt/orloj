#!/usr/bin/env python3.9
# coding:utf-8
# Copyright (C) 2023-2024 All rights reserved.
# FILENAME:    ~~/tests/__init__.py
# VERSION:     0.1.3
# CREATED:     2024-05-18 13:02
# AUTHOR:      Sitt Guruvanich <aekazitt+github@gmail.com>
# DESCRIPTION: https://www.w3docs.com/snippets/python/what-is-init-py-for.html
#
# HISTORY:
# *************************************************************
"""Module defining test_client fixture used by test suites under tests/ directory."""

### Standard Packages ###
from pytest import fixture

### Third-Party Packages ###
from fastapi import Depends, FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.testclient import TestClient

### Local Modules ###
from orloj import OrlojMiddleware


@fixture
def test_client() -> TestClient:
  """
  Sets up a FastAPI TestClient with OrlojMiddleware updating local pickle file created and
  destroyed by lifespan asynccontextmanager.

  ---
  :returns: TestClient
  """
  app = FastAPI()

  # TODO: create lifespan asynccontextmanager and two endpoints
  # 1: /reset - resets the clock and start state at 10
  # 2: /state - get countdown state
  # with the orlojmiddleware counting down from ten and saving state to pickle-file
  # read only by /state endpoint
  return TestClient(app)
