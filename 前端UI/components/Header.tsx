import React from 'react';

const Header: React.FC = () => {
  return (
    <header className="sticky top-0 z-50 w-full border-b border-border bg-background/80 backdrop-blur-md">
      <div className="mx-auto flex h-16 max-w-5xl items-center justify-between px-4 sm:px-6 lg:px-8">
        <div className="flex items-center gap-2.5">
          <div className="flex h-7 w-7 items-center justify-center rounded-md bg-foreground text-background">
            {/* Vercel-style triangle mark */}
            <svg viewBox="0 0 24 24" width="14" height="14" fill="currentColor" aria-hidden="true">
              <path d="M12 3 22 20H2L12 3Z" />
            </svg>
          </div>
          <span className="text-[15px] font-semibold tracking-tight text-foreground">
            呈尚策划
          </span>
          <span className="hidden items-center rounded-full border border-border px-2 py-0.5 text-xs font-medium text-muted sm:inline-flex">
            活动方案引擎
          </span>
        </div>

        <nav className="flex items-center gap-5">
          <a
            href="#plan-content"
            className="text-sm font-medium text-muted transition-colors hover:text-foreground"
          >
            方案说明
          </a>
          <span className="font-mono text-xs text-muted">v2.0.0</span>
        </nav>
      </div>
    </header>
  );
};

export default Header;
