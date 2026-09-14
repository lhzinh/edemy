# Edemy

AI-first e-learning SaaS platform. The monorepo contains a Next.js frontend,
Django REST backend, Expo mobile app, and Hardhat web3 app.

## AI Coding Workflow

Follow this sequence for every implementation task:

1. **Specify (SPD)**: Restate the requested behavior, identify the affected
   service and owning abstraction, and define acceptance criteria.
2. **Generate Code**: Read the nearest implementation, tests, and local
   instructions before editing. Prefer the smallest focused change.
3. **TDD**: Add or update a focused failing test first when the behavior is
   testable. Implement the change, then make the test pass. Cover negative and
   boundary cases for validation, permissions, errors, and empty states.
4. **BDD**: Describe user-visible and API behavior as Given/When/Then scenarios.
   Turn important scenarios into automated tests where practical.
5. **Lint and Format**: Run the local pre-push checks before pushing. Fix the
   source; do not disable rules globally to hide failures.
6. **CI**: Push only after local checks pass. GitHub Actions builds production
   Docker images and publishes them to GHCR on `main` or `v*` tags.
7. **Fix / Finalize**: Reproduce CI failures locally, fix the root cause, rerun
   the failing check, and repeat until all required gates pass. Report changed
   files, validation results, and remaining pre-existing failures.

### Definition of Done

- Acceptance criteria and relevant Given/When/Then scenarios are covered.
- Tests were written or updated before implementation when behavior changed.
- No secrets, generated artifacts, unrelated refactors, or placeholder TODOs
  were introduced.
- Local pre-push checks pass.
- Relevant typecheck, unit, integration, build, and migration checks pass.
- Production Docker images build successfully when deployment behavior changes.
- The final response lists validation commands and known residual risks.

### Failure Handling

- Read the complete error and identify the owning layer before editing.
- Preserve user changes in a dirty worktree; never reset or checkout unrelated
  files.
- Do not weaken tests, permissions, security settings, or lint rules to pass a
  gate.
- After each fix, rerun the narrowest failing command, then the full required
  verification order.

## Monorepo Layout

```text
/client   -> Next.js 16, App Router, React 19, Bun, Clerk
/server   -> Django 6.1, DRF, Python 3.14, uv, PostgreSQL
/mobile   -> Expo SDK 57, React Native 0.86
/web3     -> Hardhat 3, blockchain NFT and token apps
```

Read the relevant sub-project `AGENTS.md` before editing code there.

## Infrastructure

- Docker Compose (`compose.yaml`) orchestrates local services.
- Inngest runs on ports 8288/8289 and connects to Django at
  `http://server:8000/api/inngest`.
- Clerk handles frontend auth, backend JWT verification, and webhook sync.
- Never commit secrets. Server secrets are loaded from environment files or
  `server/deploy/SECRET`.

## Commands

### Root

```bash
make up              # Start all services
make down            # Stop all services
make watch           # Watch and hot reload
make build           # Rebuild all images
make lint            # Lint backend and frontend through Compose
make test            # Run server pytest
make test-e2e        # Run Playwright E2E tests
make migrate         # Apply Django migrations
make makemigrations  # Generate Django migrations
make shell           # Open Django shell
make logs            # View server logs
make setup-hooks     # Enable the tracked Git pre-push hook
```

Run `make setup-hooks` once after cloning. The tracked `.githooks/pre-push`
script runs client ESLint and server Ruff checks before every push.

### Client

```bash
cd client
bun run dev
bun run lint
bun run lint --fix
bun x tsc --noEmit
bun run test
bun run build
```

### Server

```bash
cd server
uv run python manage.py runserver
uv run ruff check . --fix
uv run ruff format
uv run ruff format --check
uv run pyright
uv run pytest
```

### Mobile

```bash
cd mobile
npx expo start
npx expo lint
npx tsc --noEmit
```

## Verification Order

Run the narrowest relevant check first, then use the complete order:

**Client**: `bun run lint --fix` -> `bun x tsc --noEmit` -> `bun run test` -> `bun run build`

**Server**: `uv run ruff check . --fix` -> `uv run ruff format` -> `uv run pyright` -> `uv run pytest`

**Pre-push**: `make setup-hooks` once, then `.githooks/pre-push`

**Docker**: `docker compose -f compose.prod.yaml config --quiet` and
`docker compose -f compose.prod.yaml build`

## Architecture Notes

- Django apps live in `server/apps/`; business logic belongs in
  `services.py` and `selectors.py`, not views or serializers.
- Shared server mixins live in `server/libs/mixins/`.
- Django settings are split into `base.py`, `local.py`, `testing.py`, and
  `production.py`.
- Tests use SQLite in-memory databases, disabled migrations, and
  `core.settings.testing` from `pytest.ini`.
- Inngest handlers should keep pure `_handle_*` functions testable without the
  SDK.
- API versioning is URL-path based (`/v1/`, `/v2/`), with v1 as default.
- Client route groups are `(auth)` and `(dashboard)`.
- Client providers are Clerk, React Query, and ThemeProvider.
- Client path alias `@/*` maps to `./src/*`; standalone output is enabled.
- The existing `apps/urls.py` import of `accounts.webhooks.clerk_webhook` may
  be unavailable; verify before assuming URL imports work.

## Conventions

- Use squash merges and Conventional Commits: `feat:`, `fix:`, `chore:`,
  `docs:`. Branches use `type/short-description`.
- Python requires type hints, no `Any`, early returns, and explicit DRF
  permissions.
- TypeScript uses functional components, named exports, `const`, and Zod for
  validation.
- Do not create `ios/` or `android/` directories manually for Expo.
- Propose schema changes and rollback steps before creating or executing Django
  migrations.
- Ask before installing third-party dependencies; prefer existing or built-in
  tools.
- Update documentation, API contracts, and runbooks when behavior,
  configuration, or deployment changes.

## Sub-project Instructions

- `client/AGENTS.md` - Client style, security, error handling, and Next.js rules
- `server/AGENTS.md` - Server style, DRF patterns, security, and migrations
- `mobile/AGENTS.md` - Expo conventions and EAS build rules
- `web3/AGENTS.md` - Blockchain, NFT, and dapp conventions