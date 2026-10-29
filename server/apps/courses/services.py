import os
from google import genai
from google.genai import types
from courses.schemas import CourseSchema

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))


def generate_course_content(topic: str, difficulty: str) -> CourseSchema:
    prompt = (
        f"Create a comprehensive course on '{topic}' for '{difficulty}' level students."
    )

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=CourseSchema,
            temperature=0.3,
        ),
    )
    
    return response.parsed
