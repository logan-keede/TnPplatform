from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TrainingProgramViewSet

router = DefaultRouter()
router.register(r'training_program', TrainingProgramViewSet, basename='job_opening')

urlpatterns = [
    path('', include(router.urls)),
]