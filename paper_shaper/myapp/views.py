# myapp/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.http import JsonResponse
import markdown

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
    #print(class_no,prompt_type)
    results = Prompt.objects.get(Class=prompt_type, Type=class_no)
    #print(results)
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
            options['category3'] = ["MATTER IN OUR SURROUNDINGS","IS MATTER AROUND US PURE","ATOMS AND MOLECULES","STRUCTURE OF THE ATOM","THE FUNDAMENTAL UNIT OF LIFE",
                                "TISSUES","MOTION","FORCE AND LAWS OF MOTION","GRAVITATION","WORK AND ENERGY",
                                "SOUND","IMPROVEMENT IN FOOD RESOURCES"]
            
        if category2 == 'Maths':
            options['category3'] = ["NUMBER SYSTEMS","POLYNOMIALS","COORDINATE GEOMETRY","LINEAR EQUATIONS IN TWO VARIABLES","INTRODUCTION TO EUCLID’S GEOMETRY",
                                "LINES AND ANGLES","TRIANGLES","QUADRILATERALS","CIRCLES","HERON’S FORMULA",
                                "SURFACE AREAS AND VOLUMES","STATISTICS"]


    if category3:

        options['category4'] = ['Mock Paper', 'Test Questions', 'MCQ']
        
    
    #print(options)      
    return JsonResponse(options)




# myapp/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save the data to the database
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')  # Redirect to the same page after submission
        else:
            messages.error(request, 'There was an error submitting the form. Please try again.')
    else:
        form = ContactForm()

    return render(request, 'myapp/contact.html', {'form': form})

# myapp/views.py
from django.shortcuts import render
from .models import Contact
# myapp/views.py
from django.contrib.auth.decorators import login_required

@login_required
def view_submissions(request):
    submissions = Contact.objects.all().order_by('-submitted_at')
    return render(request, 'myapp/view_submissions.html', {'submissions': submissions})

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
    # #print(file_path,"********************************")
    file_name_category3 = os.path.join(file_path,file_name_category3)
    file_name_category4 = os.path.join(file_path,file_name_category4)

    if os.path.exists(file_name_category3):
        with open(file_name_category3, 'r',encoding='utf-8') as file:
            file_content3 = file.read().strip()
        place_holder["Document_content"] = file_content3

    else:
        print(f"File not found: {file_name_category3}")


    if os.path.exists(file_name_category4):
        with open(file_name_category4, 'r',encoding='utf-8') as file:
            file_content4 = file.read().strip()
            
        place_holder[result['category4']] = file_content4

    else:
        print(f"File not found: {file_name_category4}")

    # print(place_holder,"%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")

    get_prompt = prompt_detail(result['category4'],result['category1'])

    response = generate_response(get_prompt.system_prompt,get_prompt.prompt.format(**place_holder),get_prompt.model)
    # html_content = markdown.markdown(response)

    return JsonResponse({'output': response})


from django.http import HttpResponse
from fpdf import FPDF
import io
import json

def generate_pdf(request):
    if request.method == 'POST':
        # Parse the JSON data sent from the frontend
        data = json.loads(request.body)
        output_text = data.get('output', '')
        print(type(output_text))

        # Split the text into lines
        all_text = output_text.split('\\n')
        print(all_text)

        # Create an instance of FPDF class
        pdf = FPDF()

        # Add a page
        pdf.add_page()

        # Set font style and size
        pdf.set_font("Arial", size=15)

        # Insert the texts from the variable into the PDF
        for line in all_text:
            # Use encode to handle special characters
            pdf.cell(200, 10, txt=line.encode('latin-1', 'replace').decode('latin-1'), ln=1, align='C')

        # Create a BytesIO buffer to store the PDF
        buffer = io.BytesIO()

        # Output the PDF into the buffer as a string (set dest='S')
        pdf_data = pdf.output(dest='S').encode('latin1')  # Encode the string as binary for HTTP response

        # Write the binary data to the buffer
        buffer.write(pdf_data)

        # Move the buffer's cursor to the beginning
        buffer.seek(0)

        # Return the PDF as an HttpResponse
        response = HttpResponse(buffer, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="output.pdf"'

        return response
    else:
        return HttpResponse(status=405)  # Method not allowed



