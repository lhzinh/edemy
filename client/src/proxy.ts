import { clerkMiddleware } from '@clerk/nextjs/server';

export default clerkMiddleware(async (auth, req) => {
  // Important: This is not an auth guarantee, only
  // a performance optimization for signed-out users.
  const pathname = req.nextUrl.pathname
  if (pathname === '/dashboard' || pathname.startsWith('/dashboard/')) {
    const { isAuthenticated, redirectToSignIn } = await auth()

    if (!isAuthenticated) return redirectToSignIn()
  }
});

export const config = {
  matcher: [
    // Skip Next.js internals and all static files, unless found in search params
    '/((?!_next|[^?]*\\.(?:html?|css|js(?!on)|jpe?g|webp|png|gif|svg|ttf|woff2?|ico|csv|docx?|xlsx?|zip|webmanifest)).*)',
    // Always run for Clerk's auto-proxy path
    '/__clerk/:path*',
    // Always run for API routes
    '/(api|trpc)(.*)',
  ],
};