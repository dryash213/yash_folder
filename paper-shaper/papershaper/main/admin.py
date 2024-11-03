# main/admin.py
from django.contrib import admin
from .models import ContactUs, NeedHelp

admin.site.register(ContactUs)
admin.site.register(NeedHelp)