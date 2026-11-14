import "server-only";
import { Category, ICourses } from "./definitions";
import query from "./queries";

export async function getData<T>(
    endpoint: string,
    params?: string,
    tag?: string,
): Promise<T> {
    const res = await fetch(
        `${process.env.API_URL}/${endpoint}/${params ? `?${params}` : ""}`,
        {
            next: { revalidate: 60, tags: [tag ?? endpoint] },
        },
    );

    if (!res.ok) {
        throw new Error(`API error: ${res.status} ${res.statusText}`);
    }

    return res.json();
}

export async function getCategories() {
    return getData<Category[]>(
        "categories",
        "fields=slug,name",
        "categories",
    );
}

export async function getCourses(params?: { [key: string]: string | string[] | undefined }) {
    const queryString = params ? query(params) : "";

    return getData<ICourses>(
        "courses",
        queryString,
        "courses",
    );
}