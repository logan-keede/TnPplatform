from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from Job_Opening.models import Job_Opening
from TrainingProgram.models import TrainingProgram
from .models import Job_Student_Application, Student_Training_Registration
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.utils import timezone

# Create your views here.
def index(request):
    return HttpResponse("this is student page")

@login_required
def register_job(request, pk):
    job = get_object_or_404(Job_Opening, pk=pk)

    if job.end_of_registration < timezone.now().date():
        return HttpResponse('Registration for this job opening has closed.')
    
    Job_Student_Application.objects.create(Student_ID=request.user, Job_ID=job, Blocked=False, Status='A')
    return JsonResponse({'status': 'success'})

@login_required
def register_training(request,pk):
    trainingProgram = get_object_or_404(TrainingProgram, pk=pk)
    Student_Training_Registration.objects.create(Student_ID=request.user, Training_ID=trainingProgram, Attended=False)
    return JsonResponse({'status': 'success'})

