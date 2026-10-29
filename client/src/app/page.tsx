import Hero from "@/components/shared/hero";

// eslint-disable-next-line @clerk/next/require-auth-protection
export default function Home() {
  return (
    <div className="w-full px-4 md:px-24 lg:px-32 xl:px-40 mx-auto h-full">
      <Hero />
    </div>
  );
}
