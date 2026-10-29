'use client';
import { Show, UserButton } from '@clerk/nextjs';
import { UserRound } from 'lucide-react';
import Link from 'next/link';
import { Suspense } from 'react';


export default function Header() {
  return (
    <header className="w-full relative z-20">
      <div className="px-4 md:px-24 lg:px-32 xl:px-40 w-full mx-auto">
        <nav className="relative flex items-center justify-between p-4 md:py-4 md:px-6 w-full">
          <Link href="/" className="text-2xl/3 font-bold">
            <span className="text-3xl italic">E</span>demy
          </Link>
          <div id="menu" className='max-md:-left-full max-md:fixed max-md:bg-black/70 max-md:backdrop-blur max-md:top-0 transition-all duration-300 max-md:h-screen max-md:w-full max-md:z-50 max-md:justify-center flex-col md:flex-row flex items-center gap-2 text-sm'>
            <a className="px-4 py-2  text-slate-100 hover:text-slate-200" href="#">Home</a>
            <a className="px-4 py-2 text-slate-100 hover:text-slate-200" href="#">Features</a>
            <a className="px-4 py-2 text-slate-100 hover:text-slate-200" href="#">Pricing</a>
            <a className="px-4 py-2 text-slate-100 hover:text-slate-200" href="#">Testimonial</a>
            <a className="px-4 py-2 text-slate-100 hover:text-slate-200" href="#">Blogs</a>
          </div>

          <button className="hidden md:flex bg-neutral-800 hover:bg-neutral-700 px-6 py-2.5 rounded-lg text-sm text-white transition cursor-pointer group">
            Get Started
          </button>

          <Suspense>
              <Show when="signed-out">
                <Link href="/sign-in">
                    <UserRound size={24} />
                </Link>
              </Show>
              <Show when="signed-in">
                <UserButton
                  appearance={{
                    elements: {
                      userButtonAvatarBox: 'size-8',
                    },
                  }}
                />
              </Show>
          </Suspense>
        </nav>
      </div>
    </header>
  );
}
