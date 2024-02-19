from django.urls import path
from .views import register_job, register_training

urlpatterns = [
    path('job_openings/<int:pk>/register/', register_job, name='register_job'),
    path('training_programs/<int:pk>/register/', register_training, name='register_training')
]