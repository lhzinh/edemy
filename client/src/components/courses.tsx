"use client"
import { use } from "react";
import { Course } from "./course";
import { ICourses } from "@/lib/definitions";

export default function Courses({
    courses,
}: {
    courses: Promise<ICourses>;
}) {
    const { results } = use(courses)

    return (
        <>
            {results.map((course: {slug: string; name: string}) => (
                <Course key={course.slug} {...course} />
            ))}
        </>
    );
}