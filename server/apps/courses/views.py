from core.paginators import StandardResultsSetPagination
from courses.filters import CourseFilter
from courses.models import Category, Course, Lesson, Module
from courses.serializers import (
    CategorySerializer,
    CourseSerializer,
    GenerateCourseSerializer,
)
from courses.services import generate_course_content
from django.db import transaction
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A viewset for viewing categories.
    """

    serializer_class = CategorySerializer
    queryset = Category.scalars.all()


class CourseViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing courses.
    """

    serializer_class = CourseSerializer
    filterset_class = CourseFilter
    pagination_class = StandardResultsSetPagination
    permission_classes = [AllowAny]
    lookup_field = "slug"

    def get_queryset(self):
        qs = Course.scalars.prefetch_related("categories")
        if self.action == "retrieve":
            qs = qs.prefetch_related("modules__lessons")
        return qs.all().order_by("-date_created")

    @action(
        detail=False,
        methods=["post"],
        url_path="generate",
        serializer_class=[GenerateCourseSerializer],
    )
    def generate(self, request):
        """POST /courses/generate/ - Generate a course using Gemini."""
        input_ser = self.get_serializer(data=request.data)
        input_ser.is_valid(raise_exception=True)

        try:
            data = generate_course_content(**input_ser.validated_data)
        except Exception:
            # logger.exception("Gemini course generation failed")
            return Response(
                {"detail": "Failed to generate course. Please try again."},
                status=status.HTTP_502_BAD_GATEWAY,
            )

        with transaction.atomic():
            course = Course.objects.create(
                title=data.title, description=data.description
            )

            for m_order, module_data in enumerate(data.modules, start=1):
                module = Module.objects.create(
                    course=course, title=module_data.title, order=m_order
                )
                Lesson.objects.bulk_create(
                    Lesson(
                        module=module,
                        title=lesson.title,
                        content=lesson.content,
                        order=l_order,
                    )
                    for l_order, lesson in enumerate(module_data.lessons, start=1)
                )

        output = CourseSerializer(course, context=self.get_serializer_context())
        return Response(output.data, status=status.HTTP_201_CREATED)
