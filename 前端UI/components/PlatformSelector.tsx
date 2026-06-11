import React from 'react';
import { Platform } from '../types';
import { PLATFORMS } from '../constants';
import { Check } from 'lucide-react';

interface PlatformSelectorProps {
  selected: Platform;
  onChange: (p: Platform) => void;
}

const PlatformSelector: React.FC<PlatformSelectorProps> = ({ selected, onChange }) => {
  return (
    <div
      role="radiogroup"
      aria-label="目标平台"
      className="grid grid-cols-1 gap-3 sm:grid-cols-3"
    >
      {PLATFORMS.map((opt) => {
        const isSelected = selected === opt.id;

        return (
          <button
            key={opt.id}
            type="button"
            role="radio"
            aria-checked={isSelected}
            onClick={() => onChange(opt.id)}
            className={`relative flex flex-col items-start gap-1 rounded-lg border p-4 text-left transition-colors focus:outline-none focus-visible:ring-2 focus-visible:ring-foreground/20 ${
              isSelected
                ? 'border-foreground bg-subtle'
                : 'border-border bg-background hover:border-foreground/40'
            }`}
          >
            {isSelected && (
              <span className="absolute right-3 top-3 flex h-4 w-4 items-center justify-center rounded-full bg-foreground text-background">
                <Check size={11} strokeWidth={3} />
              </span>
            )}
            <span className="text-sm font-semibold text-foreground">{opt.label}</span>
            <span className="text-xs text-muted">{opt.description}</span>
          </button>
        );
      })}
    </div>
  );
};

export default PlatformSelector;
