from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from api.serializer import JSON2pdfSerializer
from api.models import JSON2pdf
from api.utils import generate_pdf, store_pdf_in_drive
import os
from inspect import getsourcefile
import requests
import json
# Create your views here.

@login_required
def index(request):
    if request.method == "POST":

        jsonData = json.loads(request.body.decode('utf-8')) 
        serializedJson = JSON2pdfSerializer(data=jsonData)
        if serializedJson.is_valid():
            json_file = serializedJson.validated_data['json'][0]
            json2pdf_instance = JSON2pdf(json = json_file)
            json2pdf_instance.save()
            pdf_file = './Resume.pdf'
            pdf_data = generate_pdf(json_file, pdf_file)
            
            x =store_pdf_in_drive(request.user, pdf_data, file_name='Resume.pdf')
            print(x)
        else :
            print(serializedJson.errors)
    
    return render(request, "Resume_generator.html") 