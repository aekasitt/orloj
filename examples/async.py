#!/usr/bin/env python3.8
# coding:utf-8
# Copyright (C) 2023-2024 All rights reserved.
# FILENAME:    ~~/examples/async.py
# VERSION:     0.1.2
# CREATED:     2023-12-06 21:54
# AUTHOR:      Sitt Guruvanich <aekazitt+github@gmail.com>
# DESCRIPTION:
#
# HISTORY:
# *************************************************************
"""Example for using Orloj middleware with FastAPI application and asynchronous jobs
"""

from asyncio import sleep
from fastapi import FastAPI
from logging import Logger, getLogger
from orloj import OrlojMiddleware
from starlette.responses import PlainTextResponse, RedirectResponse
from uuid import uuid4 as uuid

app = FastAPI()
logger: Logger = getLogger("uvicorn")


async def async_hello_world() -> None:
    await sleep(1)
    logger.info("Hello, World!")


@app.get("/")
async def redirect_to_swagger_docs() -> RedirectResponse:
    return RedirectResponse("/docs")


@app.get("/health", response_class=PlainTextResponse, status_code=200)
async def health() -> str:
    return "OK"


job_id: str = str(uuid()).replace("-", "")
app.add_middleware(OrlojMiddleware, interval=3, job=async_hello_world, job_id=job_id)


__all__ = ("app",)
