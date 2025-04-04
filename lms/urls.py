from .views import CourseViewSet, LessonListAPIView, LessonCreateAPIView, LessonUpdateAPIView, LessonRetrieveAPIView, \
    LessonDestroyAPIView, CourseSubscribeAPIView
from django.urls import path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

app_name = 'lms'

router.register(r'courses', CourseViewSet, basename='course')

urlpatterns = [
                  path('lessons/', LessonListAPIView.as_view(), name='lessons_list'),
                  path('lessons/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lessons_retrieve'),
                  path('lessons/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='lessons_delete'),
                  path('lessons/create/', LessonCreateAPIView.as_view(), name='lessons_create'),
                  path('lessons/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lessons_update'),
                  path('sub/', CourseSubscribeAPIView.as_view(), name='course_sub')
              ] + router.urls
