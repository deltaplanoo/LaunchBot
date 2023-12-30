from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.http import HttpResponse

import json
from .launch import *

def index(request):
    if not results:
        return render(request, 'error.html')
    context = {'json_data': results}
    return render(request, 'index.html', context)

def upcoming(request):
    if not results:
        return render(request, 'error.html')
    context = {'json_data': results}
    return render(request, 'upcoming.html', context)

def past(request):
    if not past:
        return render(request, 'error.html')
    context = {'json_data': past}
    return render(request, 'past.html', context)


def spacex(request):
    if not results:
        return render(request, 'error.html')
    context = {'json_data': results}
    return render(request, 'spacex.html', context)

def starship(request):
    if not results:
        return render(request, 'error.html')
    context = {'json_data': results}
    return render(request, 'starship.html', context)

def launch_details(request):
    if request.method == 'POST':
        url_parameter = request.POST.get('url', '')
        custom = get_results(url_parameter)
        context = {'json_data': custom}
        return render(request, 'launch_details.html', context)
    else:
        # Handle other cases (e.g., redirect or show an error)
        return HttpResponse("Invalid request method")

"""     custom = get_results(url)
    context = {'json_data': split_datetime(custom)}
    return render(request, 'launch_details.html', context) """

def agency(request):
    if request.method == 'POST':
        url_parameter = request.POST.get('url', '')
        agency = get_results(url_parameter)
        context = {'json_data': agency}
        return render(request, 'launch_details.html', context)
    else:
        return HttpResponse("Invalid request method")