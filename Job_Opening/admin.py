# admin.py
from django.contrib import admin
from .models import Job_Opening 


class JobAdmin(admin.ModelAdmin):
    list_display = ('NameofCompany', 'profileOfCompany', 'JobProfile', 'BranchChoice', 'ctc', 'Eligibility', 'Selection', 'location', 'stipend', 'join_date','end_of_registration')

admin.site.register(Job_Opening, JobAdmin)
