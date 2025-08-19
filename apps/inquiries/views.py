from django.shortcuts import render

from rest_framework import generics
from rest_framework.views import APIView

from .models import Inquiries
from .serializers import InquiriesSerializer

# Create your views here.
class CreateInquiryAPIView(generics.CreateAPIView):
    serializer_class = InquiriesSerializer