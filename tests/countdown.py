#!/usr/bin/env python3.9
# coding:utf-8
# Copyright (C) 2023-2024 All rights reserved.
# FILENAME:    ~~/tests/countdown.py
# VERSION:     0.1.3
# CREATED:     2024-05-18 21:08
# AUTHOR:      Sitt Guruvanich <aekazitt+github@gmail.com>
# DESCRIPTION:
#
# HISTORY:
# *************************************************************

### Standard packages ###
from time import sleep

### Third-party packages ###
from fastapi.testclient import TestClient
from httpx import Response

### Local modules ###
from tests import app


def test_countdown() -> None:
  with TestClient(app) as test_client:
    response: Response = test_client.put("/")
    assert response.text == "OK"
    response = test_client.get("/")
    assert response.text == "10"
    sleep(1)
    response = test_client.get("/")
    assert response.text == "9"
    sleep(1)
    response = test_client.get("/")
    assert response.text == "8"
    sleep(1)
    response = test_client.get("/")
    assert response.text == "7"
    sleep(1)
    response = test_client.get("/")
    assert response.text == "6"
    sleep(1)
    response = test_client.get("/")
    assert response.text == "5"
    sleep(1)
    response = test_client.get("/")
    assert response.text == "4"
    sleep(1)
    response = test_client.get("/")
    assert response.text == "3"
    sleep(1)
    response = test_client.get("/")
    assert response.text == "2"
    sleep(1)
    response = test_client.get("/")
    assert response.text == "1"
    response = test_client.put("/")
    assert response.text == "OK"
    response = test_client.get("/")
    assert response.text == "10"
