export function Course({ name }: { name: string; }) {
    return (
        <ul>
            <li className='text-light'>{name}</li>
        </ul>
    );
}

export function CourseSkeleton() {
    return (
        <ul>
            <h1>XXXXX</h1>
        </ul>
    );
}