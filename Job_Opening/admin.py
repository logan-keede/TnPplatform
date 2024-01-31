from django.contrib import admin
from Job_Opening.models import Job_Opening

class JobAdmin(admin.ModelAdmin):
    list_display = ('Name_of_Company', 'Profile_Of_Company', 'Job_Profile', 'Branch_Choice', 'CTC', 'Eligibility_Criteria', 'Selection', 'Location', 'Stipend_per_month', 'Start_Date')

admin.site.register(Job_Opening,JobAdmin)

# Register your models here.
# admin.py
from django.contrib import admin
from .models import Job_Opening

class JobAdmin(admin.ModelAdmin):
    list_display = ('NameofCompany', 'profileOfCompany', 'JobProfile', 'BranchChoice', 'ctc', 'Eligibility', 'Selection', 'location', 'stipend', 'start')

admin.site.register(Job_Opening, JobAdmin)
