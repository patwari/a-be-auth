from typing import Optional
from fastapi import FastAPI, Query
from datetime import datetime, timezone
import json

app = FastAPI()


@app.get("/")
def hello():
    return "hello world"


@app.get("/time")
def get_server_time(name: Optional[str] = None, country: Optional[str] = None):
    format: str = "%d/%m/%y %H:%M:%S"

    info: str = None

    if name and country:
        info = f"Hello {name.title()} from {country.title()}"
    elif name:
        info = f"Hello {name.title()}"
    elif country:
        info = f"Hey man from {country.title()}"

    if info:
        return {
            "message": info,
            "local": datetime.now().strftime(format),
            "utc": datetime.now(timezone.utc).strftime(format),
        }
    else:
        return {
            "local": datetime.now().strftime(format),
            "utc": datetime.now(timezone.utc).strftime(format),
        }
