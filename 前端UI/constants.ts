import { Platform } from './types';

export interface PlatformInfo {
  id: Platform;
  label: string;
  description: string;
}

export const PLATFORMS: PlatformInfo[] = [
  { id: Platform.MEITUAN, label: '美团外卖', description: '美团平台活动配置' },
  { id: Platform.ELEME, label: '饿了么', description: '饿了么平台活动配置' },
  { id: Platform.BOTH, label: '双平台', description: '同时生成两套方案' },
];

export interface ActivitySection {
  platform: string;
  activities: { name: string; desc: string }[];
}

export const PLAN_SECTIONS: ActivitySection[] = [
  {
    platform: '饿了么平台活动',
    activities: [
      { name: '爆单红包', desc: '获取平台流量扶持' },
      { name: '减配送费', desc: '降低下单门槛' },
      { name: '优评返券', desc: '刺激顾客好评' },
      { name: '下单返券', desc: '促进二次消费' },
      { name: '集点返券', desc: '培养老客忠诚度' },
    ],
  },
  {
    platform: '美团平台活动',
    activities: [
      { name: '天天神券', desc: '获取平台流量扶持' },
      { name: '减配送费', desc: '降低下单门槛' },
      { name: '好评返券', desc: '刺激顾客好评' },
      { name: '下单返券', desc: '促进二次消费' },
      { name: '集点返券', desc: '培养老客忠诚度' },
    ],
  },
];
