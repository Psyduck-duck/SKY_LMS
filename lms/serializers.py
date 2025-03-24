from rest_framework import serializers

from lms.models import Course, Lesson
from lms.validators import validate_youtube_url


class LessonSerializer(serializers.ModelSerializer):
    video_http_url = serializers.URLField(validators=[validate_youtube_url])
    # owner = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(many=True)

    def get_lesson_count(self, obj):
        return obj.lessons.count()

    class Meta:
        model = Course
        fields = ['id', 'name', 'image', 'description', 'lesson_count', 'lessons']
