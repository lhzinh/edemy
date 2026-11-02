import Link from 'next/link';
import { getCourses } from '@/lib/data';


export default async function Page() {
  const { results: courses } = await getCourses();
  console.log(courses);

  return (
    <ul>
      {courses?.map((course: { slug: string; title: string }) => (
        <li key={course.slug}>
          <Link href={`/courses/${course.slug}`}>{course.title}</Link>
        </li>
      ))}
    </ul>
  );
}
