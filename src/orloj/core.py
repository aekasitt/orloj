#!/usr/bin/env python3.9
# coding:utf-8
# Copyright (C) 2023-2024 All rights reserved.
# FILENAME:    ~~/orloj/core.py
# VERSION:     0.1.3
# CREATED:     2023-12-06 21:54
# AUTHOR:      Sitt Guruvanich <aekazitt+github@gmail.com>
# DESCRIPTION:
#
# HISTORY:
# *************************************************************
"""Module defining `OrlojMiddleware` class
"""

### Standard packages ###
from typing import Any, Callable, Dict

### Third-party packages ###
from apscheduler import AsyncScheduler, RunState
from apscheduler.triggers.interval import IntervalTrigger
from starlette.types import ASGIApp, Receive, Scope, Send


class OrlojMiddleware:
    app: ASGIApp
    interval: int
    kwargs: Dict[str, Any]
    job: Callable
    job_id: str
    scheduler: AsyncScheduler

    def __init__(
        self,
        app: ASGIApp,
        job: Callable,
        job_id: str,
        scheduler: AsyncScheduler = AsyncScheduler(),
        interval: int = 3_600,
        *args: Any,
        **kwargs: Any,
    ) -> None:
        self.app = app
        self.interval = interval
        self.kwargs = {key: value for key, value in args}
        self.kwargs.update(kwargs)
        self.job = job
        self.job_id = job_id
        self.scheduler = scheduler

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        if scope["type"] == "lifespan":
            async with self.scheduler:
                await self.scheduler.add_schedule(
                    self.job,
                    IntervalTrigger(seconds=self.interval),
                    id=self.job_id,
                    kwargs=self.kwargs,
                )
                if self.scheduler.state != RunState.started:
                    await self.scheduler.start_in_background()
                await self.app(scope, receive, send)
        else:
            await self.app(scope, receive, send)


__all__ = ("OrlojMiddleware",)
