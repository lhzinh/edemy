export async function generateStaticParams() {
  const courses = await fetch('https://68d0ff25e6c0cbeb39a32bb1.mockapi.io/courses').then((res) => res.json())
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  return courses.map((post: any) => ({
    slug: post.slug,
  }))
}


export default async function Page({ params }: PageProps<"/explore/[slug]">) {
    const { slug } = await params;

    return (
        <div>
            <h1>Course: {slug}</h1>
            {/* <h1>{post.title}</h1>
            <p>{post.content}</p> */}
        </div>
    );
}
