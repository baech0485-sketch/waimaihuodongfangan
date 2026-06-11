import React from 'react';
import Header from './components/Header';
import GeneratorForm from './components/GeneratorForm';
import PlanContent from './components/PlanContent';

const App: React.FC = () => {
  return (
    <div className="flex min-h-screen flex-col bg-background font-sans text-foreground">
      <Header />

      <main className="mx-auto w-full max-w-5xl flex-grow px-4 py-12 sm:px-6 lg:px-8">
        <div className="max-w-2xl">
          <h1 className="text-2xl font-semibold tracking-tight text-balance sm:text-3xl">
            外卖活动方案生成器
          </h1>
          <p className="mt-3 text-pretty text-muted">
            输入店铺名称并选择目标平台，即可生成符合美团 / 饿了么运营策略的专业活动方案 PDF。
          </p>
        </div>

        <div className="mt-10 grid gap-6 lg:grid-cols-2">
          <GeneratorForm />
          <PlanContent />
        </div>
      </main>

      <footer className="border-t border-border">
        <div className="mx-auto flex max-w-5xl flex-col items-center justify-between gap-2 px-4 py-6 text-sm text-muted sm:flex-row sm:px-6 lg:px-8">
          <span>呈尚策划 · 活动方案引擎</span>
          <span className="font-mono text-xs">POWERED BY CHENGSHANG INTELLIGENCE</span>
        </div>
      </footer>
    </div>
  );
};

export default App;
