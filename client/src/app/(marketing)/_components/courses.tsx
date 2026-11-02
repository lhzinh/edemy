'use client'
import { use } from 'react'
import { CourseList } from '@/types'

export default function Courses({
  courses,
}: {
  courses: Promise<CourseList>
}) {
  const allCourses = use(courses)
  console.log(allCourses)

  return (
    <ul>
      {allCourses.results.map((course) => (
        <li key={course.slug}>{course.title}</li>
      ))}
    </ul>
  )
}