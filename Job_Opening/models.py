from django.db import models

class Job_Opening(models.Model):
    Name_of_Company = models.CharField(max_length=200)
    Profile_Of_Company = models.CharField(max_length=200)
    Job_Profile = models.CharField(max_length=100)
    
    # Use choices for fields with predefined options
    BRANCH_CHOICES = [
        ("CSE", "Computer Science and Engineering"),
        ("ECE", "Electronics and Engineering"),
    ]
    Branch_Choice = models.CharField(max_length=50, choices=BRANCH_CHOICES)
    
    CTC = models.TextField()
    Eligibility_Criteria = models.TextField()
    
    SELECTION_CHOICES = [
        ("Virtual", "Virtual"),
        ("Offline", "Offline"),
    ]
    Selection = models.CharField(max_length=10, choices=SELECTION_CHOICES)
    
    Location = models.CharField(max_length=100)
    Stipend_per_month = models.IntegerField()
    Start_Date = models.DateField()
