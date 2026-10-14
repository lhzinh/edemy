'use client';
import { Show, SignInButton, SignUpButton, UserButton } from '@clerk/nextjs';

export default function Header() {
  return (
    <header className="flex justify-end items-center p-4 gap-4 h-16">
      <Show when="signed-out">
        <SignInButton />
        <SignUpButton>
          <button className="bg-purple-700 text-white rounded-full font-medium text-sm sm:text-base h-10 sm:h-12 px-4 sm:px-5 cursor-pointer">
            Sign Up
          </button>
        </SignUpButton>
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
    </header>
  );
}
