# myapp/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.http import JsonResponse

from django.conf import settings

import os
from .models import Prompt
from .genai import generate_response

def about(request):
    return render(request, 'myapp/about.html')

# myapp/views.py
from django.shortcuts import render

def contact(request):
    return render(request, 'myapp/contact.html')


def prompt_detail(class_no,prompt_type):
    results = Prompt.objects.get(Class=prompt_type, Type=class_no)
    return results




def home(request):
    return render(request, 'myapp/home.html')

@login_required
def explore(request):
    return render(request, 'myapp/explore.html')

@login_required
def thumbnail_detail(request, thumbnail_id):
    context = {
        'thumbnail_id': thumbnail_id,
        'message': f'This is the detail page for thumbnail {thumbnail_id}.'
    }
    return render(request, 'myapp/thumbnail_detail.html', context)

@login_required
def custom_logout(request):
    if request.method == 'POST':
        auth_logout(request)
        return redirect('home')
    return render(request, 'myapp/logout.html')

@login_required
def get_dynamic_options(request):
    category1 = request.GET.get('category1')
    category2 = request.GET.get('category2')
    category3 = request.GET.get('category3')

    options = {
        'category1':category1,
        'category2': [],
        'category3': [],
        'category4': [],

    }


    
    if category1:
        if category1 == 'Class 9th':
            options['category2'] = ['Maths','Science']

    if category2:
        if category2 == 'Science':
            options['category3'] = ["MATTER IN OUR SURROUNDINGS","Acids, Bases and Salts","Metals and Non-metals","Carbon and its Compounds","Life Processes",
                                "Control and Coordination","How do Organisms Reproduce","Heredity","Light – Reflection and Refraction","The Human Eye and the Colourful World",
                                "Electricity","Magnetic Effects of Electric Current"]


    if category3:

        options['category4'] = ['Mock Paper', 'Test Questions', 'MCQ']
        
    
    print(options)      
    return JsonResponse(options)





@login_required
def get_static_values(request):
    category1 = request.GET.get('category1')
    category2 = request.GET.get('category2')
    category3 = request.GET.get('category3')
    category4 = request.GET.get('category4')

    result = {
        'category1': category1,
        'category2': category2, 
        'category3': category3,
        'category4': category4,
    }
    place_holder = {}


    file_name_category3 = result['category3'] + ".txt"  # Append .txt to category3
    file_name_category4 = result['category4'] + ".txt"  # Append .txt to category3
    file_path = os.path.join(settings.BASE_DIR, f'myapp/static/myapp/{result['category1']}/{result['category2']}')

    file_name_category3 = os.path.join(file_path,file_name_category3)
    file_name_category4 = os.path.join(file_path,file_name_category3)

    if os.path.exists(file_name_category3):
        with open(file_name_category3, 'r',encoding='utf-8') as file:
            file_content = file.read().strip()
        place_holder["Document_content"] = file_content

    else:
        print(f"File not found: {file_name_category3}")


    if os.path.exists(file_name_category4):
        with open(file_name_category4, 'r',encoding='utf-8') as file:
            file_content = file.read().strip()
        place_holder[result['category4']] = file_content

    else:
        print(f"File not found: {file_name_category4}")

    print(place_holder)

    get_prompt = prompt_detail(result['category4'],result['category1'])

    response = generate_response(get_prompt.system_prompt,get_prompt.prompt.format(**place_holder),get_prompt.model)
    

    return JsonResponse({'output': response})

















