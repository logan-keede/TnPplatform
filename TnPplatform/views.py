from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import os
from inspect import getsourcefile
from django.http import JsonResponse
import json
# Create your views here.

@login_required
def index(request):
    if request.method == "POST":
        print(request.body)

    
    return render(request, "Resume_generator.html")