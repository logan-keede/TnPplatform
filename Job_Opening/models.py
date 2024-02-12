from django.db import models
from django.contrib.auth.models import User

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

    def has_user_applied(self, user):
        return self.jobapplication_set.filter(user=user).exists()

class JobApplication(models.Model):
    STATUS_CHOICES = [
        ('P', 'Pending'),
        ('A', 'Accepted'),
        ('R', 'Rejected'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job_opening = models.ForeignKey(Job_Opening, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')
    class Meta:
        unique_together = ('user', 'job_opening')
    # Add more fields as needed