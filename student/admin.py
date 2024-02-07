from django.contrib import admin
from .models import *

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ('First_Name', 'Last_Name', 'Student_ID', 'Email', 'Branch', 'Resume_Link', 'CGPA', 'Block_All_Applications','Placed', 'Access_Token')

class TrainingRegAdmin(admin.ModelAdmin):
    list_display = ('Student_ID','Training_ID','Attended')

class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('Student_ID','Job_ID','Blocked', 'Status')

admin.site.register(Student, StudentAdmin)
admin.site.register(Student_Training_Registration, TrainingRegAdmin)
admin.site.register(Job_Student_Application, JobApplicationAdmin)