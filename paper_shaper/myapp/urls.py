# myapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('explore/', views.explore, name='explore'),
    path('thumbnail/<int:thumbnail_id>/', views.thumbnail_detail, name='thumbnail_detail'),
    path('logout/', views.custom_logout, name='custom_logout'),
    path('get-dynamic-options/', views.get_dynamic_options, name='get_dynamic_options'),
    path('get-static-values/', views.get_static_values, name='get_static_values'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),  # Contact Us page
    path('submissions/', views.view_submissions, name='view_submissions'),  # View all submissions

]