from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True, verbose_name='Номер телефона')
    city = models.CharField(max_length=100, blank=True, null=True, verbose_name='Страна')
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True, verbose_name='Аватар')
    # token = models.CharField(max_length=100, verbose_name="Token", blank=True, null=True)
    is_active = models.BooleanField(default=False)
    # is_blocked = models.BooleanField(default=False, verbose_name="Пользователь заблокирован")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'


class Payment(models.Model):
    PAYMENT_SYSTEM_CHOISES = [
        ('Наличные', 'Наличные'),
        ('Перевод на счет', 'Перевод на счет')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payments', verbose_name='Пользователь')
    pay_date = models.DateField(blank=True, null=True, auto_now_add=True, verbose_name='Дата платежа')
    course = models.ForeignKey('lms.Course', blank=True, on_delete=models.CASCADE, related_name='payments', verbose_name='Курс')
    lesson = models.ForeignKey('lms.Lesson', on_delete=models.CASCADE, related_name='pauments', verbose_name='Урок')
    amount = models.PositiveIntegerField(verbose_name='Сумма платежа')
    payment_system = models.CharField(max_length=100, choices=PAYMENT_SYSTEM_CHOISES, verbose_name='Способ оплаты')
    session_id = models.CharField(max_length=255, blank=True, null=True, verbose_name='ID сессии')
    link = models.URLField(max_length=400, blank=True, null=True, verbose_name='Ссылка на оплату')
