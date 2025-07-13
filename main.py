from http.client import HTTPException
from typing import Optional
from fastapi import FastAPI, Query
from datetime import datetime, timedelta, timezone
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def hello():
    return "hello world"


@app.get("/time")
def get_server_time(name: Optional[str] = None, country: Optional[str] = None) -> dict:
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


@app.get("/time/offset/{offset}")
def get_server_time_with_offset(offset: float) -> dict:
    if offset < -12 or offset > 14:
        # bad request
        raise HTTPException(status_code=400, detail="Invalid time offset")

    format: str = "%d/%m/%y %H:%M:%S"
    utc_time: datetime = datetime.now(timezone.utc)

    return {
        "utc": utc_time.strftime(format),
        "offset_time": (utc_time + timedelta(hours=offset)).strftime(format),
    }


# Request Body Schema
class User(BaseModel):
    name: str
    country: str


@app.post("/time")
def get_server_time(user: User) -> dict:
    format: str = "%d-%m-%y %H:%M:%S"
    return {
        "message": f"hello {user.name.title()} from {user.country.title()}",
        "local": datetime.now().strftime(format),
        "utc": datetime.now(timezone.utc).strftime(format),
    }
