from rest_framework import serializers

from .models import JSON2pdf


class JSON2pdfSerializer(serializers.ModelSerializer):
    class Meta:
        model = JSON2pdf
        fields = '__all__'