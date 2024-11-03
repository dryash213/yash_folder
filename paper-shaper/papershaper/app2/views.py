# app1/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return render(request, 'app2/index.html')


# app1/views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import time

@csrf_exempt
def api_endpoint(request):
    if request.method == 'POST':
        # Simulate a delay
        time.sleep(2)

        # Extract data from POST request
        data = request.POST
        dropdown1 = data.get('dropdown1')
        dropdown2 = data.get('dropdown2')
        dropdown3 = data.get('dropdown3')
        dropdown4 = data.get('dropdown4')

        # Process the data and generate a response
        response_data = {
            'message': f'Selected options: {dropdown1}, {dropdown2}, {dropdown3}, {dropdown4}'
        }
        return JsonResponse(response_data)
    return JsonResponse({'error': 'Invalid request'}, status=400)