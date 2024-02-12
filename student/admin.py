from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

# Register your models here.
class StudentAdmin(UserAdmin):
    list_display = ('username','email','first_name','last_name','Student_ID', 'Branch', 'Resume_Link', 'CGPA', 'Block_All_Applications','Placed', 'Access_Token','resume_json')

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Student info', {'fields': ('Student_ID', 'Branch', 'Resume_Link', 'CGPA', 'Block_All_Applications','Placed')}),
    )

class TrainingRegAdmin(admin.ModelAdmin):
    list_display = ('Student_ID','Training_ID','Attended')

class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('Student_ID','Job_ID','Blocked', 'Status')

admin.site.register(Student, StudentAdmin)
admin.site.register(Student_Training_Registration, TrainingRegAdmin)
admin.site.register(Job_Student_Application, JobApplicationAdmin)