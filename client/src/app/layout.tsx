import type { Metadata } from 'next';
import {
  Nunito,
  JetBrains_Mono,
  Jersey_10
} from 'next/font/google';

import '@/styles/globals.css';
import { cn } from '@/lib/utils';
import Providers from '@/providers';

const body = Nunito({
  variable: '--font-nunito',
  subsets: ['latin', 'vietnamese'],
});

const heading = Jersey_10({
  subsets: ['latin'],
  variable: '--font-jersey-10',
  weight: ["400"]
});

const mono = JetBrains_Mono({
  subsets: ['latin', 'vietnamese'],
  variable: '--font-jetbrains-mono',
});

export const metadata: Metadata = {
  title: 'Edemy',
  description: 'Game start, clear levels now',
};

export default function RootLayout({ children }: LayoutProps<'/'>) {
  return (
    <html
      lang="en"
      suppressHydrationWarning
      className={cn(
        'h-full',
        'antialiased',
        body.variable,
        heading.variable,
        mono.variable,
      )}
    >
      <body suppressHydrationWarning className="h-full">
        <Providers>
          {children}
        </Providers>
      </body>
    </html>
  );
}
