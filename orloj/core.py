#!/usr/bin/env python3.9
# coding:utf-8
# Copyright (C) 2023-2024 All rights reserved.
# FILENAME:    ~~/orloj/core.py
# VERSION:     0.1.2
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
### v3.10.4 API ###
from apscheduler.schedulers.asyncio import AsyncIOScheduler as AsyncScheduler

### TODO: v4.0.0a4 API ###
# from apscheduler import AsyncScheduler
# from apscheduler.triggers.interval import IntervalTrigger
from starlette.types import ASGIApp, Receive, Scope, Send


class OrlojMiddleware:
    app: ASGIApp
    args: Dict[str, Any]
    interval: int
    job: Callable
    scheduler: AsyncScheduler

    def __init__(
        self,
        app: ASGIApp,
        job: Callable,
        scheduler: AsyncScheduler = AsyncScheduler(),
        interval: int = 3_600,
        *args: Any,
        **kwargs: Any,
    ) -> None:
        self.app = app
        self.args = {key: value for key, value in args}
        self.args.update(kwargs)
        self.interval = interval
        self.job = job
        self.scheduler = scheduler

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        if scope["type"] == "lifespan":
            ### v3.10.4 API ###
            self.scheduler.add_job(self.job, "interval", self.args.values(), seconds=self.interval)
            self.scheduler.start()

            ### TODO:: v4.0.0a4 API ###
            # async with self.scheduler:
            #     await self.scheduler.add_schedule(
            #         self.job, IntervalTrigger(seconds=self.interval), self.args.values(), id=uuid()
            #     )
            #     await self.scheduler.start_in_background()

            await self.app(scope, receive, send)


__all__ = ["OrlojMiddleware"]
