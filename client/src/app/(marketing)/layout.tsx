import Header from '@/components/layout/header';

export default function Layout({ children }: LayoutProps<'/'>) {
  return (
    <>
      <Header />
      <main className="w-full flex-1">{children}</main>
    </>
  );
}
