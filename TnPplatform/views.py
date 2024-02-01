from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import os
from inspect import getsourcefile
# Create your views here.

@login_required
def index(request):
    if request == "POST":
        pass    
    
    return render(request, "Resume_generator.html")