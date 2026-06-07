from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('delete/<int:pk>/', views.delete_contact, name ='delete_contact'),
    path('update/<int:pk>/',views.update_contact, name = 'update_contact'),
]