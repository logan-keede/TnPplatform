# admin.py
from django.contrib import admin
from .models import Job_Opening, JobApplication

class JobApplicationInline(admin.TabularInline):
    model = JobApplication
    extra = 0
    fields = ['user', 'status']

class JobAdmin(admin.ModelAdmin):
    list_display = ('NameofCompany', 'profileOfCompany', 'JobProfile', 'BranchChoice', 'ctc', 'Eligibility', 'Selection', 'location', 'stipend', 'start')
    inlines = [JobApplicationInline]

admin.site.register(Job_Opening, JobAdmin)
admin.site.register(JobApplication)
