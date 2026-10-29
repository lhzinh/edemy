"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";

export interface CourseGenerationPayload {
  topic: string;
  difficulty: "Beginner" | "Intermediate" | "Advanced";
}

export interface GenerationResponse {
  course_id: number;
  title: string;
}

export default function Generator({ authToken }: { authToken: string }) {
  const [topic, setTopic] = useState("");
  const [difficulty, setDifficulty] = useState<CourseGenerationPayload["difficulty"]>("Beginner");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const router = useRouter();

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    setLoading(true);
    setError(null);

    try {
      const res = await fetch("http://localhost:8000/courses/generate/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ topic, difficulty }),
      });

      if (!res.ok) {
        throw new Error("Failed to generate course. Please try again.");
      }

      const data: GenerationResponse = await res.json();
      console.log(data)
    //   router.push(`/courses/${data.course_id}`);
    } catch (err: unknown) {
      if (err instanceof Error) setError(err.message);
    } finally {
      setLoading(false);
    }
  }

  return (
    <form onSubmit={handleSubmit} className="flex flex-col gap-4 max-w-md mx-auto p-4 border rounded">
      <label className="flex flex-col gap-1">
        <span className="font-semibold">What do you want to learn?</span>
        <input
          type="text"
          value={topic}
          onChange={(e) => setTopic(e.target.value)}
          placeholder="e.g., Python Concurrency, Docker Fundamentals"
          required
          className="border p-2 rounded"
        />
      </label>

      <label className="flex flex-col gap-1">
        <span className="font-semibold">Skill Level</span>
        <select
          value={difficulty}
          onChange={(e) => setDifficulty(e.target.value as CourseGenerationPayload["difficulty"])}
          className="border p-2 rounded"
        >
          <option value="Beginner">Beginner</option>
          <option value="Intermediate">Intermediate</option>
          <option value="Advanced">Advanced</option>
        </select>
      </label>

      {error && <p className="text-red-500 text-sm">{error}</p>}

      <button
        type="submit"
        disabled={loading}
        className="bg-blue-600 text-white py-2 px-4 rounded disabled:bg-gray-400"
      >
        {loading ? "AI is generating your course..." : "Generate Course"}
      </button>
    </form>
  );
}