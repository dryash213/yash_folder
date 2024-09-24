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


    
from django.http import JsonResponse, HttpResponseBadRequest

def get_dynamic_options(request):
    category1 = request.GET.get('category1')
    category2 = request.GET.get('category2')
    category3 = request.GET.get('category3')
    
    # Check if category1 is provided
    if not category1:
        return HttpResponseBadRequest("Missing category1 parameter.")

    # Define options dictionary to store category selections
    options = {} 

    # Class and subject selection logic for Class 9
    if category1:
        if category1 == 'Class 9th':
            options['category2'] = ['Maths', 'Science']

    if category2:
        if category2 == 'Science':
<<<<<<< HEAD
            options['category3'] = [
                "MATTER IN OUR SURROUNDINGS", "IS MATTER AROUND US PURE?", "ATOMS AND MOLECULES", 
                "STRUCTURE OF THE ATOM", "THE FUNDAMENTAL UNIT OF LIFE", "TISSUES", 
                "MOTION", "FORCE AND LAWS OF MOTION", "GRAVITATION", "WORK AND ENERGY", 
                "SOUND", "IMPROVEMENT IN FOOD RESOURCES"
            ]
        elif category2 == 'Maths':
            options['category3'] = [
                "Number Systems", "Polynomials", "Coordinate Geometry", "Linear Equations in Two Variables", 
                "Introduction to Euclid's Geometry", "Lines and Angles", "Triangles", "Quadrilaterals", 
                "Areas of Parallelograms and Triangles", "Circles", "Constructions", "Heron's Formula", 
                "Surface Areas and Volumes", "Statistics", "Probability"
            ]
=======
            options['category3'] = ["MATTER IN OUR SURROUNDINGS","IS MATTER AROUND US PURE","ATOMS AND MOLECULES","STRUCTURE OF THE ATOM","THE FUNDAMENTAL UNIT OF LIFE",
                                "TISSUES","MOTION","FORCE AND LAWS OF MOTION","GRAVITATION","WORK AND ENERGY",
                                "SOUND","IMPROVEMENT IN FOOD RESOURCES"]
            
        if category2 == 'Maths':
            options['category3'] = ["NUMBER SYSTEMS","POLYNOMIALS","COORDINATE GEOMETRY","LINEAR EQUATIONS IN TWO VARIABLES","INTRODUCTION TO EUCLID’S GEOMETRY",
                                "LINES AND ANGLES","TRIANGLES","QUADRILATERALS","CIRCLES","HERON’S FORMULA",
                                "SURFACE AREAS AND VOLUMES","STATISTICS"]
>>>>>>> 7f3e19e66d4fa3403fe5a50477f1e6c3c97373e1

    # For Class 10
    if category1:
        if category1 == 'Class 10th':
            options['category2'] = ['Maths', 'Science']

    if category2:
        if category2 == 'Science':
            options['category3'] = [
                "Chemical Reactions and Equations", "Acids, Bases and Salts", "Metals and Non-metals", 
                "Carbon and its Compounds", "Periodic Classification of Elements", "Life Processes", 
                "Control and Coordination", "How do Organisms Reproduce", "Heredity and Evolution", 
                "Light – Reflection and Refraction", "The Human Eye and the Colourful World", 
                "Electricity", "Magnetic Effects of Electric Current", "Sources of Energy", 
                "Our Environment", "Sustainable Management of Natural Resources"
            ]
        elif category2 == 'Maths':
            options['category3'] = [
                "Real Numbers", "Polynomials", "Pair of Linear Equations in Two Variables", "Quadratic Equations", 
                "Arithmetic Progressions", "Triangles", "Coordinate Geometry", "Introduction to Trigonometry", 
                "Some Applications of Trigonometry", "Circles", "Constructions", "Areas Related to Circles", 
                "Surface Areas and Volumes", "Statistics", "Probability"
            ]

    # For Class 11
    if category1 == 'Class 11th':
        options['category2'] = ['Maths', 'Physics', 'Chemistry', 'Biology']

        if category2 == 'Physics':
            options['category3'] = [
                "Physical World", "Units and Measurements", "Motion in a Straight Line", 
                "Motion in a Plane", "Laws of Motion", "Work, Energy and Power", 
                "System of Particles and Rotational Motion", "Gravitation", 
                "Mechanical Properties of Solids", "Mechanical Properties of Fluids", 
                "Thermal Properties of Matter", "Thermodynamics", "Kinetic Theory", 
                "Oscillations", "Waves"
            ]
        elif category2 == 'Chemistry':
            options['category3'] = [
                "Some Basic Concepts of Chemistry", "Structure of Atom", 
                "Classification of Elements and Periodicity in Properties", 
                "Chemical Bonding and Molecular Structure", "Chemical Thermodynamics", 
                "Equilibrium", "Redox Reactions", "Organic Chemistry – Some Basic Principles and Techniques", 
                "Hydrocarbons"
            ]
        elif category2 == 'Biology':
            options['category3'] = [
                "Diversity in the Living World", "Biological Classification", 
                "Plant Kingdom", "Animal Kingdom", "Morphology of Flowering Plants", 
                "Anatomy of Flowering Plants", "Structural Organisation in Animals", 
                "Cell: The Unit of Life", "Biomolecules", "Cell Cycle and Cell Division", 
                "Photosynthesis in Higher Plants", "Respiration in Plants", 
                "Plant Growth and Development", "Human Physiology", "Body Fluids and Circulation", 
                "Excretory Products and Their Elimination", "Locomotion and Movement", 
                "Neural Control and Coordination", "Chemical Coordination and Integration"
            ]

    # Class and subject selection logic for Class 12
    elif category1 == 'Class 12th':
        options['category2'] = ['Maths', 'Physics', 'Chemistry', 'Biology']

        if category2 == 'Physics':
            options['category3'] = [
                "Electric Charges and Fields", "Electrostatic Potential and Capacitance", 
                "Current Electricity", "Moving Charges and Magnetism", "Magnetism and Matter", 
                "Electromagnetic Induction", "Alternating Current", "Electromagnetic Waves", 
                "Ray Optics and Optical Instruments", "Wave Optics", "Dual Nature of Radiation and Matter", 
                "Atoms", "Nuclei", "Semiconductor Electronics: Materials, Devices and Simple Circuits"
            ]
        elif category2 == 'Chemistry':
            options['category3'] = [
                "Solutions", "Electrochemistry", "Chemical Kinetics", "d- and f-Block Elements", 
                "Coordination Compounds", "Haloalkanes and Haloarenes", "Alcohols, Phenols and Ethers", 
                "Aldehydes, Ketones and Carboxylic Acids", "Amines", "Biomolecules"
            ]
        elif category2 == 'Biology':
            options['category3'] = [
                "Sexual Reproduction in Flowering Plants", "Human Reproduction", 
                "Reproductive Health", "Principles of Inheritance and Variation", 
                "Molecular Basis of Inheritance", "Evolution", "Human Health and Diseases", 
                "Microbes in Human Welfare", "Biotechnology – Principles and Processes", 
                "Biotechnology and its Applications", "Organisms and Populations", 
                "Ecosystem", "Biodiversity and Its Conservation"
            ]

    # Add options for the fourth category
    if category3:
        options['category4'] = ['Mock Paper', 'Test Questions', 'MCQ']
<<<<<<< HEAD

    # Return the options as a JsonResponse
=======
        
    
    #print(options)      
>>>>>>> 7f3e19e66d4fa3403fe5a50477f1e6c3c97373e1
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



