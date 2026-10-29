from core.serializers import DynamicFieldsModelSerializer
from courses.models import Category, Course
from rest_framework import serializers


class CategorySerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Category
        fields = ["slug", "name"]


class CourseSerializer(DynamicFieldsModelSerializer):
    categories = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field="name"
    )

    class Meta:
        model = Course
        exclude = ["id", "date_updated", "creator", "changer"]


class GenerateCourseSerializer(serializers.Serializer):
    topic = serializers.CharField(max_length=200)
    difficulty = serializers.ChoiceField(
        choices=["Beginner", "Intermediate", "Advanced"],
        default="Beginner",
    )