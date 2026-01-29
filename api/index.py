# -*- coding: utf-8 -*-
"""Vercel Serverless API"""

import os
import sys
import tempfile

# 设置项目根目录
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_ROOT)

# 设置字体目录环境变量
os.environ['FONT_DIR'] = os.path.join(PROJECT_ROOT, 'fonts')

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse, HTMLResponse
from pydantic import BaseModel
from typing import Literal

from backend.app.services.pdf_generator import generate_plan

app = FastAPI()


class GenerateRequest(BaseModel):
    store_name: str
    platform: Literal['eleme', 'meituan', 'both']


@app.get("/")
async def index():
    return HTMLResponse(content=HTML_PAGE)


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


HTML_PAGE = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>外卖活动方案生成器 - 呈尚策划</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
    tailwind.config = {
        theme: {
            extend: {
                colors: {
                    brand: { dark: '#1A1A2E', gold: '#C9A962', cream: '#F5F0E8' },
                    meituan: { primary: '#FFD000', bg: '#FFF8E1' },
                    eleme: { primary: '#0097FF', bg: '#E6F4FF' }
                }
            }
        }
    }
    </script>
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@600&display=swap');
    .font-serif-cn { font-family: 'Noto Serif SC', serif; }
    .stamp { border: 3px solid #C9A962; border-radius: 4px; padding: 4px 12px; transform: rotate(-3deg); }
    .glass { background: rgba(255,255,255,0.95); backdrop-filter: blur(10px); }
    </style>
</head>
<body class="min-h-screen bg-gradient-to-br from-brand-cream to-white">
    <!-- 背景装饰 -->
    <div class="fixed inset-0 overflow-hidden pointer-events-none">
        <div class="absolute top-0 right-0 w-96 h-96 bg-brand-gold/10 rounded-full blur-3xl"></div>
        <div class="absolute bottom-0 left-0 w-80 h-80 bg-eleme-primary/5 rounded-full blur-3xl"></div>
        <div class="absolute top-1/2 left-1/2 w-64 h-64 bg-meituan-primary/5 rounded-full blur-3xl"></div>
    </div>

    <div class="relative max-w-lg mx-auto py-12 px-4">
        <!-- 品牌头部 -->
        <div class="text-center mb-10">
            <div class="inline-block stamp mb-4">
                <span class="font-serif-cn text-brand-gold text-xl tracking-widest">呈尚策划</span>
            </div>
            <h1 class="text-3xl font-bold text-brand-dark mb-2">外卖活动方案</h1>
            <p class="text-gray-500 text-sm">专业外卖代运营 · 一键生成活动策划</p>
        </div>
        <!-- 主卡片 -->
        <div class="bg-white rounded-3xl p-8 shadow-xl border border-gray-100">
            <div class="space-y-6">
                <!-- 店铺名称输入 -->
                <div>
                    <label class="block text-sm font-semibold text-brand-dark mb-2">店铺名称</label>
                    <input type="text" id="storeName" placeholder="例如：霸王茶姬（春熙路店）"
                        class="w-full px-4 py-3.5 bg-brand-cream/50 border-2 border-transparent rounded-xl focus:outline-none focus:border-brand-gold focus:bg-white transition-all text-brand-dark placeholder-brand-dark/40">
                </div>

                <!-- 平台选择 -->
                <div>
                    <label class="block text-sm font-semibold text-brand-dark mb-3">目标平台</label>
                    <div class="grid grid-cols-3 gap-3">
                        <label class="cursor-pointer">
                            <input type="radio" name="platform" value="meituan" checked class="hidden peer">
                            <div class="p-4 border-2 border-gray-200 rounded-xl text-center peer-checked:border-meituan-primary peer-checked:bg-meituan-bg transition-all">
                                <div class="w-10 h-10 mx-auto mb-2 rounded-full bg-meituan-primary flex items-center justify-center text-white font-bold">美</div>
                                <div class="text-sm font-medium text-brand-dark">美团</div>
                            </div>
                        </label>
                        <label class="cursor-pointer">
                            <input type="radio" name="platform" value="eleme" class="hidden peer">
                            <div class="p-4 border-2 border-gray-200 rounded-xl text-center peer-checked:border-eleme-primary peer-checked:bg-eleme-bg transition-all">
                                <div class="w-10 h-10 mx-auto mb-2 rounded-full bg-eleme-primary flex items-center justify-center text-white font-bold">饿</div>
                                <div class="text-sm font-medium text-brand-dark">饿了么</div>
                            </div>
                        </label>
                        <label class="cursor-pointer">
                            <input type="radio" name="platform" value="both" class="hidden peer">
                            <div class="p-4 border-2 border-gray-200 rounded-xl text-center peer-checked:border-brand-gold peer-checked:bg-brand-cream transition-all">
                                <div class="w-10 h-10 mx-auto mb-2 rounded-full bg-gradient-to-r from-meituan-primary to-eleme-primary flex items-center justify-center text-white font-bold text-xs">双</div>
                                <div class="text-sm font-medium text-brand-dark">双平台</div>
                            </div>
                        </label>
                    </div>
                </div>
                <button onclick="generatePDF()" id="generateBtn"
                    class="w-full py-4 bg-brand-gold text-white font-semibold rounded-xl hover:bg-brand-gold/90 transition-all shadow-lg">
                    生成活动方案 PDF
                </button>
                <div id="status" class="hidden p-4 rounded-xl text-sm text-center"></div>
            </div>
        </div>

        <!-- 底部说明 -->
        <div class="mt-8 text-center text-gray-400 text-xs">
            <p>方案包含：爆单红包 · 减配送费 · 返券活动 · 效果预期</p>
        </div>

        <!-- 话术展示框 -->
        <div class="mt-8 bg-white rounded-2xl p-6 shadow-lg border border-gray-100">
            <div class="flex items-center justify-between mb-4">
                <div class="flex items-center gap-2">
                    <span class="text-lg">💬</span>
                    <h3 class="font-semibold text-brand-dark">客户沟通话术</h3>
                </div>
                <button onclick="copyScript()" id="copyBtn"
                    class="px-4 py-1.5 text-sm bg-brand-cream text-brand-dark rounded-lg hover:bg-brand-gold hover:text-white transition-all flex items-center gap-1">
                    <span id="copyIcon">📋</span>
                    <span id="copyText">点击复制</span>
                </button>
            </div>
            <div id="scriptContent" class="text-sm text-gray-600 leading-relaxed space-y-3 cursor-pointer hover:bg-brand-cream/30 p-4 rounded-xl transition-all" onclick="copyScript()">
                <p>老板，您店铺的活动方案我们已经发到群里了，您可以先看一下。</p>
                <p>这个方案是我们根据您店铺的数据情况和周边商圈的竞争环境来设计的，包括<span class="text-brand-gold font-medium">满减门槛、折扣力度、活动时段</span>这些都是经过测算的，既能吸引客户下单，又能保证您的利润空间不会被压得太低。</p>
                <p>我们会按照这个方案来调整您店铺的活动设置，调整完成后平台算法会重新识别您的活动数据，配合我们之前优化的<span class="text-brand-gold font-medium">关键词和商品权重</span>，曝光和转化都会有提升。</p>
                <p>活动上线后我们会持续盯着数据表现，如果某个活动的转化效果特别好我们会加大力度，效果不理想的我们也会及时调整策略。</p>
                <p>您这边如果对方案有什么想法或者疑问，随时跟我们说，我们可以根据您的实际情况做微调。</p>
            </div>
            <div id="copyStatus" class="hidden mt-3 text-center text-sm text-green-600 bg-green-50 py-2 rounded-lg">
                ✓ 已复制到剪贴板
            </div>
        </div>
    </div>
    <script>
    // ============ Tauri/Web 双环境兼容工具 ============
    function isTauriEnvironment() {
        return typeof window !== 'undefined' &&
               typeof window.__TAURI__ !== 'undefined' &&
               typeof window.__TAURI__.core !== 'undefined' &&
               typeof window.__TAURI__.core.invoke === 'function';
    }

    async function showTauriSaveDialog(filename) {
        return await window.__TAURI__.core.invoke('plugin:dialog|save', {
            options: {
                defaultPath: filename,
                title: '保存 PDF 文件',
                filters: [
                    { name: 'PDF 文件', extensions: ['pdf'] },
                    { name: '所有文件', extensions: ['*'] }
                ]
            }
        });
    }

    async function writeTauriFile(filePath, bytes) {
        await window.__TAURI__.core.invoke(
            'plugin:fs|write_file',
            bytes,
            {
                headers: {
                    path: encodeURIComponent(filePath),
                    options: JSON.stringify({})
                }
            }
        );
    }

    // ============ 浏览器下载 ============
    function browserDownload(blob, filename) {
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = filename;
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
        URL.revokeObjectURL(url);
    }

    // ============ 主函数 ============
    async function generatePDF() {
        const storeName = document.getElementById('storeName').value.trim();
        const platform = document.querySelector('input[name="platform"]:checked').value;
        const btn = document.getElementById('generateBtn');
        const status = document.getElementById('status');
        const filename = storeName + '_活动方案.pdf';

        if (!storeName) { showStatus('请输入店铺名称', 'error'); return; }

        btn.disabled = true;
        btn.textContent = '正在生成...';
        btn.classList.add('opacity-70');
        status.classList.add('hidden');

        try {
            // 1. 调用API生成PDF
            const res = await fetch('/api/generate', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ store_name: storeName, platform: platform })
            });
            if (!res.ok) throw new Error('生成失败');
            const blob = await res.blob();

            // 2. 根据环境选择下载方式
            if (isTauriEnvironment()) {
                // Tauri 环境：显示保存对话框
                console.log('[Tauri] 检测到 Tauri 环境，使用原生保存对话框');
                const filePath = await showTauriSaveDialog(filename);
                if (!filePath) {
                    showStatus('已取消保存', 'error');
                    return;
                }
                // 转换 Blob 为 Uint8Array
                const arrayBuffer = await blob.arrayBuffer();
                const bytes = new Uint8Array(arrayBuffer);
                await writeTauriFile(filePath, bytes);
                showStatus('PDF 已保存到: ' + filePath, 'success');
            } else {
                // 浏览器环境：直接下载
                console.log('[Browser] 使用浏览器下载');
                browserDownload(blob, filename);
                showStatus('PDF 已生成并开始下载', 'success');
            }
        } catch (e) {
            console.error('导出失败:', e);
            showStatus('生成失败，请重试: ' + e.message, 'error');
        } finally {
            btn.disabled = false;
            btn.textContent = '生成活动方案 PDF';
            btn.classList.remove('opacity-70');
        }
    }

    function showStatus(msg, type) {
        const s = document.getElementById('status');
        s.textContent = msg;
        s.className = 'p-4 rounded-xl text-sm text-center ' + (type === 'error' ? 'bg-red-50 text-red-600' : 'bg-green-50 text-green-600');
    }

    // ============ 话术复制功能 ============
    const SCRIPT_TEXT = `老板，您店铺的活动方案我们已经发到群里了，您可以先看一下。

这个方案是我们根据您店铺的数据情况和周边商圈的竞争环境来设计的，包括满减门槛、折扣力度、活动时段这些都是经过测算的，既能吸引客户下单，又能保证您的利润空间不会被压得太低。

我们会按照这个方案来调整您店铺的活动设置，调整完成后平台算法会重新识别您的活动数据，配合我们之前优化的关键词和商品权重，曝光和转化都会有提升。

活动上线后我们会持续盯着数据表现，如果某个活动的转化效果特别好我们会加大力度，效果不理想的我们也会及时调整策略。

您这边如果对方案有什么想法或者疑问，随时跟我们说，我们可以根据您的实际情况做微调。`;

    async function copyScript() {
        try {
            await navigator.clipboard.writeText(SCRIPT_TEXT);
            // 显示复制成功状态
            const copyStatus = document.getElementById('copyStatus');
            const copyText = document.getElementById('copyText');
            const copyIcon = document.getElementById('copyIcon');

            copyStatus.classList.remove('hidden');
            copyText.textContent = '已复制';
            copyIcon.textContent = '✓';

            // 2秒后恢复
            setTimeout(() => {
                copyStatus.classList.add('hidden');
                copyText.textContent = '点击复制';
                copyIcon.textContent = '📋';
            }, 2000);
        } catch (err) {
            console.error('复制失败:', err);
            alert('复制失败，请手动选择文字复制');
        }
    }

    // 页面加载时显示当前环境
    document.addEventListener('DOMContentLoaded', function() {
        const env = isTauriEnvironment() ? 'Tauri 桌面应用' : '浏览器';
        console.log('当前运行环境:', env);
    });
    </script>
</body>
</html>'''
