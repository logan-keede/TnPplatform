# TnPplatform/urls.py
from django.contrib import admin
from django.urls import path, include
from student.admin import custom_admin_site
from . import views
from student.views import index




urlpatterns = [
    path("admin/", admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('accounts/', include('allauth.socialaccount.urls')),
    path('', index, name='index'),
    path('', include('Announcement.urls')),
    path('', include('Job_Opening.urls')),
    path('', include('TrainingProgram.urls')),
    path('admin/', include('student.urls')),
    path('admin/student/', custom_admin_site.urls),
    path('student/', include('student.urls')),
]
