from django.shortcuts import render
from rest_framework import viewsets
from .models import TrainingProgram
from .serializer import TrainingProgramSerializer

# Create your views here.

class TrainingProgramViewSet(viewsets.ModelViewSet):
    queryset = TrainingProgram.objects.all()
    serializer_class = TrainingProgramSerializer