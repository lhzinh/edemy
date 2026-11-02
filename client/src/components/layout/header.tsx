'use client';
import { Show, UserButton } from '@clerk/nextjs';
import { UserRound } from 'lucide-react';
import Link from 'next/link';
import Image from 'next/image';
import React, { Suspense } from 'react';
import { cn } from '@/lib/utils';
import { TextAlignJustify } from 'lucide-react';
import {
  NavigationMenu,
  NavigationMenuContent,
  NavigationMenuItem,
  NavigationMenuLink,
  NavigationMenuList,
  NavigationMenuTrigger,
  NavigationMenuItemLink,
} from '@/components/ui/navigation-menu';
import { ThemeToggle } from '@/components/layout/theme-toggle';
import { Button } from '@/components/ui/button';
import {
  Sheet,
  SheetClose,
  SheetContent,
  SheetDescription,
  SheetFooter,
  SheetHeader,
  SheetTitle,
  SheetTrigger,
} from '@/components/ui/sheet';

export default function Header() {
  const courses: { title: string; href: string; description: string }[] = [
    {
      title: 'HTML',
      href: '/courses/html',
      description:
        'Learn the structure of the web: tags, forms, tables and semantic markup.',
    },
    {
      title: 'CSS',
      href: '/courses/css',
      description:
        'Style your pages with selectors, Flexbox, Grid and responsive design.',
    },
    {
      title: 'JavaScript',
      href: '/courses/javascript',
      description:
        'Master variables, functions, DOM manipulation and asynchronous code.',
    },
    {
      title: 'TypeScript',
      href: '/courses/typescript',
      description:
        'Add static types to JavaScript and catch bugs before they reach production.',
    },
    {
      title: 'React',
      href: '/courses/react',
      description:
        'Build interactive UIs with components, hooks and state management.',
    },
    {
      title: 'Python',
      href: '/courses/python',
      description:
        'Start programming with clear syntax, data structures and real mini projects.',
    },
  ];

  return (
    <header className="flex flex-col items-center w-full">
      <nav className="flex items-center justify-between p-4 md:px-16 lg:px-24 xl:px-32 md:py-4 w-full relative">
        <Link href="/">
          <Image
            src={'./logo.svg'}
            alt="Edemy logo"
            width={157}
            height={40}
            className="w-25 h-auto"
            priority
          />
        </Link>

        <NavigationMenu id="menu">
          <NavigationMenuList className="hidden md:flex lg:gap-8 md:gap-2">
            <NavigationMenuItem className="hidden md:flex">
              <NavigationMenuTrigger>Courses</NavigationMenuTrigger>
              <NavigationMenuContent>
                <ul className="grid gap-2 md:grid-cols-2 sm:w-100 md:w-125 lg:w-150">
                  {courses.map((course) => (
                    <ListItem
                      key={course.title}
                      title={course.title}
                      href={course.href}
                      className="p-2 hover:bg-accent rounded-xl cursor-pointer"
                    >
                      {course.description}
                    </ListItem>
                  ))}
                </ul>
              </NavigationMenuContent>
            </NavigationMenuItem>
            <NavigationMenuItemLink href="/projects">
              Projects
            </NavigationMenuItemLink>
            <NavigationMenuItemLink href="/pricing">
              Pricing
            </NavigationMenuItemLink>
            <NavigationMenuItemLink href="/contact">
              Contact Us
            </NavigationMenuItemLink>
          </NavigationMenuList>
        </NavigationMenu>

        <div className="flex items-center space-x-4">
          <ThemeToggle />
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
          <MobileMenu />
        </div>
      </nav>
    </header>
  );
}

function MobileMenu() {
  return (
    <Sheet>
      <SheetTrigger
        render={
          <Button
            id="openMenu"
            variant="outline"
            size="icon"
            aria-label="Open Menu"
            className="md:hidden"
          >
            <TextAlignJustify />
          </Button>
        }
      />
      <SheetContent>
        <SheetHeader>
          <SheetTitle className="text-yellow-400">Menu</SheetTitle>
          <SheetDescription>
            Make changes to your profile here. Click save when you&apos;re done.
          </SheetDescription>
        </SheetHeader>
        <nav className="flex flex-col gap-6 px-4">
          <Link href={'/'}>Courses</Link>
          <Link href={'/'}>Projects</Link>
          <Link href={'/'}>Pricing</Link>
          <Link href={'/'}>Contact Us</Link>
        </nav>
      </SheetContent>
    </Sheet>
  );
}

function ListItem({
  title,
  children,
  href,
  ...props
}: React.ComponentPropsWithoutRef<'li'> & { href: string }) {
  return (
    <li {...props}>
      <NavigationMenuLink
        render={
          <Link href={href}>
            <div className="flex flex-col gap-2 text-sm">
              <div className="leading-none font-medium text-base font-heading text-yellow-400">
                {title}
              </div>
              <div className="line-clamp-2 text-muted-foreground text-xs">
                {children}
              </div>
            </div>
          </Link>
        }
      />
    </li>
  );
}
