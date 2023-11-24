from django.shortcuts import render
from django.http import JsonResponse
import json
from .launch import *

def index(request):

    if not results:
        return render(request, 'error.html')
    
    context = {'json_data': results}

    return render(request, 'index.html', context)
