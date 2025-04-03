from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from .models import Course, Lesson, CourseSubscription
from .paginators import CustomPagination
from .serializers import CourseSerializer, LessonSerializer, CourseSubscriptionSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, generics, views
from .permissions import IsOwner, IsManager


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination

    def perform_create(self, serializer):
        new_course = serializer.save()
        new_course.owner = self.request.user
        new_course.save()

    def get_permissions(self):
        if self.action == 'create':
            self.permissions_classes = (~IsManager,)
        elif self.action in ['update', 'retrieve', 'partial_update']:
            self.permissions_classes = (IsManager | IsOwner,)
        elif self.action == 'destroy':
            self.permissions_classes = (IsOwner, ~IsManager)
        return super().get_permissions()


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated & ~IsManager]

    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.owner = self.request.user
        new_lesson.save()


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner | IsManager]


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner | IsManager]


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated & ~IsManager & IsOwner]


class CourseSubscribeAPIView(views.APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CourseSubscriptionSerializer

    def post(self, *args, **kwargs):
        user = self.request.user
        course_pk = self.request.data.get('course')
        course_item = get_object_or_404(Course, pk=course_pk)

        subs_item = CourseSubscription.objects.filter(course=course_item, user=user)

        if subs_item.exists():
            subs_item.delete()
            message = 'Подписка удалена'

        else:
            CourseSubscription.objects.create(course=course_item, user=user)
            message = 'Подписка добавлена'

        return Response({'message': message})
