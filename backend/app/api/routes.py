# -*- coding: utf-8 -*-
"""
API 路由定义
"""

import os
import tempfile
from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import Literal

from app.services.pdf_generator import generate_plan

router = APIRouter()


class GeneratePlanRequest(BaseModel):
    """生成方案请求模型"""
    store_name: str
    platform: Literal['eleme', 'meituan', 'both']


@router.post("/generate")
async def generate_pdf(request: GeneratePlanRequest):
    """
    生成外卖活动方案PDF

    - store_name: 店铺名称
    - platform: 平台类型 (eleme/meituan/both)
    """
    try:
        # 使用临时目录存储生成的PDF
        output_dir = tempfile.mkdtemp()
        pdf_path = generate_plan(
            store_name=request.store_name,
            platform=request.platform,
            output_dir=output_dir
        )

        # 返回文件下载
        filename = os.path.basename(pdf_path)
        return FileResponse(
            path=pdf_path,
            filename=filename,
            media_type='application/pdf'
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
