from fastapi import FastAPI

from datetime import datetime

app = FastAPI()


@app.get("/")
def hello():
    return "hello world"


@app.get("/time")
def get_server_local_time():
    return datetime.now()
