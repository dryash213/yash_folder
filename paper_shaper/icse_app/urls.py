from django.urls import path
from . import views

urlpatterns = [
    path('', views.icse_home, name='icse'),
]
