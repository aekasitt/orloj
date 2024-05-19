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
from contextlib import asynccontextmanager
from os import path, remove
from pickle import PickleError, dump, load
from typing import AsyncGenerator

### Third-Party Packages ###
from fastapi import Depends, FastAPI, Request
from fastapi.responses import PlainTextResponse, Response
from fastapi.testclient import TestClient
from pytest import fixture

### Local Modules ###
from orloj import OrlojMiddleware

TEST_PICKLE: str = "tests/orloj.pickle"


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncGenerator[None, None]:
  countdown: int = 10
  if path.exists(TEST_PICKLE):
    remove(TEST_PICKLE)
  with open(TEST_PICKLE, "wb") as pickle_file:
    dump(countdown, pickle_file)
  yield
  if path.exists(TEST_PICKLE):
    remove(TEST_PICKLE)


app: FastAPI = FastAPI(lifespan=lifespan)


@app.get("/", response_class=PlainTextResponse)
async def state() -> str:
  try:
    with open(TEST_PICKLE, "rb") as pickle_file:
      return str(load(pickle_file))
  except FileNotFoundError:
    return "File not found"


@app.put("/", response_class=PlainTextResponse)
async def reset(response: Response) -> str:
  countdown: int = 10
  try:
    with open(TEST_PICKLE, "wb") as pickle_file:
      dump(countdown, pickle_file)
  except PickleError:
    response.status_code = 500
    return "Not OK"
  return "OK"


def wind_down() -> None:
  try:
    with open(TEST_PICKLE, "rb") as pickle_file:
      countdown: int = load(pickle_file) - 1
    with open(TEST_PICKLE, "wb") as pickle_file:
      dump(countdown, pickle_file)
  except PickleError:
    ...


app.add_middleware(OrlojMiddleware, interval=1, job=wind_down, job_id="wind-down")

__all__ = ("TEST_PICKLE", "app")
