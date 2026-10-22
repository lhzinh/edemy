from langchain_core.tools import tool
from langchain_core.runnables import RunnableConfig

from bot.llms import call_model
from courses.models import Course

model = call_model()


@tool
def list_courses(config: RunnableConfig):
    """
    Get list courses from Course models for the current user.
    """
    metadata = config.get("metadata") or config.get("configurable")
    courses = (
        Course.objects.filter(creator_id=metadata.get("user_id"))
        .all()
        .order_by("-date_created")
    )
    res = []
    for obj in courses:
        res.append({"id": obj.id, "title": obj.title})
    return res


@tool
def get_course(course_id: int, config: RunnableConfig):
    """
    Get the details of a course from Course models for the current user.
    """
    metadata = config.get("metadata") or config.get("configurable")

    try:
        obj = Course.objects.get(id=course_id, creator_id=metadata.get("user_id"))
    except Course.DoesNotExist:
        raise Exception("Course not foun, try again")

    res = {"id": obj.id, "title": obj.title}
    return res


tools = [list_courses, get_course]
tools_by_name = {tool.name: tool for tool in tools}
model_with_tools = model.bind_tools(tools)
