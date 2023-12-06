# Orloj

[![Format](https://img.shields.io/pypi/format/orloj)](https://pypi.org/project/orloj)
[![Python version](https://img.shields.io/pypi/pyversions/orloj)](https://pypi.org/project/orloj)
[![License](https://img.shields.io/pypi/l/orloj)](https://pypi.org/project/orloj)
[![Top](https://img.shields.io/github/languages/top/aekasitt/orloj)](.)
[![Languages](https://img.shields.io/github/languages/count/aekasitt/orloj)](.)
[![Size](https://img.shields.io/github/repo-size/aekasitt/orloj)](.)
[![Last commit](https://img.shields.io/github/last-commit/aekasitt/orloj/master)](.)

[![Orloj banner](static/orloj-banner.svg)](static/orloj-banner.svg)

## Getting Started

The following example shows you how to setup `OrlojMiddleware` to run scheduled tasks alongside
your [FastAPI](https://github.com/tiangolo/fastapi) application.

```python
from fastapi import FastAPI
from logging import Logger, getLogger
from orloj import OrlojMiddleware
from starlette.responses import PlainTextResponse, RedirectResponse

app = FastAPI()
logger: Logger = getLogger("uvicorn")

def hello_name(name: str) -> None:
  logger.info(f"Hello, {name}!")

def hello_world() -> None:
  logger.info("Hello, World!")

@app.get("/")
async def redirect_to_swagger_docs() -> RedirectResponse:
  """Redirects to swagger documentation
  """
  return RedirectResponse("/docs")

@app.get("/health", response_class=PlainTextResponse, status_code=200)
async def health() -> str:
  """Health check
  """
  return "OK"

app.add_middleware(OrlojMiddleware, interval=3, job=hello_name, name="Igor")
app.add_middleware(OrlojMiddleware, interval=6, job=hello_world)
```

## Contributions

To contribute to the project, fork the repository and clone to your local device and development
dependencies including three extra libraries not included in final builds as such:

* [black](https://github.com/psf/black) - The uncompromising Python code formatter 
* [mypy](https://github.com/python/mypy) - Optional static typing for Python
* [pytest](https://github.com/pytest-dev/pytest) - The pytest framework makes it easy to write small tests, yet scales to support complex functional testing

Use the following commands to setup your local environment with development dependencies:

```bash
pip install --user poetry
poetry install --with dev
```

## Acknowledgements

* [Wikimedia Commons - File:Prague Astronomical Clock.svg](https://commons.wikimedia.org/wiki/File:Prague_Astronomical_Clock.svg)

## License

This project is licensed under the terms of the MIT license.