# -*- coding: utf-8 -*-
"""Vercel Serverless API"""

import os
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import Literal

from backend.app.services.pdf_generator import generate_plan

app = FastAPI()


class GenerateRequest(BaseModel):
    store_name: str
    platform: Literal['eleme', 'meituan', 'both']


@app.post("/api/generate")
async def generate_pdf(request: GenerateRequest):
    try:
        output_dir = tempfile.mkdtemp()
        pdf_path = generate_plan(
            store_name=request.store_name,
            platform=request.platform,
            output_dir=output_dir
        )
        return FileResponse(
            path=pdf_path,
            filename=os.path.basename(pdf_path),
            media_type='application/pdf'
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
