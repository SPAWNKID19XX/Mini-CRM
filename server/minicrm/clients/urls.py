from django.urls import path
from . import views

urlpatterns = [
#clients/, /clients/add/, /clients/<id>/edit/, /clients/<id>/delete/
    path('', views.get_list, name="get_list"),
    path('add_client/', views.add_new_customer, name='add_client')
]