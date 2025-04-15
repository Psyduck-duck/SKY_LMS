from django.contrib import admin
from .models import Course, Lesson, CourseSubscription


@admin.register(Course)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'owner')
    search_fields = ('name',)


@admin.register(Lesson)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'video_http_url', 'course', 'owner')
    search_fields = ('name', 'video_http_url')


@admin.register(CourseSubscription)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('course', 'user')
    search_fields = ('course',)
