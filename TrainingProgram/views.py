from django.shortcuts import render
from rest_framework import viewsets
from .models import TrainingProgram
from .serializer import TrainingProgramSerializer
from student.models import Student_Training_Registration
from django.shortcuts import get_object_or_404

# Create your views here.

class TrainingProgramViewSet(viewsets.ModelViewSet):
    queryset = TrainingProgram.objects.all()
    serializer_class = TrainingProgramSerializer

def training_program_detail(request, pk):
    training_program = get_object_or_404(TrainingProgram, pk=pk)
    user_has_registered = Student_Training_Registration.objects.filter(Student_ID=request.user, Training_ID=training_program).exists()
    return render(request, 'training_program_detail.html', {'training_program': training_program, 'user_has_registered': user_has_registered})