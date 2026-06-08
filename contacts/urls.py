from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('delete/<int:pk>/', views.delete_contact, name ='delete_contact'),
    path('update/<int:pk>/',views.update_contact, name = 'update_contact'),
    path('api/contacts/', views.api_contacts, name='api_contacts'),
    path('api/contacts/<int:pk>/', views.api_contact_detail, name='api_contact_detail'),
]