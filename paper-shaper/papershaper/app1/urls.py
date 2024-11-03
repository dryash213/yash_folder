# app1/urls.py
from django.urls import path
from . import views

app_name = 'app1'

urlpatterns = [
    path('', views.index, name='index'),
    path('get_dynamic_options/', views.get_dynamic_options, name='get_dynamic_options'),
    path('get_static_values/', views.get_static_values, name='get_static_values'),
]