# -*- coding: utf-8 -*-
"""
外卖活动方案生成器 - FastAPI 主入口
呈尚策划 品牌定制
"""

import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.api.routes import router

app = FastAPI(
    title="外卖活动方案生成器",
    description="为外卖店铺生成专业的平台活动方案PDF文档",
    version="1.0.0"
)

# 注册 API 路由
app.include_router(router, prefix="/api")

# 静态文件目录
static_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "static")
app.mount("/static", StaticFiles(directory=static_dir), name="static")


@app.get("/")
async def index():
    return FileResponse(os.path.join(static_dir, "index.html"))
