import React from 'react';
import { AlertCircle, CheckCircle2 } from 'lucide-react';

interface StatusMessageProps {
  type: 'error' | 'success';
  children: React.ReactNode;
}

const STYLES = {
  error: {
    container: 'border-red-200 bg-red-50 text-red-700',
    Icon: AlertCircle,
  },
  success: {
    container: 'border-emerald-200 bg-emerald-50 text-emerald-700',
    Icon: CheckCircle2,
  },
} as const;

const StatusMessage: React.FC<StatusMessageProps> = ({ type, children }) => {
  const { container, Icon } = STYLES[type];

  return (
    <div
      role={type === 'error' ? 'alert' : 'status'}
      className={`flex items-start gap-2.5 rounded-lg border p-3 text-sm ${container}`}
    >
      <Icon size={16} className="mt-0.5 shrink-0" />
      <span>{children}</span>
    </div>
  );
};

export default StatusMessage;
