# main/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', auth_views.LoginView.as_view(template_name='main/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('about/', views.about, name='about'),
    path('profile/', views.profile, name='profile'),
    path('need_help/', views.need_help, name='need_help'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('explore/', views.explore, name='explore'),
    path('generate_pdf/', views.generate_pdf, name='generate_pdf'),
    path('view_contact_us/', views.view_contact_us, name='view_contact_us'),
    path('view_need_help/', views.view_need_help, name='view_need_help'),
]