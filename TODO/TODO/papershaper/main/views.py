
# main/views.py
import json
from django.contrib.auth import login, authenticate

import io
from django.http import HttpResponse
from fpdf import FPDF
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ContactForm, HelpForm, SignUpForm
# main/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import ContactUs, NeedHelp

def is_staff(user):
    return user.is_staff

@login_required
@user_passes_test(is_staff)
def view_contact_us(request):
    submissions = ContactUs.objects.all()
    return render(request, 'main/view_contact_us.html', {'submissions': submissions})

@login_required
@user_passes_test(is_staff)
def view_need_help(request):
    submissions = NeedHelp.objects.all()
    return render(request, 'main/view_need_help.html', {'submissions': submissions})


def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # Load the profile instance created by the signal
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'main/signup.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'main/profile.html')

@login_required
def explore(request):
    return render(request, 'main/explore.html')

def need_help(request):
    if request.method == 'POST':
        form = HelpForm(request.POST)
        if form.is_valid():
            # Process the form data and send an email or save to database
            send_mail(
                subject=f"Help Request from {form.cleaned_data['name']}",
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['support@example.com'],
            )
            messages.success(request, 'Your help request has been sent!')
            return redirect('need_help')
    else:
        form = HelpForm()
    return render(request, 'main/need_help.html', {'form': form})

def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data and send an email or save to database
            send_mail(
                subject=f"Contact Us Message from {form.cleaned_data['name']}",
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['contact@example.com'],
            )
            messages.success(request, 'Your message has been sent!')
            return redirect('contact_us')
    else:
        form = ContactForm()
    return render(request, 'main/contact_us.html', {'form': form})





def need_help(request):
    if request.method == 'POST':
        form = HelpForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            NeedHelp.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                message=form.cleaned_data['message']
            )
            messages.success(request, 'Your help request has been sent!')
            return redirect('need_help')
    else:
        form = HelpForm()
    return render(request, 'main/need_help.html', {'form': form})

def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            ContactUs.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                message=form.cleaned_data['message']
            )
            messages.success(request, 'Your message has been sent!')
            return redirect('contact_us')
    else:
        form = ContactForm()
    return render(request, 'main/contact_us.html', {'form': form})







def generate_pdf(request):
    if request.method == 'POST':
        # Parse the JSON data sent from the frontend
        data = json.loads(request.body)
        output_text = data.get('output', '')

        # Split the text into lines
        all_text = output_text.split('\n')

        # Create an instance of FPDF class
        pdf = FPDF()

        # Add a page
        pdf.add_page()

        # Set font style and size
        pdf.set_font("Arial", size=12)  # Adjust font size to better fit text

        # Set margins
        pdf.set_left_margin(10)
        pdf.set_right_margin(10)

        # Insert the texts from the variable into the PDF
        for line in all_text:
            # Use multi_cell for text wrapping
            pdf.multi_cell(0, 10, txt=line.encode('latin-1', 'replace').decode('latin-1'), align='L')

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