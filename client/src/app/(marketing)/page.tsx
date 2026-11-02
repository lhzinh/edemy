import { Suspense } from 'react';
import { getCourses } from '@/lib/data';
import Hero from './_components/hero';
import Courses from './_components/courses';

export default function Home() {
  const coursesPromise = getCourses().then(
    data => data ?? { count: 0, results: [] }
  );

  return (
    <>
      <Hero />
      <Suspense fallback={<div>Loading...</div>}>
        <Courses courses={coursesPromise} />
      </Suspense>
    </>
  );
}
