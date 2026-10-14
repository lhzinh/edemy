import { resolve } from 'node:path';
import { defineConfig, devices } from '@playwright/test';

if (
  !process.env.CLERK_PUBLISHABLE_KEY &&
  process.env.NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY
) {
  process.env.CLERK_PUBLISHABLE_KEY =
    process.env.NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY;
}

const isCI = Boolean(process.env.CI);

export default defineConfig({
  testDir: './e2e',
  fullyParallel: true,
  forbidOnly: isCI,
  retries: isCI ? 2 : 0,
  workers: isCI ? 1 : undefined,
  reporter: 'list',
  use: {
    baseURL: process.env.PLAYWRIGHT_BASE_URL ?? 'http://127.0.0.1:3000',
    trace: 'retain-on-failure',
  },
  projects: [
    {
      name: 'setup',
      testMatch: /global\.setup\.ts/,
    },
    {
      name: 'chromium',
      testMatch: /.*\.spec\.ts/,
      dependencies: ['setup'],
      use: { ...devices['Desktop Chrome'] },
    },
  ],
  webServer: [
    {
      command: 'bun run dev -- --hostname 127.0.0.1',
      url: 'http://127.0.0.1:3000/sign-in/',
      reuseExistingServer: !isCI,
      timeout: 120_000,
    },
    {
      command: './.venv/bin/python manage.py runserver 127.0.0.1:8000',
      cwd: resolve(process.cwd(), '../server'),
      url: 'http://127.0.0.1:8000/admin/login/',
      reuseExistingServer: !isCI,
      timeout: 120_000,
    },
  ],
});
