import React from 'react';
import { Platform } from '../types';
import { ShoppingBag, ShoppingCart, Layers } from 'lucide-react';

interface PlatformSelectorProps {
  selected: Platform;
  onChange: (p: Platform) => void;
}

const PlatformSelector: React.FC<PlatformSelectorProps> = ({ selected, onChange }) => {
  
  const options = [
    { id: Platform.MEITUAN, label: '美团外卖', icon: ShoppingBag, color: 'text-yellow-500' },
    { id: Platform.ELEME, label: '饿了么', icon: ShoppingCart, color: 'text-blue-500' },
    { id: Platform.BOTH, label: '双平台', icon: Layers, color: 'text-indigo-500' },
  ];

  return (
    <div className="grid grid-cols-1 sm:grid-cols-3 gap-3 w-full">
      {options.map((opt) => {
        const isSelected = selected === opt.id;
        const Icon = opt.icon;
        
        return (
          <div
            key={opt.id}
            onClick={() => onChange(opt.id)}
            className={`
              relative group cursor-pointer rounded-xl p-4 border transition-all duration-300
              flex flex-col items-center justify-center gap-2
              ${isSelected 
                ? 'bg-white border-primary-500 shadow-lg shadow-primary-500/10' 
                : 'bg-slate-50 border-slate-200 hover:border-slate-300 hover:bg-white'}
            `}
          >
            {/* Active Indicator Dot */}
            {isSelected && (
              <div className="absolute top-2 right-2 w-2 h-2 rounded-full bg-primary-500 animate-pulse" />
            )}

            <div className={`
              p-2.5 rounded-lg transition-colors duration-300
              ${isSelected ? 'bg-primary-50' : 'bg-white shadow-sm'}
            `}>
              <Icon size={20} className={isSelected ? opt.color : 'text-slate-400'} />
            </div>
            
            <span className={`font-semibold text-sm ${isSelected ? 'text-slate-800' : 'text-slate-500'}`}>
              {opt.label}
            </span>
          </div>
        );
      })}
    </div>
  );
};

export default PlatformSelector;