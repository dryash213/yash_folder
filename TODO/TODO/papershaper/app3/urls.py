# app1/urls.py
from django.urls import path
from . import views

app_name = 'app3'

urlpatterns = [
    path('', views.index, name='index'),
    path('api/endpoint/', views.api_endpoint, name='api_endpoint'),
]