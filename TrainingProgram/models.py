# models.py

from django.db import models

class TrainingProgram(models.Model):
    training_subject = models.CharField(max_length=200)
    prerequisites = models.TextField()
    training_organization = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()