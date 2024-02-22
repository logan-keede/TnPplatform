from rest_framework import serializers

from .models import JSON2pdf


class JSON2pdfSerializer(serializers.ModelSerializer):
    class Meta:
        model = JSON2pdf
        fields = '__all__'

    def create(self, validated_data):
        student_id = validated_data.get('Student_Id')
        existing_student = JSON2pdf.objects.filter(Student_Id=student_id).first()

        if existing_student:
            # Update other fields if the student already exists
            existing_student.json = validated_data.get('json', existing_student.json)
            # Update other fields as needed

            existing_student.save()
            return existing_student
        else:
            return super().create(validated_data)