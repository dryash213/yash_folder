# app1/views.py
from django.http import JsonResponse, HttpResponseBadRequest
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def index(request):
    return render(request, 'app1/index.html')

@login_required
def get_dynamic_options(request):
    category1 = request.GET.get('category1')
    category2 = request.GET.get('category2')
    category3 = request.GET.get('category3')

    if not category1:
        return HttpResponseBadRequest("Missing category1 parameter.")

    options = {
        'category2': [],
        'category3': [],
        'category4': [],
    }

    # Class and subject selection logic for Class 9
    if category1 == 'Class 9th':
        options['category2'] = ['Maths', 'Science', "English-Moments", "English-Beehive", "English-Words and Expressions"]
        if category2:
            if category2 == 'Science':
                options['category3'] = ["MATTER IN OUR SURROUNDINGS", "IS MATTER AROUND US PURE", "ATOMS AND MOLECULES", "STRUCTURE OF THE ATOM", "THE FUNDAMENTAL UNIT OF LIFE",
                                        "TISSUES", "MOTION", "FORCE AND LAWS OF MOTION", "GRAVITATION", "WORK AND ENERGY",
                                        "SOUND", "IMPROVEMENT IN FOOD RESOURCES"]
            elif category2 == 'Maths':
                options['category3'] = ["NUMBER SYSTEMS", "POLYNOMIALS", "COORDINATE GEOMETRY", "LINEAR EQUATIONS IN TWO VARIABLES", "INTRODUCTION TO EUCLID’S GEOMETRY",
                                        "LINES AND ANGLES", "TRIANGLES", "QUADRILATERALS", "CIRCLES", "HERON’S FORMULA",
                                        "SURFACE AREAS AND VOLUMES", "STATISTICS"]
            elif category2 == 'English-Moments':
                options['category3'] = ["The Lost Child", "The Adventures of Toto", "Iswaran the Storyteller", "In the Kingdom of Fools", "The Happy Prince", "Weathering the Storm in Ersama", "The Last Leaf", "A House Is Not a Home", "The Beggar"]
            elif category2 == 'English-Beehive':
                options['category3'] = ["The Sound of Music", "The Little Girl", "A Truly Beautiful Mind", "The Snake and the Mirror", "My Childhood", "Reach for the Top", "Kathmandu", "If I Were You", "The Fun They Had"]
            elif category2 == 'English-Words and Expressions':
                options['category3'] = ["Unit1", "Unit2", "Unit3", "Unit4", "Unit5", "Unit6", "Unit7", "Unit8", "Unit9"]

    # Class and subject selection logic for Class 10
    elif category1 == 'Class 10th':
        options['category2'] = ['Maths', 'Science', "English-First Flight"]
        if category2:
            if category2 == 'Science':
                options['category3'] = ["Chemical Reactions and Equations", "Acids, Bases and Salts", "Metals and Non-metals",
                                        "Carbon and its Compounds", "Periodic Classification of Elements", "Life Processes",
                                        "Control and Coordination", "How do Organisms Reproduce", "Heredity and Evolution",
                                        "Light – Reflection and Refraction", "The Human Eye and the Colourful World",
                                        "Electricity", "Magnetic Effects of Electric Current", "Sources of Energy",
                                        "Our Environment", "Sustainable Management of Natural Resources"]
            elif category2 == 'Maths':
                options['category3'] = ["Real Numbers", "Polynomials", "Pair of Linear Equations in Two Variables", "Quadratic Equations",
                                        "Arithmetic Progressions", "Triangles", "Coordinate Geometry", "Introduction to Trigonometry",
                                        "Some Applications of Trigonometry", "Circles", "Constructions", "Areas Related to Circles",
                                        "Surface Areas and Volumes", "Statistics", "Probability"]
            elif category2 == 'English-First Flight':
                options['category3'] = ["A Letter to God", "Nelson Mandela: Long Walk to Freedom", "Two Stories about Flying", "From the Diary of Anne Frank", "Glimpses of India", "Mijbil the Otter", "Madam Rides the Bus", "The Sermon at Benares", "The Proposal"]

    # Class and subject selection logic for Class 11
    elif category1 == 'Class 11th':
        options['category2'] = ['Maths', 'Physics', 'Chemistry', 'Biology']
        if category2:
            if category2 == 'Physics':
                options['category3'] = ["Physical World", "Units and Measurements", "Motion in a Straight Line",
                                        "Motion in a Plane", "Laws of Motion", "Work, Energy and Power",
                                        "System of Particles and Rotational Motion", "Gravitation",
                                        "Mechanical Properties of Solids", "Mechanical Properties of Fluids",
                                        "Thermal Properties of Matter", "Thermodynamics", "Kinetic Theory",
                                        "Oscillations", "Waves"]
            elif category2 == 'Chemistry':
                options['category3'] = ["Some Basic Concepts of Chemistry", "Structure of Atom",
                                        "Classification of Elements and Periodicity in Properties",
                                        "Chemical Bonding and Molecular Structure", "Chemical Thermodynamics",
                                        "Equilibrium", "Redox Reactions", "Organic Chemistry – Some Basic Principles and Techniques",
                                        "Hydrocarbons"]
            elif category2 == 'Biology':
                options['category3'] = ["Diversity in the Living World", "Biological Classification",
                                        "Plant Kingdom", "Animal Kingdom", "Morphology of Flowering Plants",
                                        "Anatomy of Flowering Plants", "Structural Organisation in Animals",
                                        "Cell: The Unit of Life", "Biomolecules", "Cell Cycle and Cell Division",
                                        "Photosynthesis in Higher Plants", "Respiration in Plants",
                                        "Plant Growth and Development", "Human Physiology", "Body Fluids and Circulation",
                                        "Excretory Products and Their Elimination", "Locomotion and Movement",
                                        "Neural Control and Coordination", "Chemical Coordination and Integration"]

    # Class and subject selection logic for Class 12
    elif category1 == 'Class 12th':
        options['category2'] = ['Maths', 'Physics', 'Chemistry', 'Biology']
        if category2:
            if category2 == 'Physics':
                options['category3'] = ["Electric Charges and Fields", "Electrostatic Potential and Capacitance",
                                        "Current Electricity", "Moving Charges and Magnetism", "Magnetism and Matter",
                                        "Electromagnetic Induction", "Alternating Current", "Electromagnetic Waves",
                                        "Ray Optics and Optical Instruments", "Wave Optics", "Dual Nature of Radiation and Matter",
                                        "Atoms", "Nuclei", "Semiconductor Electronics: Materials, Devices and Simple Circuits"]
            elif category2 == 'Chemistry':
                options['category3'] = ["Solutions", "Electrochemistry", "Chemical Kinetics", "d- and f-Block Elements",
                                        "Coordination Compounds", "Haloalkanes and Haloarenes", "Alcohols, Phenols and Ethers",
                                        "Aldehydes, Ketones and Carboxylic Acids", "Amines", "Biomolecules"]
            elif category2 == 'Biology':
                options['category3'] = ["Sexual Reproduction in Flowering Plants", "Human Reproduction",
                                        "Reproductive Health", "Principles of Inheritance and Variation",
                                        "Molecular Basis of Inheritance", "Evolution", "Human Health and Diseases",
                                        "Microbes in Human Welfare", "Biotechnology – Principles and Processes",
                                        "Biotechnology and its Applications", "Organisms and Populations",
                                        "Ecosystem", "Biodiversity and Its Conservation"]

    # Add options for the fourth category
    if category3:
        options['category4'] = ['Mock Paper', 'Test Questions', 'MCQ']

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

    return JsonResponse({'output': result})