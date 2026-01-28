import React from 'react';
import { Zap } from 'lucide-react';

const Header: React.FC = () => {
  return (
    <nav className="w-full bg-white/80 backdrop-blur-md border-b border-slate-200 sticky top-0 z-50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between items-center h-16">
          <div className="flex items-center gap-2">
            <div className="bg-gradient-to-br from-primary-500 to-secondary-500 text-white p-1.5 rounded-lg shadow-lg shadow-primary-500/30">
              <Zap size={20} fill="currentColor" />
            </div>
            <span className="font-bold text-xl tracking-tight text-slate-800">
              呈尚<span className="text-slate-400">策划</span>
            </span>
            <span className="hidden md:inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-primary-50 text-primary-700 ml-2">
              AI 驱动
            </span>
          </div>
          
          <div className="flex items-center gap-4">
             <a href="#" className="text-sm font-medium text-slate-500 hover:text-primary-600 transition-colors">帮助文档</a>
             <div className="h-4 w-px bg-slate-200"></div>
             <span className="text-sm text-slate-400">v2.0.0</span>
          </div>
        </div>
      </div>
    </nav>
  );
};

export default Header;