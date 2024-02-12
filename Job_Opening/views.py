from django.db import IntegrityError
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from .models import Job_Opening, JobApplication
from django.shortcuts import render, get_object_or_404, redirect
# Create your views here.

def job_openings(request):
    job_openings = Job_Opening.objects.all()
    return render(request, 'jobs.html', {'jobs':job_openings})

def job_detail(request, job_id):
    job = get_object_or_404(Job_Opening, pk=job_id)
    has_applied = job.jobapplication_set.filter(user=request.user).exists()
    if request.method == 'POST':
        try:
            JobApplication.objects.create(user=request.user, job_opening=job)
            return redirect('job_openings')
        except IntegrityError:
            messages.error(request, 'You have already registered for this job.')
    return render(request, 'job_detail.html', {'job': job, 'has_applied': has_applied})
