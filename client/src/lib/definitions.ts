export type Course = {
  id: string;
  slug: string;
  name: string;
  price: number;
  short_description: string;
};

export type ICourses = {
    per_page: number;
    count: number;
    results: Pick<Course, "slug" | "name" | "price" | "short_description">[]
}

export type Category = {
  id: string;
  slug: string;
  name: string;
};