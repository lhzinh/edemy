import 'server-only'
import createClient from "openapi-fetch";
import type { paths } from "@/types/api";
import { endpoints } from "@/constants";

const client = createClient<paths>({ baseUrl: process.env.API_URL || 'http://localhost:8000' });

export async function getCourses() {
  const { data } = await client.GET(endpoints.COURSES, {
    next: { revalidate: 3600 },
  });
  return data
}


export async function getCourse(slug: string) {
  const { data } = await client.GET(endpoints.COURSE, {
    params: { path: { slug } },
    next: { revalidate: 3600 },
  });
  return data
}