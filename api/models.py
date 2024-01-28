from django.db import models
from django.contrib.auth.models import User
class JSON2pdf(models.Model):
    json=models.JSONField()

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    google_drive_credentials = models.TextField(null=True, blank=True)
    