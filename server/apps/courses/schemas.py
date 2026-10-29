from pydantic import BaseModel, Field


class LessonSchema(BaseModel):
    title: str = Field(description="Title of the lesson", max_length=255)
    content: str = Field(description="Detailed educational content in Markdown")


class ModuleSchema(BaseModel):
    title: str = Field(description="Title of the module")
    lessons: list[LessonSchema] = Field(
        description="List of lessons in this module", min_length=1
    )


class CourseSchema(BaseModel):
    title: str = Field(description="Course title")
    description: str = Field(description="Short summary of the course")
    modules: list[ModuleSchema] = Field(
        description="List of learning modules", min_length=1
    )