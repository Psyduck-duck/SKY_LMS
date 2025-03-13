from rest_framework import serializers

from lms.models import Course


class CourseSerializer(serializers.Serializer):
    class Meta:
        model = Course
        fields = ['id', 'image', 'description']
        