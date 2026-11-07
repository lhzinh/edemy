import Link from 'next/link'

export default function Home() {
  return (
    <div>
      <h1>Welcome to Edemy!</h1>
      <Link href="/guides">Guides</Link>
    </div>
  );
}
