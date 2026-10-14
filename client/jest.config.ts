import type { Config } from 'jest'
import nextJest from 'next/jest.js'

const createJestConfig = nextJest({
  dir: './',
})

const config: Config = {
  clearMocks: true,
  testEnvironment: 'jsdom',
  setupFilesAfterEnv: ['<rootDir>/src/__tests__/jest.setup.ts'],
  // Map next-router-mock to the next/navigation module it mocks
  // Learn more - https://github.com/scottrippey/next-router-mock
  moduleNameMapper: {
    '^next/navigation$': 'next-router-mock',
  },
}

export default createJestConfig(config)