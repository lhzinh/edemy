import { Spinner } from '@/components/ui/spinner';

export default function Loading() {
  return (
    <div className="flex items-center gap-4">
      <Spinner className="size-8" />
    </div>
  );
}
