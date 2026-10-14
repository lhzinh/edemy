import { SignUp } from '@clerk/nextjs';
import { Suspense } from 'react';

export default function Register() {
  return (
    <Suspense fallback={<div>Loading...</div>}>
      <SignUp />
    </Suspense>
  );
}
