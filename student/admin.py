from django.contrib import admin
from django.urls import path
from .views import ExcelGeneratorAdminView, export_student_data, export_job_data
from import_export.admin import ImportExportModelAdmin
from .models import Student, Job_Student_Application, Job_Opening

class CustomAdminSite(admin.AdminSite):
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('excel-generator/', self.admin_view(ExcelGeneratorAdminView.as_view()), name='excel_generator'),
            path('export-student-data/<int:student_id>/', export_student_data, name='export_student_data'),
            path('export-job-data/<int:job_id>/', export_job_data, name='export_job_data'),
        ]
        return custom_urls + urls

custom_admin_site = CustomAdminSite(name='custom_admin')

class StudentAdmin(ImportExportModelAdmin):
    list_display = ('username', 'email', 'Student_ID', 'Branch', 'CGPA', 'Block_All_Applications', 'Placed')
    search_fields = ('email', 'Student_ID', 'username')
    readonly_fields = ('id', 'date_joined')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

if admin.site.is_registered(Student):
    admin.site.unregister(Student)

custom_admin_site.register(Student, StudentAdmin)
custom_admin_site.register(Job_Student_Application)
custom_admin_site.register(Job_Opening)

if admin.site.is_registered(Student):
    admin.site.unregister(Student)
if admin.site.is_registered(Job_Student_Application):
    admin.site.unregister(Job_Student_Application)
if admin.site.is_registered(Job_Opening):
    admin.site.unregister(Job_Opening)

admin.site.register(Student, StudentAdmin)
admin.site.register(Job_Student_Application)
admin.site.register(Job_Opening)