import { Platform } from '../types';

const API_BASE_URL = import.meta.env.VITE_API_URL || '';

export const downloadPDF = async (storeName: string, platform: Platform) => {
  try {
    const response = await fetch(`${API_BASE_URL}/api/generate`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        store_name: storeName,
        platform: platform,
      }),
    });

    if (!response.ok) {
      throw new Error('PDF生成失败');
    }

    // 获取文件名
    const contentDisposition = response.headers.get('content-disposition');
    let filename = `${storeName}_活动方案.pdf`;
    if (contentDisposition) {
      const match = contentDisposition.match(/filename\*?=(?:UTF-8'')?([^;]+)/i);
      if (match) {
        filename = decodeURIComponent(match[1].replace(/['"]/g, ''));
      }
    }

    // 下载文件
    const blob = await response.blob();
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = filename;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    window.URL.revokeObjectURL(url);
  } catch (error) {
    console.error("PDF generation failed", error);
    alert("PDF下载失败，请重试。");
  }
};
