from django.db import models

class Job_Opening(models.Model):
    NameofCompany = models.CharField(max_length=200)
    profileOfCompany = models.CharField(max_length=200)
    JobProfile = models.CharField(max_length=100)
    
    # Use choices for fields with predefined options
    BRANCH_CHOICES = [
        ("CSE", "Computer Science and Engineering"),
        ("ECE", "Electronics and Engineering"),
    ]
    BranchChoice = models.CharField(max_length=50, choices=BRANCH_CHOICES)
    
    ctc = models.TextField()
    Eligibility = models.TextField()
    
    SELECTION_CHOICES = [
        ("Virtual", "Virtual"),
        ("Offline", "Offline"),
    ]
    Selection = models.CharField(max_length=10, choices=SELECTION_CHOICES)
    
    location = models.CharField(max_length=100)
    stipend = models.IntegerField()
    start = models.DateField()
