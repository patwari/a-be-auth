from fastapi import FastAPI  # type: ignore
from datetime import datetime, timezone
import json

app = FastAPI()


@app.get("/")
def hello():
    return "hello world"


@app.get("/time")
def get_server_utc_time():
    format: str = "%d/%m/%y %H:%M:%S"
    return {
        "local": datetime.now().strftime(format),
        "utc": datetime.now(timezone.utc).strftime(format),
    }
