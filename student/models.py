from django.db import models
from TrainingProgram.models import TrainingProgram
from Job_Opening.models import Job_Opening

# Create your models here.
class Student(models.Model):
    First_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    Student_ID = models.CharField(max_length=8)
    Email = models.EmailField()

    BRANCH_CHOICES = [
        ("CSE", "Computer Science and Engineering"),
        ("ECE", "Electronics and Engineering"),
    ]

    Branch = models.CharField(max_length=50, choices=BRANCH_CHOICES)
    Resume_Link = models.CharField(max_length=300)
    CGPA = models.DecimalField(max_digits = 3, decimal_places = 2)
    Block_All_Applications = models.BooleanField()
    Placed = models.ForeignKey(Job_Opening, null = True, blank = True, on_delete = models.CASCADE)
    Access_Token = models.CharField(max_length=300)

class Student_Training_Registration(models.Model):
    Student_ID = models.ForeignKey(Student,on_delete = models.CASCADE)
    Training_ID = models.ForeignKey(TrainingProgram, on_delete = models.CASCADE)
    Attended = models.BooleanField()

class Job_Student_Application(models.Model):
    Student_ID = models.ForeignKey(Student, on_delete = models.CASCADE)
    Job_ID = models.ForeignKey(Job_Opening, on_delete = models.CASCADE)
    Blocked = models.BooleanField()
    Status = models.CharField(max_length = 1)