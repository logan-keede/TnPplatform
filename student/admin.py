from django.contrib import admin
from django.urls import path
import pandas as pd
# from .views import export_student_data
from .models import Student, Job_Student_Application, Job_Opening
import io
import os
import zipfile
from django.http import HttpResponse
from Job_Opening.admin import JobAdmin

def export_student_data(modeladmin, request, queryset):
    zip_buffer = io.BytesIO()

    with zipfile.ZipFile(zip_buffer, 'a', zipfile.ZIP_DEFLATED, False) as zip_file:
        for student in queryset:
            applications = Job_Student_Application.objects.filter(Student_ID=student)

            student_info = {
                'Student ID': [student.Student_ID],
                'Username': [student.username],
                'Email': [student.email],
                'Branch': [student.Branch],
            }
            student_df = pd.DataFrame(student_info)

            job_details = {
                'Job ID': [app.Job_ID.id if app.Job_ID else "N/A" for app in applications],
                'Company': [app.Job_ID.NameofCompany if app.Job_ID else "N/A" for app in applications],
                'Position': [app.Job_ID.JobProfile if app.Job_ID else "N/A" for app in applications],
            }
            job_df = pd.DataFrame(job_details)

            job_df['S.No'] = range(1, len(job_df) + 1)
            
            excel_buffer = io.BytesIO()
            with pd.ExcelWriter(excel_buffer, engine='xlsxwriter') as writer:
                student_df.to_excel(writer, index=False, sheet_name=f'Student_{student.Student_ID}', startrow=0)
                pd.DataFrame([[]]).to_excel(writer, index=False, sheet_name=f'Student_{student.Student_ID}', startrow=student_df.shape[0] + 2)
                job_df[['S.No', 'Job ID', 'Company', 'Position']].to_excel(writer, index=False, sheet_name=f'Student_{student.Student_ID}', startrow=student_df.shape[0] + 3)

            zip_file.writestr(f'student_data_{student.Student_ID}.xlsx', excel_buffer.getvalue())

    zip_buffer.seek(0)
    response = HttpResponse(zip_buffer.read(), content_type='application/zip')
    response['Content-Disposition'] = 'attachment; filename=students_data.zip'

    return response

export_student_data.short_description = "Export selected students' data"

# def export_job_data(modeladmin, request, queryset):
#     zip_buffer = io.BytesIO()

#     with zipfile.ZipFile(zip_buffer, 'a', zipfile.ZIP_DEFLATED, False) as zip_file:
#         for job in queryset:
#             applicants = Job_Student_Application.objects.filter(Job_ID=job)

#             job_info = {
#                 'Job ID': [job.id],
#                 'Company': [job.NameofCompany],
#                 'Profile': [job.JobProfile],
#                 'CTC': [job.ctc],
#             }
#             job_df = pd.DataFrame(job_info)

#             student_details = {
#                 'S.No': list(range(1, len(applicants) + 1)),
#                 'Student ID': [app.Student_ID.Student_ID for app in applicants],
#                 'Username': [app.Student_ID.username for app in applicants],
#                 'Email': [app.Student_ID.email for app in applicants],
#                 'Branch': [app.Student_ID.Branch for app in applicants],
#             }
#             student_df = pd.DataFrame(student_details)

#             student_df['S.No'] = range(1, len(student_df) + 1)

#             excel_buffer = io.BytesIO()
#             with pd.ExcelWriter(excel_buffer, engine='xlsxwriter') as writer:
#                 job_df.to_excel(writer, index=False, sheet_name=f'Job_{job.id}', startrow=0)
#                 pd.DataFrame([[]]).to_excel(writer, index=False, sheet_name=f'Job_{job.id}', startrow=job_df.shape[0] + 2)
#                 student_df.to_excel(writer, index=False, sheet_name=f'Job_{job.id}', startrow=job_df.shape[0] + 3)

#             zip_file.writestr(f'job_data_{job.id}.xlsx', excel_buffer.getvalue())

#     zip_buffer.seek(0)
#     response = HttpResponse(zip_buffer.read(), content_type='application/zip')
#     response['Content-Disposition'] = 'attachment; filename=jobs_data.zip'

#     return response

# export_job_data.short_description = "Export selected jobs' data"

class StudentAdmin(admin.ModelAdmin):
    actions = [export_student_data]
    list_display = ('Student_ID', 'username', 'email', 'Branch')
#class JobAdmin(admin.ModelAdmin):
#     actions = [export_job_data]
#     list_display = ('id', 'NameofCompany', 'JobProfile', 'ctc')

if admin.site.is_registered(Student):
    admin.site.unregister(Student)

if admin.site.is_registered(Job_Student_Application):
    admin.site.unregister(Job_Student_Application)

if admin.site.is_registered(Job_Opening):
    admin.site.unregister(Job_Opening)

admin.site.register(Student, StudentAdmin)
admin.site.register(Job_Student_Application)
admin.site.register(Job_Opening, JobAdmin)