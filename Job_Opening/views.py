'''from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Job_Opening
from .serializer import JobOpeningSerializer

class JobOpeningViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Job_Opening.objects.all()
        serializer = JobOpeningSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = JobOpeningSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk=None):
        queryset = Job_Opening.objects.all()
        job_opening = get_object_or_404(queryset, pk=pk)
        serializer = JobOpeningSerializer(job_opening)
        return Response(serializer.data)

    def put(self, request, pk=None):
        queryset = Job_Opening.objects.all()
        job_opening = get_object_or_404(queryset, pk=pk)
        serializer = JobOpeningSerializer(job_opening, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk=None):
        queryset = Job_Opening.objects.all()
        job_opening = get_object_or_404(queryset, pk=pk)
        serializer = JobOpeningSerializer(job_opening, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        #queryset = Job_Opening.objects.all()
        job_opening = get_object_or_404(Job_Opening, pk=kwargs.get('pk'))
        print(Job_Opening.objects.all())
        job_opening.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Job_Opening
from .serializer import JobOpeningSerializer
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class JobOpeningViewSet(APIView):
    @csrf_exempt
    def get(self, request, *args, **kwargs):
        Job_Openings = Job_Opening.objects.all()
        serializer = JobOpeningSerializer(Job_Openings, many=True)
        return JsonResponse(serializer.data, safe=False)

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        data = JSONParser().parse(request)
        serializer = JobOpeningSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    @csrf_exempt
    def put(self, request, *args, **kwargs):
        data = JSONParser().parse(request)
        Job_Opening = get_object_or_404(Job_Opening, pk=kwargs.get('pk'))
        serializer = JobOpeningSerializer(Job_Opening, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    @csrf_exempt
    def patch(self, request, *args, **kwargs):
        data = JSONParser().parse(request)
        Job_Opening = get_object_or_404(Job_Opening, pk=kwargs.get('pk'))
        serializer = JobOpeningSerializer(Job_Opening, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    @csrf_exempt
    def delete(self, request, *args, **kwargs):
        print("Hey")
        job_opening = get_object_or_404(Job_Opening, pk=kwargs.get('pk'))
        job_opening.delete()
        return JsonResponse({'detail': 'Deleted successfully'}, status=204)'''

    #def destroy(self, request, *args, **kwargs):
    #    job_opening = self.get_object()
    #    job_opening.delete()
    #    return Response(status=status.HTTP_204_NO_CONTENT)

from rest_framework import viewsets
from .models import Job_Opening
from .serializer import JobOpeningSerializer

class JobOpeningViewSet(viewsets.ModelViewSet):
    queryset = Job_Opening.objects.all()
    serializer_class = JobOpeningSerializer