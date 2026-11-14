import { Suspense } from 'react';
import Nav from "@/components/shared/nav";
import { getCategories } from "@/lib/data";

const Header = () => {
    const categories = getCategories();

    return (
        <header className="sticky top-0 h-16">
          <Suspense fallback={<div>Loading...</div>}>
            <Nav categories={categories} />
          </Suspense>
        </header>
    );
};

export default Header;
