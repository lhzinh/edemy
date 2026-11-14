import Header from "@/components/shared/header";

export default function MarketingLayout({
  children,
}: LayoutProps<"/">) {
  return (
    <>
        <Header />
        <main>{children}</main>
    </>
  )
}