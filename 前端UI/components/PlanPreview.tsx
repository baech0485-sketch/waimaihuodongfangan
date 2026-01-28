import React from 'react';
import { GeneratedPlan } from '../types';
import { Target, TrendingUp, Wallet, Users, LayoutDashboard } from 'lucide-react';

interface PlanPreviewProps {
  data: GeneratedPlan;
  id: string;
}

const PlanPreview: React.FC<PlanPreviewProps> = ({ data, id }) => {
  const { content } = data;

  return (
    <div id={id} className="bg-white text-slate-800 p-10 shadow-sm mx-auto w-full max-w-2xl min-h-[800px] relative">
      {/* Decorative top bar for the document */}
      <div className="h-2 w-20 bg-gradient-to-r from-primary-500 to-secondary-500 mb-8 rounded-full"></div>

      <div className="flex justify-between items-start mb-10">
        <div>
          <h1 className="text-2xl font-bold text-slate-900 mb-2">{content.title}</h1>
          <div className="flex items-center gap-3 text-sm text-slate-500">
            <span className="bg-slate-100 px-2 py-1 rounded text-slate-600 font-medium">
              {content.shopName}
            </span>
            <span>•</span>
            <span className="text-primary-600 font-medium">{content.platform}</span>
          </div>
        </div>
        <div className="text-right">
           <div className="text-xs font-mono text-slate-300">REF: {new Date().getTime().toString().slice(-6)}</div>
        </div>
      </div>

      {/* Summary Box */}
      <div className="bg-slate-50 border border-slate-100 rounded-xl p-6 mb-8">
        <h3 className="text-sm font-bold text-slate-400 uppercase tracking-wider mb-3 flex items-center gap-2">
          <LayoutDashboard size={14} /> 执行摘要
        </h3>
        <p className="text-slate-700 leading-relaxed text-sm">{content.summary}</p>
      </div>

      <div className="grid grid-cols-2 gap-8 mb-10">
        <div>
          <h3 className="text-sm font-bold text-slate-900 mb-4 flex items-center gap-2">
            <Users className="text-primary-500" size={16} /> 目标客群
          </h3>
          <div className="space-y-2">
            {content.targetAudience.map((tag, idx) => (
              <div key={idx} className="flex items-center gap-2 text-sm text-slate-600">
                <div className="w-1.5 h-1.5 rounded-full bg-secondary-500"></div>
                {tag}
              </div>
            ))}
          </div>
        </div>

        <div>
          <h3 className="text-sm font-bold text-slate-900 mb-4 flex items-center gap-2">
            <TrendingUp className="text-primary-500" size={16} /> 预期效果
          </h3>
          <p className="text-sm text-slate-600 bg-green-50 text-green-700 p-3 rounded-lg border border-green-100">
            {content.expectedOutcome}
          </p>
        </div>
      </div>

      <div className="mb-10">
        <h3 className="text-lg font-bold text-slate-900 mb-6 border-b border-slate-100 pb-2">
          核心策略
        </h3>
        <div className="space-y-6">
          {content.activities.map((activity, idx) => (
            <div key={idx} className="group">
              <div className="flex items-baseline justify-between mb-1">
                <h4 className="font-bold text-slate-800 flex items-center gap-2">
                  <span className="flex items-center justify-center w-5 h-5 rounded bg-slate-900 text-white text-xs">
                    {idx + 1}
                  </span>
                  {activity.name}
                </h4>
                {activity.discount && (
                  <span className="text-xs font-semibold text-primary-600 bg-primary-50 px-2 py-0.5 rounded-full">
                    {activity.discount}
                  </span>
                )}
              </div>
              <p className="text-sm text-slate-600 pl-7 leading-relaxed">
                {activity.description}
              </p>
            </div>
          ))}
        </div>
      </div>

      <div className="border-t border-slate-100 pt-6 flex items-start gap-3">
        <Wallet className="text-slate-400 mt-1" size={18} />
        <div>
          <span className="text-xs font-bold text-slate-400 uppercase tracking-wider block mb-1">预算预估</span>
          <span className="text-slate-800 font-medium">{content.budget}</span>
        </div>
      </div>

      <div className="absolute bottom-6 left-0 w-full text-center">
        <p className="text-[10px] text-slate-300 font-mono">POWERED BY CHENGSHANG INTELLIGENCE</p>
      </div>
    </div>
  );
};

export default PlanPreview;