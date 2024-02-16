'''from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Announcement
from .serializer import AnnouncementSerializer
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView

class AnnouncementViewSet(APIView):
    @csrf_exempt
    def get(self, request, *args, **kwargs):
        announcements = Announcement.objects.all()
        serializer = AnnouncementSerializer(announcements, many=True)
        return JsonResponse(serializer.data, safe=False)

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        data = JSONParser().parse(request)
        serializer = AnnouncementSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    @csrf_exempt
    def put(self, request, *args, **kwargs):
        data = JSONParser().parse(request)
        announcement = get_object_or_404(Announcement, pk=kwargs.get('pk'))
        serializer = AnnouncementSerializer(announcement, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    @csrf_exempt
    def patch(self, request, *args, **kwargs):
        data = JSONParser().parse(request)
        announcement = get_object_or_404(Announcement, pk=kwargs.get('pk'))
        serializer = AnnouncementSerializer(announcement, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    @csrf_exempt
    def delete(self, request, *args, **kwargs):
        announcement = get_object_or_404(Announcement, pk=kwargs.get('pk'))
        announcement.delete()
        return JsonResponse({'detail': 'Deleted successfully'}, status=204)'''

from rest_framework import viewsets
from .models import Announcement
from .serializer import AnnouncementSerializer

class AnnouncementViewSet(viewsets.ModelViewSet):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer