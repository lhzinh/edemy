import {
  Card,
  CardAction,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { Skeleton } from '@/components/ui/skeleton';
import { Badge } from '@/components/ui/badge';

function CourseSkeleton() {
  return (
    <Card className="w-full max-w-xs">
      <CardHeader>
        <CardAction>
          <Skeleton className="h-4 w-2/3" />
        </CardAction>
        <CardTitle>
          <Skeleton className="h-4 w-1/2" />
        </CardTitle>
        <CardDescription>
          <Skeleton className="aspect-video w-full" />
        </CardDescription>
      </CardHeader>
      <CardFooter>
        <Skeleton className="aspect-video w-full" />
      </CardFooter>
    </Card>
  );
}

function Course() {
  return (
    <Card className="w-full max-w-xs">
      <CardHeader>
        <CardAction>
          <Badge variant="secondary">Featured</Badge>
        </CardAction>
        <CardTitle>Design systems meetup</CardTitle>
        <CardDescription>
          A practical talk on component APIs, accessibility, and shipping
          faster.
        </CardDescription>
      </CardHeader>
      <CardFooter>
        <Button className="w-full">View Event</Button>
      </CardFooter>
    </Card>
  );
}

export { Course, CourseSkeleton };
