from django_countries.serializer_fields import CountryField
from rest_framework import serializers

from apps.ratings.serializers import RatingSerializer
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username")
    first_name = serializers.CharField(source="user.first_name")
    
