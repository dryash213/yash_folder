from django.urls import path
from . import views

app_name = 'app1'

urlpatterns = [
    path('', views.index, name='index'),
    path('get-options-for-dropdown2/', views.get_options_for_dropdown2, name='get_options_for_dropdown2'),
    path('get-options-for-dropdown3/', views.get_options_for_dropdown3, name='get_options_for_dropdown3'),
    path('get-options-for-dropdown4/', views.get_options_for_dropdown4, name='get_options_for_dropdown4'),
    path('api/endpoint/', views.api_endpoint, name='api_endpoint'),
]
        
