from typing import Any
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from middleware import middleware
from routers.api_v1.routers import router
from config import Settings

app = FastAPI(
    title="FastAPI",
    version="0.1.0",
    summary="FastAPI",
    description="FastAPI",
    # openapi_url="", # 禁用openapi文档
    root_path="/fast-app",
    middleware=middleware, # 注册中间件
)

settings = Settings()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(router, prefix="/api/v1")


# 配置信息
@app.get("/info")
async def info():
    return {
        "app_name": settings.app_name,
        "admin_email": settings.admin_email,
        "items_per_user": settings.items_per_user,
    }

# 静态文件目录
app.mount("/static", StaticFiles(directory="static"), name='static')
templates = Jinja2Templates(directory="templates")

@app.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse("item.html", {"request": request, "id": id})

# 多个 APP
@app.get("/app")
def read_main() -> Any:
    return {"message": "Hello World from main app"}

subapi = FastAPI()
@subapi.get("/sub")
def read_sub() -> Any:
    return {"message": "Hello World from sub API"}

app.mount("/subapi", subapi)
