from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse, status_code=200)
async def index():
    # return "Hello, this is a FastAPI Server. You can check its health by accessing the URL '/healthz'"
    return """
<html>
        <head>
            <title>Example Page</title>
        </head>
        <body>
        <div>Hello, this is a FastAPI Server. You can check its health by accessing the 
            <a href="/healthz"> URL</a>.
            </div>
        </body>
    </html>
"""

@app.get("/healthz", status_code=200)
async def healthz():
    return {"message": "OK"}