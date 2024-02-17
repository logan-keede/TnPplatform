from typing import Any
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
# from rest_framework.authtoken.models import Token
from allauth.socialaccount.models import SocialAccount, SocialApp, SocialToken
from allauth.account.models import EmailAddress
from django.contrib.sites.models import Site
from django.db.models.query import QuerySet
from .models import *

# define your filters here

class YearFilter(admin.SimpleListFilter):

    # heading of the filter
    title = "year"

    # name passed in url of query
    parameter_name = "year"

    def lookups(self, request, model_admin):
        """
        this is the list where the values on the right side are the filter option's names.
        """
        return [
            (('UI20'),('4th Year')),
            (('UI21'),('3rd Year')),
            (('UI22'),('2nd Year')),
            (('UI23'),('1st Year')),
        ]
    
    def queryset(self, request, queryset):
        if self.value() == '':
            return queryset
        
        # returns entries for 4th year
        if self.value() == 'UI20':
            return queryset.filter(Student_ID__startswith = 'UI20')
        
        # returns entries for 3rd year
        if self.value() == 'UI21':
            return queryset.filter(Student_ID__startswith = 'UI21')
        
        # returns entries for 2nd year
        if self.value() == 'UI22':
            return queryset.filter(Student_ID__startswith = 'UI22')
        
        # returns entries for 1st year
        if self.value() == 'UI23':
            return queryset.filter(Student_ID__startswith = 'UI23')
    
class PlacedFilter(admin.SimpleListFilter):

    # heading of the filter
    title = "Placements"

    # name passed in url of query
    parameter_name = "placed"

    def lookups(self, request, model_admin):
        """
        this is the list where the values on the right side are the filter option's names.
        """
        return [
            (('not_placed'),('not placed')),
            (('placed'),('placed')),
        ]
    
    def queryset(self, request, queryset):
        if self.value() == '':
            return queryset
        
        if self.value() == 'placed':
            return queryset.exclude(Placed = None) 
        
        if self.value() == 'not_placed':
            return queryset.filter(Placed = None) 

class PackageCategoryFilter(admin.SimpleListFilter):
    
    # heading of the filter
    title = "Package Category"

    # name passed in url of query
    parameter_name = "category"

    def lookups(self, request, model_admin):
        """
        this is the list where the values on the right side are the filter option's names.
        """
        return [
            (('A'),('A')),
            (('B'),('B')),
        ]
    
    def queryset(self, request, queryset):
        if self.value() == '':
            return queryset
        
        if self.value() == 'A':
            return queryset.filter(CGPA__gte = 7.5) 
        
        if self.value() == 'B':
            return queryset.filter(CGPA__lt = 7.5)

# Register your models here.
class StudentAdmin(UserAdmin):

    list_filter = ("Branch",YearFilter, PlacedFilter, PackageCategoryFilter)

    list_display = ('username','email','first_name','last_name','Student_ID', 'Branch', 'Resume_Link', 'CGPA', 'Block_All_Applications','Placed', 'Access_Token','resume_json')


    # list_editable = ('Student_ID',)

    ordering = ("email",)

    fieldsets = (
        (None, {'fields': ('username','email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Student info', {'fields': ('Student_ID', 'Branch', 'Resume_Link', 'CGPA', 'Block_All_Applications','Placed')}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions"
            )}
        ),
    )
    search_fields = ("username","email", "Branch", "Student_ID")

class TrainingRegAdmin(admin.ModelAdmin):
    list_display = ('Student_ID','Training_ID','Attended')
    search_fields = ('Student_ID', 'Training_ID')

class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('Student_ID','Job_ID','Blocked', 'Status')
    search_fields = ('Student_ID', 'Job_ID')

admin.site.register(Student, StudentAdmin)
admin.site.register(Student_Training_Registration, TrainingRegAdmin)
admin.site.register(Job_Student_Application, JobApplicationAdmin)

admin.site.unregister(SocialAccount)
# admin.site.unregister(SocialApp)
admin.site.unregister(SocialToken)
# admin.site.unregister(Site)
admin.site.unregister(Group)
admin.site.unregister(EmailAddress)
# admin.site.unregister(Token)