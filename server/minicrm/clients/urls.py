from django.urls import path
from .views import health_ok

urlpatterns = [
    path('', health_ok, name='health')
]