# Client

## End-to-end tests

Run the Playwright suite from this directory with `bun run e2e`. The config
starts the Next.js app and the Django development server on ports 3000 and 8000.
The server environment must include the Clerk development publishable and
secret keys; `NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY` is reused as
`CLERK_PUBLISHABLE_KEY` for the Clerk testing helper when needed. Set
`PLAYWRIGHT_BASE_URL` to override the Next.js test base URL.

The suite covers the signed-out dashboard redirect, rejection of an unsigned
Clerk webhook, and authentication on the Django user API.