from django.urls import path
from rest_framework.routers import DefaultRouter

from users.views import UserViewSet, PaymentViewSet

router = DefaultRouter()

app_name = 'users'

router.register(r'users', UserViewSet, basename='user')
router.register(r'payments', PaymentViewSet, basename='payment')

urlpatterns = [

] + router.urls
