from rest_framework import viewsets
from .models import Job_Opening
from .serializer import JobOpeningSerializer

class JobOpeningViewSet(viewsets.ModelViewSet):
    queryset = Job_Opening.objects.all()
    serializer_class = JobOpeningSerializer