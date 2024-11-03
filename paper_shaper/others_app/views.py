from django.shortcuts import render

def others_home(request):
    return render(request, 'others_app/others_home.html')
