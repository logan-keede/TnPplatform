from rest_framework import viewsets
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Announcement
from .serializer import AnnouncementSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

class AnnouncementViewSet(viewsets.ModelViewSet):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    
@api_view(['GET'])
def announcement_detail(request, pk):
    announcement = get_object_or_404(Announcement, pk=pk)
    return render(request, 'announcement_detail.html', {'announcement': announcement})