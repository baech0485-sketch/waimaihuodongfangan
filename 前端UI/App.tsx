import React, { useState } from 'react';
import Header from './components/Header';
import PlatformSelector from './components/PlatformSelector';
import { Platform } from './types';
import { downloadPDF } from './services/pdfService';
import { Loader2, Download, Wand2 } from 'lucide-react';

const App: React.FC = () => {
  const [shopName, setShopName] = useState('');
  const [platform, setPlatform] = useState<Platform>(Platform.MEITUAN);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [success, setSuccess] = useState(false);

  const handleGenerate = async () => {
    if (!shopName.trim()) {
      setError("请输入店铺名称");
      return;
    }

    setIsLoading(true);
    setError(null);
    setSuccess(false);

    try {
      await downloadPDF(shopName, platform);
      setSuccess(true);
    } catch (err: any) {
      setError(err.message || "生成失败，请重试");
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-slate-50 flex flex-col font-sans text-slate-900 selection:bg-primary-100 selection:text-primary-700">
      <Header />

      <main className="flex-grow max-w-7xl mx-auto w-full px-4 sm:px-6 lg:px-8 py-8">
        
        <div className="grid lg:grid-cols-12 gap-8 h-full">
          
          {/* LEFT COLUMN: Controls */}
          <div className="lg:col-span-5 space-y-6">
            <div className="bg-white rounded-2xl p-6 shadow-sm border border-slate-200">
              <h2 className="text-lg font-bold text-slate-800 mb-1 flex items-center gap-2">
                <Wand2 className="text-primary-500" size={20} />
                创建方案
              </h2>
              <p className="text-slate-500 text-sm mb-6">填写店铺信息，一键生成专业活动方案PDF。</p>
              
              <div className="space-y-6">
                {/* Shop Name */}
                <div className="group">
                  <label htmlFor="shopName" className="block text-sm font-medium text-slate-700 mb-2">
                    店铺名称
                  </label>
                  <div className="relative">
                    <input
                      id="shopName"
                      type="text"
                      value={shopName}
                      onChange={(e) => {
                        setShopName(e.target.value);
                        if (error) setError(null);
                      }}
                      placeholder="例如：霸王茶姬（春熙路店）"
                      className="w-full px-4 py-3 bg-slate-50 border border-slate-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-primary-500/20 focus:border-primary-500 transition-all text-slate-800 placeholder-slate-400"
                    />
                  </div>
                </div>

                {/* Platform */}
                <div>
                  <label className="block text-sm font-medium text-slate-700 mb-3">
                    目标平台
                  </label>
                  <PlatformSelector selected={platform} onChange={setPlatform} />
                </div>

                {/* Error */}
                {error && (
                  <div className="p-4 rounded-xl bg-red-50 text-red-600 text-sm border border-red-100 animate-pulse">
                    ⚠️ {error}
                  </div>
                )}

                {/* Success */}
                {success && (
                  <div className="p-4 rounded-xl bg-green-50 text-green-600 text-sm border border-green-100">
                    ✅ PDF已生成并开始下载
                  </div>
                )}

                {/* Generate Button */}
                <button
                  onClick={handleGenerate}
                  disabled={isLoading || !shopName.trim()}
                  className={`
                    w-full py-3.5 rounded-xl font-semibold text-white shadow-lg shadow-primary-500/20
                    transition-all duration-300 transform active:scale-[0.98]
                    flex items-center justify-center gap-2 relative overflow-hidden
                    ${isLoading || !shopName.trim()
                      ? 'bg-slate-300 cursor-not-allowed shadow-none'
                      : 'bg-gradient-to-r from-primary-600 to-secondary-500 hover:brightness-110'}
                  `}
                >
                  {isLoading ? (
                    <>
                      <Loader2 className="animate-spin" size={20} />
                      正在生成PDF...
                    </>
                  ) : (
                    <>
                      <Download size={20} />
                      生成并下载PDF
                    </>
                  )}
                </button>
              </div>
            </div>

            {/* Informational Card (only visible on large screens) */}
            <div className="hidden lg:block bg-gradient-to-br from-slate-900 to-slate-800 rounded-2xl p-6 text-white shadow-xl relative overflow-hidden">
               <div className="relative z-10">
                 <h3 className="font-bold text-lg mb-2">专业提示</h3>
                 <p className="text-slate-300 text-sm leading-relaxed">
                   活动方案基于美团/饿了么平台最佳实践配置，包含爆单红包、减配送费、返券活动等完整策略。
                 </p>
               </div>
               <Download className="absolute -bottom-4 -right-4 text-slate-700 opacity-20 w-32 h-32" />
            </div>
          </div>

          {/* RIGHT COLUMN: Info */}
          <div className="lg:col-span-7">
            <div className="bg-white rounded-2xl p-6 shadow-sm border border-slate-200">
              <h2 className="text-lg font-bold text-slate-800 mb-4">方案内容说明</h2>
              <div className="space-y-4 text-sm text-slate-600">
                <div>
                  <h3 className="font-semibold text-slate-800 mb-2">饿了么平台活动</h3>
                  <ul className="list-disc list-inside space-y-1">
                    <li>爆单红包 - 获取平台流量扶持</li>
                    <li>减配送费 - 降低下单门槛</li>
                    <li>优评返券 - 刺激顾客好评</li>
                    <li>下单返券 - 促进二次消费</li>
                    <li>集点返券 - 培养老客忠诚度</li>
                  </ul>
                </div>
                <div>
                  <h3 className="font-semibold text-slate-800 mb-2">美团平台活动</h3>
                  <ul className="list-disc list-inside space-y-1">
                    <li>天天神券 - 获取平台流量扶持</li>
                    <li>减配送费 - 降低下单门槛</li>
                    <li>好评返券 - 刺激顾客好评</li>
                    <li>下单返券 - 促进二次消费</li>
                    <li>集点返券 - 培养老客忠诚度</li>
                  </ul>
                </div>
              </div>
            </div>
          </div>

        </div>
      </main>
    </div>
  );
};

export default App;