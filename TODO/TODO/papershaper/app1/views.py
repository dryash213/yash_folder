from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@login_required
def index(request):
    return render(request, 'app1/index.html')

@csrf_exempt
def get_options_for_dropdown2(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        selected_value = data.get('selectedValue')

        # Based on selected_value, generate options for dropdown 2
        if selected_value == 'Class 9th':
            options = [
                {'value': 'Math', 'label': 'Mathematics'},
                {'value': 'Science', 'label': 'Science'},
            ]
        else:
            options = [{'value': 'NoData', 'label': 'No Data Available'}]
        
        return JsonResponse({'options': options})

@csrf_exempt
def get_options_for_dropdown3(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        selected_value = data.get('selectedValue')

        # Based on selected_value, generate options for dropdown 3
        options = [
            {'value': 'OptionA', 'label': 'Option A'},
            {'value': 'OptionB', 'label': 'Option B'},
        ]
        return JsonResponse({'options': options})

@csrf_exempt
def get_options_for_dropdown4(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        selected_value = data.get('selectedValue')

        # Based on selected_value, generate options for dropdown 4
        options = [
            {'value': 'Item1', 'label': 'Item 1'},
            {'value': 'Item2', 'label': 'Item 2'},
        ]
        return JsonResponse({'options': options})

@csrf_exempt
def api_endpoint(request):
    if request.method == 'POST':
        # Simulate a delay
        # time.sleep(2)

        # Extract data from POST request
        data = json.loads(request.body)
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
