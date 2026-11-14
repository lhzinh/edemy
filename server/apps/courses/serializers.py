from core.serializers import (
    DynamicFieldsModelSerializer,
    GeneralSerializer,
    HyperlinkedModelSerializer,
)
from courses.models import Category, Course
from rest_framework import serializers


class CategorySerializer(DynamicFieldsModelSerializer, GeneralSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class CourseSerializer(
    DynamicFieldsModelSerializer, GeneralSerializer, HyperlinkedModelSerializer
):
    category = serializers.SlugRelatedField(read_only=True, slug_field="name")

    class Meta:
        model = Course
        fields = "__all__"
        # exclude = ["category"]
