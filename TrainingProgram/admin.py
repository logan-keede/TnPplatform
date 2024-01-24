from django.contrib import admin
from TrainingProgram.models import TrainingProgram

class TrainingProgramAdmin(admin.ModelAdmin):
    list_display = ('training_subject', 'prerequisites', 'training_organization', 'start_date', 'end_date')

admin.site.register(TrainingProgram, TrainingProgramAdmin)
# Register your models here.
