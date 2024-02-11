'''from rest_framework import viewsets

from .serializer import JSON2pdfSerializer
from main.models import JSON2pdf


class JSON2pdfViewSet(viewsets.ModelViewSet):
    queryset = JSON2pdf.objects.all()
    serializer_class = JSON2pdfSerializer'''

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import JSON2pdfSerializer
from allauth.socialaccount.models import SocialAccount
from google.oauth2.credentials import Credentials
# from .sample import generate_pdf

# from django.templatetags.static import static

from .models import JSON2pdf
from .utils import generate_pdf, store_pdf_in_drive

from io import BytesIO

from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseUpload
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.http import HttpResponse


class JSON2pdfView(APIView):
    def post(self, request, format=None): 
        serializer = JSON2pdfSerializer(data=request.data)
        if serializer.is_valid():
            json_file = serializer.validated_data['json'][0]
            # print(json_file["Name"])  
            json2pdf_instance = JSON2pdf(json = json_file)
            json2pdf_instance.save()
            pdf_file = './Resume.pdf'  # or determine the path dynamically
            pdf_data = generate_pdf(json_file, pdf_file)
 
             # Load your credentials from the 'token.json' file
            # creds = get_google_drive_credentials(request.user)

            x =store_pdf_in_drive(request.user, pdf_data, file_name='Resume.pdf')
            # Call the Drive v3 API
            # # service = build('drive', 'v3', credentials=creds)

            # # # Create a media object from the byte stream
            # # media = MediaIoBaseUpload(BytesIO(pdf_data), mimetype='application/pdf')

            # # # Upload the file to Google Drive
            # # file_metadata = {'name': 'Resume.pdf'}
            # file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
            print(x)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
