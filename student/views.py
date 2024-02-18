import pandas as pd
from django.http import HttpResponse
from django.views import View
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404
from .models import Student, Job_Student_Application, Job_Opening
import io
import os

@method_decorator(staff_member_required, name='dispatch')
class ExcelGeneratorAdminView(View):
    def get(self, request):
        students = Student.objects.all()

        data = {
            'Student ID': [student.Student_ID for student in students],
            'Name': [f"{student.first_name} {student.last_name}" for student in students],
            'Branch': [student.Branch for student in students],
            'CGPA': [student.CGPA for student in students],
        }

        df = pd.DataFrame(data)

        excel_buffer = io.BytesIO()
        df.to_excel(excel_buffer, index=False, sheet_name='Students')
        excel_buffer.seek(0)

        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=student_data.xlsx'
        response.write(excel_buffer.read())

        return response

def export_student_data(request, student_id):
    student = get_object_or_404(Student, Student_ID=student_id)
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
    with pd.ExcelWriter('student_data.xlsx', engine='xlsxwriter') as writer:
        student_df.to_excel(writer, index=False, sheet_name='Sheet1', startrow=0)
        pd.DataFrame([[]]).to_excel(writer, index=False, sheet_name='Sheet1', startrow=student_df.shape[0] + 2)
        job_df[['S.No', 'Job ID', 'Company', 'Position']].to_excel(writer, index=False, sheet_name='Sheet1', startrow=student_df.shape[0] + 3)

    file_path = 'student_data.xlsx'

    with open(file_path, 'rb') as excel_file:
        response = HttpResponse(excel_file.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = f'attachment; filename=student_data_{student_id}.xlsx'

    os.remove(file_path)

    return response


def export_job_data(request, job_id):
    job = get_object_or_404(Job_Opening, id=job_id)
    applicants = Job_Student_Application.objects.filter(Job_ID=job)

    job_info = {
        'Job ID': [job.id],
        'Company': [job.NameofCompany],
        'Profile': [job.JobProfile],
        'CTC': [job.ctc],
    }
    job_df = pd.DataFrame(job_info)

    student_details = {
        'S.No': list(range(1, len(applicants) + 1)), 
        'Student ID': [app.Student_ID.Student_ID for app in applicants],
        'Username': [app.Student_ID.username for app in applicants],
        'Email': [app.Student_ID.email for app in applicants],
        'Branch': [app.Student_ID.Branch for app in applicants],
    }
    student_df = pd.DataFrame(student_details)

    student_df['S.No'] = range(1, len(student_df) + 1)

    with pd.ExcelWriter('job_data.xlsx', engine='xlsxwriter') as writer:
        job_df.to_excel(writer, index=False, sheet_name='Sheet1', startrow=0)
        pd.DataFrame([[]]).to_excel(writer, index=False, sheet_name='Sheet1', startrow=job_df.shape[0] + 2)
        pd.DataFrame([['Student Applications']]).to_excel(writer, index=False, sheet_name='Sheet1', startrow=job_df.shape[0] + 3)
        student_df.to_excel(writer, index=False, sheet_name='Sheet1', startrow=job_df.shape[0] + 4)

    file_path = 'job_data.xlsx'

    with open('job_data.xlsx', 'rb') as excel_file:
        response = HttpResponse(excel_file.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = f'attachment; filename=job_data_{job_id}.xlsx'
    
    os.remove(file_path)

    return response