from rest_framework import serializers
from .models import Job_Opening

class JobOpeningSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job_Opening
        fields = '__all__'