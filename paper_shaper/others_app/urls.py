from django.urls import path
from . import views

urlpatterns = [
    path('', views.others_home, name='others'),
]
