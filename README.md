# Learning to Create BE in python

This file is for me to learn. Will be too boring. Avoid it at all cost.

## Step 1: Setup

1. One Time

   ```bash
   git init
   # add .gitignore and .gitattributes file

   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

2. Create `main.py` file.

   ```py
    from fastapi import FastAPI

    app = FastAPI()
    @app.get("/")
    def hello():
        return "hello world"
   ```

3. Host the server

   ```bash
   uvicorn main:app --reload
   ```

4. Test it on Browser / Postman. Open url = [127.0.0.1:8000](127.0.0.1:8000).
5. Verified? - Perfect
6. Now play around by adding another end points.

   ```py
   from datetime import datetime

    @app.get("/time")
    def get_server_local_time():
        return datetime.now()
   ```

7. Explore Swagger UI and ReDoc (auto-generated docs)
   - http://127.0.0.1:8000/docs — Swagger UI
   - http://127.0.0.1:8000/redoc — ReDoc
