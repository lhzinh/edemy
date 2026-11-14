import { Suspense } from "react";
import { CourseSkeleton } from "@/components/course";
import Courses from "@/components/courses";
import { getCourses } from "@/lib/data";

export default async function Page({
  searchParams,
}: {
  searchParams: Promise<{ [key: string]: string | string[] | undefined }>
}) {
    const { page = '1', category } = await searchParams 
    console.log(category)
    const courses = getCourses({
        category,
        page
    });

    return (
        <div>
            <Suspense fallback={<CourseSkeleton />}>
                <Courses courses={courses} />
            </Suspense>
        </div>
    );
}
