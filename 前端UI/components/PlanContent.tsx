import React from 'react';
import { PLAN_SECTIONS } from '../constants';

const PlanContent: React.FC = () => {
  return (
    <section
      id="plan-content"
      className="rounded-xl border border-border bg-background p-6"
    >
      <h2 className="text-base font-semibold text-foreground">方案内容说明</h2>
      <p className="mt-1 text-sm text-muted">
        基于平台最佳实践配置，覆盖引流、转化与复购的完整策略。
      </p>

      <div className="mt-6 grid gap-6 sm:grid-cols-2">
        {PLAN_SECTIONS.map((section) => (
          <div key={section.platform}>
            <h3 className="mb-3 text-sm font-semibold text-foreground">
              {section.platform}
            </h3>
            <ul className="space-y-2.5">
              {section.activities.map((activity) => (
                <li key={activity.name} className="flex items-baseline gap-2 text-sm">
                  <span className="font-medium text-foreground">{activity.name}</span>
                  <span className="text-muted">·</span>
                  <span className="text-muted">{activity.desc}</span>
                </li>
              ))}
            </ul>
          </div>
        ))}
      </div>
    </section>
  );
};

export default PlanContent;
