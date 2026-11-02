// export function generateStaticParams() {}
import { getCourse } from '@/lib/data';

export default async function Page({
  params,
}: PageProps<'/courses/[slug]'>) {
  const { slug } = await params
  const course = await getCourse(slug)

  return (
    <div className="w-full max-w-md mx-auto">
      <h1 className="text-3xl text-yellow-400">{course.title}</h1>
      <p>{course.description}</p>
    </div>
  )
}
