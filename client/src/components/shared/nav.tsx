"use client";
import { useQueryString } from "@/hooks/use-querystring";
import Link from "next/link";
import { use } from "react";

export default function Nav({
    categories,
}: {
    categories: Promise<{ slug: string; name: string }[]>;
}) {
    const data = use(categories);
    const { createQueryString } = useQueryString();

    return (
        <nav className='flex gap-2.5'>
            <Link href='/explore'>Explore</Link>
            <Link href='/guides'>Guides</Link>

            {data.map((category: { slug: string; name: string }) => (
                <Link
                    key={category.slug}
                    href={`/explore?${createQueryString("category", category.slug)}`}
                >
                    {category.name}
                </Link>
            ))}
        </nav>
    );
}
