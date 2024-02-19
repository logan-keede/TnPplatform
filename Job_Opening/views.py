from rest_framework import viewsets
from django.shortcuts import render, get_object_or_404

from student.models import Job_Student_Application
from .models import Job_Opening
from .serializer import JobOpeningSerializer

class JobOpeningViewSet(viewsets.ModelViewSet):
    queryset = Job_Opening.objects.all()
    serializer_class = JobOpeningSerializer

def job_opening_detail(request, pk):
    job = get_object_or_404(Job_Opening, pk=pk)
    user_has_registered = Job_Student_Application.objects.filter(Student_ID=request.user, Job_ID=job).exists()
    return render(request, 'job_detail.html', {'job': job, 'user_has_registered': user_has_registered})