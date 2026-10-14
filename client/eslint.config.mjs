import { defineConfig, globalIgnores } from 'eslint/config';
import nextVitals from 'eslint-config-next/core-web-vitals';
import nextTs from 'eslint-config-next/typescript';
import prettier from 'eslint-config-prettier/flat';
import clerkNext from '@clerk/eslint-plugin/next'

const eslintConfig = defineConfig([
  ...nextVitals,
  ...nextTs,
  prettier,
  // Override default ignores of eslint-config-next.
  globalIgnores([
    // Default ignores of eslint-config-next:
    '.next/**',
    'out/**',
    'build/**',
    'next-env.d.ts',
  ]),
  {
    plugins: { '@clerk/next': clerkNext },
    rules: {
      '@clerk/next/require-auth-protection': [
        'error',
        {
          protected: ['**'],
          public: ['src/app/page.tsx', 'src/app/(auth)/sign-in/**', 'src/app/(auth)/sign-up/**'],
        },
      ],
    },
  },
]);

export default eslintConfig;
