import React, { useState } from 'react';
import { Loader2, Download } from 'lucide-react';
import { Platform } from '../types';
import { downloadPDF } from '../services/pdfService';
import PlatformSelector from './PlatformSelector';
import StatusMessage from './StatusMessage';

const GeneratorForm: React.FC = () => {
  const [shopName, setShopName] = useState('');
  const [platform, setPlatform] = useState<Platform>(Platform.MEITUAN);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [success, setSuccess] = useState(false);

  const isDisabled = isLoading || !shopName.trim();

  const handleGenerate = async () => {
    if (!shopName.trim()) {
      setError('请输入店铺名称');
      return;
    }

    setIsLoading(true);
    setError(null);
    setSuccess(false);

    try {
      await downloadPDF(shopName, platform);
      setSuccess(true);
    } catch (err: any) {
      setError(err?.message || '生成失败，请重试');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <section className="rounded-xl border border-border bg-background p-6">
      <h2 className="text-base font-semibold text-foreground">创建方案</h2>
      <p className="mt-1 text-sm text-muted">填写店铺信息，一键生成专业活动方案 PDF。</p>

      <div className="mt-6 space-y-6">
        <div>
          <label htmlFor="shopName" className="mb-2 block text-sm font-medium text-foreground">
            店铺名称
          </label>
          <input
            id="shopName"
            type="text"
            value={shopName}
            onChange={(e) => {
              setShopName(e.target.value);
              if (error) setError(null);
            }}
            placeholder="例如：霸王茶姬（春熙路店）"
            className="w-full rounded-lg border border-border bg-background px-3.5 py-2.5 text-sm text-foreground placeholder-muted transition-colors focus:border-foreground focus:outline-none focus:ring-2 focus:ring-foreground/10"
          />
        </div>

        <div>
          <span className="mb-3 block text-sm font-medium text-foreground">目标平台</span>
          <PlatformSelector selected={platform} onChange={setPlatform} />
        </div>

        {error && <StatusMessage type="error">{error}</StatusMessage>}
        {success && <StatusMessage type="success">PDF 已生成并开始下载</StatusMessage>}

        <button
          type="button"
          onClick={handleGenerate}
          disabled={isDisabled}
          className={`flex w-full items-center justify-center gap-2 rounded-lg px-4 py-2.5 text-sm font-medium transition-colors ${
            isDisabled
              ? 'cursor-not-allowed bg-subtle text-muted'
              : 'bg-foreground text-background hover:bg-foreground/90'
          }`}
        >
          {isLoading ? (
            <>
              <Loader2 className="animate-spin" size={16} />
              正在生成 PDF...
            </>
          ) : (
            <>
              <Download size={16} />
              生成并下载 PDF
            </>
          )}
        </button>
      </div>
    </section>
  );
};

export default GeneratorForm;
