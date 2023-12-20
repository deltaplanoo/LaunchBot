from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
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

def launch_details(request, pk):
    launch = get_object_or_404(Launch, pk=pk)
    return render(request, 'launch_details.html', {'launch': launch})
