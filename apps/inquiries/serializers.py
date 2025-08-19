from rest_framework import serializers

from .models import Inquiries

class InquiriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inquiries
        fields = "__all__"