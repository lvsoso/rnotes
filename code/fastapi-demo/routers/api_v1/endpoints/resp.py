from typing import Any
from fastapi import APIRouter
from fastapi.responses import PlainTextResponse, FileResponse, StreamingResponse,\
     RedirectResponse, HTMLResponse

router = APIRouter()

@router.get("/plaintext", response_class=PlainTextResponse)
async def plaintext():
    return "Hello, world!"

@router.get("/file")
async def file():
    return FileResponse("test.http")

@router.get("/stream")
async def stream():
    async def generate():
        for i in range(10):
            yield f"Message {i}\n"
    return StreamingResponse(generate())

@router.get("/redirect")
async def redirect():
    return RedirectResponse(url="/api/v1/resp/plaintext")

@router.get("/html")
async def html():
    return HTMLResponse(content="<h1>Hello, world!</h1>")