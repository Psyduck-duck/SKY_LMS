from rest_framework.documentation import include_docs_urls
from django.urls import path


app_name = 'api_docs'

urlpatterns = [
    path('docs/', include_docs_urls(title='API Documentation')),
]