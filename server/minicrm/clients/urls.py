from django.urls import path
from . import views

urlpatterns = [
#clients/, /clients/add/, /clients/<id>/edit/, /clients/<id>/delete/
    path('', views.get_list, name="get_list"),
    path('add_client/', views.add_new_customer, name='add_client'),
    path('<int:pk>/edit/', views.edit_customer, name='edit_customer'),
    path('<int:pk>/edit/delete/', views.delete_customer, name='delete_customer'),
]