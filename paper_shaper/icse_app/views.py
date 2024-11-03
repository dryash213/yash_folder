from django.shortcuts import render

def icse_home(request):
    return render(request, 'icse_app/icse_home.html')
