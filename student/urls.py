from django.urls import path
from .views import ExcelGeneratorAdminView, export_student_data, export_job_data

urlpatterns = [
    path('excel-generator/', ExcelGeneratorAdminView.as_view(), name='excel_generator'),
    path('export-student-data/<str:student_id>/', export_student_data, name='export_student_data'),
    path('export-job-data/<int:job_id>/', export_job_data, name='export_job_data'),
    
]
