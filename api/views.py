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
from student.models import Student

# class JSON2pdfView(APIView):
#     def post(self, request, format=None):
#         request.data["Student_Id"] = Student.objects.get(username = request.user).Student_ID 
#         serializer = JSON2pdfSerializer(data=request.data)
#         if serializer.is_valid():
#             json_file = serializer.validated_data['json'][0]
#             Student_Id =  serializer.validated_data['Student_Id']
#             # print(json_file["Name"])  
#             json2pdf_instance = JSON2pdf.objects.get_or_create(Student_Id= Student_Id)
#             json2pdf_instance.json = json_file
#             json2pdf_instance.save()
#             pdf_file = './Resume.pdf'  # or determine the path dynamically
#             pdf_data = generate_pdf(json_file, pdf_file)
 
#             print(request.user)
#              # Load your credentials from the 'token.json' file
#             # creds = get_google_drive_credentials(request.user)

#             x =store_pdf_in_drive(request.user, pdf_data, file_name='Resume.pdf')
#             # Call the Drive v3 API
#             # # service = build('drive', 'v3', credentials=creds)

#             # # # Create a media object from the byte stream
#             # # media = MediaIoBaseUpload(BytesIO(pdf_data), mimetype='application/pdf')

#             # # # Upload the file to Google Drive
#             # # file_metadata = {'name': 'Resume.pdf'}
#             # file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
#             print(x)

#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class JSON2pdfView(APIView):

    def post(self, request, format=None):
        student_id = Student.objects.get(username=request.user).Student_ID

        serializer = JSON2pdfSerializer(student_id=student_id, data=request.data)

        if serializer.is_valid():
            json_file = serializer.validated_data['json'][0]

            # Attempt to get an existing instance or create a new one
            json2pdf_instance, created = JSON2pdf.objects.get_or_create(Student_Id=student_id)

            # Update the json field and save the instance
            json2pdf_instance.json = json_file
            json2pdf_instance.save()


            pdf_file = './Resume.pdf'  # or determine the path dynamically
            pdf_data = generate_pdf(json_file, pdf_file)

            # Call the function to store PDF in Google Drive
            # st = Student.objects.get(Student_ID=student_id)
            # st.Resume_Link = "https://drive.google.com/file/d/"+x 
            x = store_pdf_in_drive(request.user, pdf_data, file_name='Resume.pdf')
            st = Student.objects.get(Student_ID=student_id)
            st.Resume_Link = "https://drive.google.com/file/d/"+x 
            st.resume_json = json_file
            st.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
