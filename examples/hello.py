#!/usr/bin/env python3.8
# coding:utf-8
# Copyright (C) 2023-2024 All rights reserved.
# FILENAME:    ~~/examples/hello.py
# VERSION:     0.1.3
# CREATED:     2023-12-06 21:54
# AUTHOR:      Sitt Guruvanich <aekazitt+github@gmail.com>
# DESCRIPTION:
#
# HISTORY:
# *************************************************************
"""Example for using Orloj middleware with FastAPI application and parametrized jobs
"""

from fastapi import FastAPI
from logging import Logger, getLogger
from orloj import OrlojMiddleware
from starlette.responses import PlainTextResponse
from uuid import uuid4 as uuid

app = FastAPI()
logger: Logger = getLogger("uvicorn")


def hello_name(name: str) -> None:
    logger.info(f"Hello, {name}!")


def hello_world() -> None:
    logger.info("Hello, World!")


@app.get("/")
async def redirect_to_swagger_docs() -> str:
    return "OK"


@app.get("/health", response_class=PlainTextResponse, status_code=200)
async def health() -> str:
    return "OK"


job_id_name: str = str(uuid()).replace("-", "")
job_id_world: str = str(uuid()).replace("-", "")
app.add_middleware(OrlojMiddleware, interval=3, job=hello_name, job_id=job_id_name, name="Igor")
app.add_middleware(OrlojMiddleware, interval=6, job=hello_world, job_id=job_id_world)

__all__ = ("app",)
