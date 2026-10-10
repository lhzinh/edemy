import { auth } from '@clerk/nextjs/server';

export default async function Dashboard() {
  await auth.protect();

  return (
    <>
      <h1>Welcome to the dashboard</h1>
    </>
  );
}
