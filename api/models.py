from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from student.models import Student
from allauth.socialaccount.models import SocialAccount


class JSON2pdf(models.Model):
    Student_Id = models.CharField(max_length=20, default = "studentID",unique = True)
    json = models.JSONField(default=dict)


class UserProfile(models.Model):
    user = models.OneToOneField(Student, on_delete=models.CASCADE)
    google_drive_credentials = models.TextField(null=True, blank=True)
    

# @receiver(post_save, sender = JSON2pdf)
# def create_profile(sender, instance, created, **kwargs):
#     # print("hell")
#     # if created:
#        # Grabbing data from social account to create profile for that user
#     profile=Student.objects.get(username=instance.Student_Id)
#     # profile.Student_ID = instance.user
#     # resume = JSON2pdf.objects.get_or_create(Student_Id=instance.user)
#     profile.resume_json = instance.json
#     profile.save()