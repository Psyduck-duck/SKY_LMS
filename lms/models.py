from django.db import models

from users.models import User


class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название курса')
    image = models.ImageField(upload_to='courses_images/', blank=True, null=True, verbose_name='Фото курса')
    description = models.TextField(verbose_name='Описание')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='courses', verbose_name='Владелец')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название урока')
    description = models.TextField(verbose_name='Описание урока')
    image = models.ImageField(upload_to='courses_images/', blank=True, null=True, verbose_name='Фото урока')
    video_http_url = models.URLField(blank=True, null=True, verbose_name='Ссылка на видео')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons', verbose_name='Курс')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lessons', verbose_name='Владелец')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
