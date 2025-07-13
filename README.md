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

8. Catch Query Parameters

   ```py
   @app.get("/time")
   def get_server_time(name: Optional[str] = None, country: Optional[str] = None):
   ```

   - Add params in the GET requests

   ```bash
   curl http://127.0.0.1:8000/time
   # {"local":"13/07/25 19:13:12","utc":"13/07/25 13:43:12"}

   curl http://127.0.0.1:8000/time?name=rahul
   # {"message":"Hello Rahul","local":"13/07/25 19:13:58","utc":"13/07/25 13:43:58"}%

   curl http://127.0.0.1:8000/time?country=india&name=rahul
   # {"message":"Hello Rahul from India","local":"13/07/25 19:14:15","utc":"13/07/25 13:44:15"}
   ```

9. Catch Path Parameters

   ```py
   @app.get("/time/offset/{offset}")
   def get_server_time_with_offset(offset: float):
   ```

   - Add params in the GET request

   ```bash
   curl 127.0.0.1:8000/time/offset/0
   # {"utc":"13/07/25 18:42:56","offset_time":"13/07/25 18:42:56"}

   curl 127.0.0.1:8000/time/offset/0.5
   # {"utc":"13/07/25 18:42:33","offset_time":"13/07/25 19:12:33"}

   curl 127.0.0.1:8000/time/offset/+5.5
   # {"utc":"13/07/25 18:43:16","offset_time":"14/07/25 00:13:16"}

   curl 127.0.0.1:8000/time/offset/5.5
   # {"utc":"13/07/25 18:43:18","offset_time":"14/07/25 00:13:18"}
   ```

10. Setup a POST request:

- Add body in post request

  ```bash
  curl 127.0.0.1:8000/time --request POST --header 'Content-Type: application/json' --data '{ "name": "rahul", "country": "india" }'
  # {"message":"hello Rahul from India","local":"14-07-25 00:51:13","utc":"13-07-25 19:21:13"}%
  ```
