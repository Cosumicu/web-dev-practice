from django.core.mail import send_mail
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from real_estate.settings.development import DEFAULT_FROM_EMAIL

from .models import Inquiry


@api_view(["POST"])
@permission_classes([permissions.AllowAny])
def send_inquiry_email(request):
    data = request.data

    try:
        subject = data["subject"]
        name = data["name"]
        email = data["email"]
        message = data["message"]
        from_email = data["email"]
        recipient_list = [DEFAULT_FROM_EMAIL]

        send_mail(subject, message, from_email, recipient_list, fail_silently=True)

        enquiry = Inquiry(name=name, email=email, subject=subject, message=message)
        enquiry.save()

        return Response({"success": "Your Inquiry was successfully submitted"})

    except:
        return Response({"fail": "Inquiry was not sent. Please try again"})