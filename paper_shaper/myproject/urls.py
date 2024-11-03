# # myproject/urls.py

# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('accounts/', include('allauth.urls')),  # Include Allauth URLs
#     path('', include('myapp.urls')),  # Your app URLs
# ]


from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', include('myapp.urls')),  # Links the root URL to 'myapp'

    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),  # Include Allauth URLs
    path('icse/', include('icse_app.urls')),  # Link to ICSE app
    path('cbse/', include('cbse_app.urls')),  # Link to CBSE app
    path('others/', include('others_app.urls')),  # Link to Others app
]
