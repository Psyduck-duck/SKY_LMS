from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from lms.models import Course, Lesson, CourseSubscription
from users.models import User


class CourseTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email='user@mail.com', )
        self.client.force_authenticate(user=self.user)
        self.course = Course.objects.create(name='Course', description='Course description', owner=self.user)
        self.lesson = Lesson.objects.create(name='Lesson', description='Lesson description', course=self.course,
                                            owner=self.user)

    def test_course_list(self):
        url = reverse('lms:course-list', )
        response = self.client.get(url)
        data = response.json()
        result = {
            'count': 1,
            'next': None,
            'previous': None,
            'results':
                [
                    {
                        'id': self.course.pk,
                        'lesson_count': 1,
                        'lessons':
                            [
                                {
                                    'id': self.lesson.pk,
                                    'video_http_url': None,
                                    'name': self.lesson.name,
                                    'description': self.lesson.description,
                                    'image': None,
                                    'course': self.course.pk,
                                    'owner': self.user.pk
                                }
                            ],
                        'subscription': False,
                        'name': self.course.name,
                        'image': None,
                        'description': self.course.description,
                        'owner': self.user.pk
                    }
                ]
        }

        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )

        self.assertEqual(
            data, result
        )

    def test_course_retrieve(self):
        url = reverse('lms:course-detail', args=(self.course.pk,))
        # self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_course_create(self):
        url = reverse('lms:course-list', )
        data = {'name': 'New Course', 'description': 'New course description'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )
        self.assertEqual(
            Course.objects.all().count(), 2
        )

    def test_course_update(self):
        url = reverse('lms:course-detail', args=(self.course.pk,))
        data = {'name': 'Updated Course', 'description': 'Updated course description'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            response.json()['name'], 'Updated Course'
        )

    def test_course_delete(self):
        url = reverse('lms:course-detail', args=(self.course.pk,))
        response = self.client.delete(url)
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            Course.objects.all().count(), 0
        )


class LessonTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email='user@mail.com', )
        self.client.force_authenticate(user=self.user)
        self.course = Course.objects.create(name='Course', description='Course description', owner=self.user)
        self.lesson = Lesson.objects.create(name='Lesson', description='Lesson description', course=self.course,
                                            owner=self.user)

    def test_lesson_list(self):
        url = reverse('lms:lessons_list', )
        response = self.client.get(url)
        data = response.json()
        result = {
            'count': 1,
            'next': None,
            'previous': None,
            'results':
                [
                    {
                        'id': self.lesson.pk,
                        'video_http_url': None,
                        'name': self.lesson.name,
                        'description': self.lesson.description,
                        'image': None,
                        'course': self.course.pk,
                        'owner': self.user.pk
                    }
                ]
        }

        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )

        self.assertEqual(
            data, result
        )

    def test_lesson_retrieve(self):
        url = reverse('lms:lessons_retrieve', args=(self.lesson.pk,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_lesson_create(self):
        url = reverse('lms:lessons_create')
        data = {
            'name': 'New Lesson',
            'description': 'New lesson description',
            'course': self.course.pk,
        }
        response = self.client.post(url, data)
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )
        self.assertEqual(
            Lesson.objects.all().count(), 2
        )

    def test_lesson_update(self):
        url = reverse('lms:lessons_update', args=(self.lesson.pk,))
        data = {'name': 'Updated Lesson', 'description': 'Updated lesson description'}
        response = self.client.patch(url, data)
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            response.json()['name'], 'Updated Lesson'
        )

    def test_lesson_delete(self):
        url = reverse('lms:lessons_delete', args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            Lesson.objects.all().count(), 0
        )

    def test_create_lesson_no_Youtube(self):
        url = reverse('lms:lessons_create')
        data = {
            'name': 'шляпа',
            'description': 'описание шляпы',
            'course': self.course.pk,
            'owner': self.user.pk,
            'video_http_url': 'https://www.example.com/'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Lesson.objects.count(), 1)


class SubscribeTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email='user@mail.com', )
        self.client.force_authenticate(user=self.user)
        self.course = Course.objects.create(name='Course', description='Course description', owner=self.user)
        self.lesson = Lesson.objects.create(name='Lesson', description='Lesson description', course=self.course,
                                            owner=self.user)

    def test_subscribe_to_course(self):
        url = reverse('lms:course_sub')
        data = {'course': self.course.pk}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], 'Подписка добавлена')
        self.assertTrue(CourseSubscription.objects.filter(user=self.user, course=self.course).exists())
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], 'Подписка удалена')
