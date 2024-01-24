from django.shortcuts import render
from TrainingProgram.models import TrainingProgram

def index(request):
    training_programs = TrainingProgram.objects.all()

    return render(request, 'training.html', {'training_programs': training_programs})


# Create your views here.
