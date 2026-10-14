import { SignIn } from '@clerk/nextjs';
import { Suspense } from 'react';

export default function LogIn() {
  return (
    <Suspense fallback={<div>Loading...</div>}>
      <SignIn />
    </Suspense>
  );
}
