from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import os
from inspect import getsourcefile
from django.http import JsonResponse, QueryDict
import json
# Create your views here.

@login_required
def index(request):
    if request.method == "POST":
        # a = request.body.decode('utf-8');
        # print(request.__dict__['_post']);
        print(QueryDict(request.body).dict())

    
    return render(request, "Resume_generator.html")