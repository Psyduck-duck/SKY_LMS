from rest_framework import serializers

from lms.models import Course, Lesson, CourseSubscription
from lms.validators import validate_youtube_url


class LessonSerializer(serializers.ModelSerializer):
    video_http_url = serializers.URLField(validators=[validate_youtube_url], default=None)
    # owner = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True)
    subscription = serializers.SerializerMethodField(read_only=True)

    def get_lesson_count(self, obj):
        return obj.lessons.count()

    def get_subscription(self, obj):
        user = self.context['request'].user
        return CourseSubscription.objects.filter(course=obj, user=user).exists()

    class Meta:
        model = Course
        fields = '__all__'


class CourseSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseSubscription
        fields = '__all__'
