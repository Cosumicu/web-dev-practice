from django import path

from . import views

urlpatterns = [
    path("", views.send_inquiry_email, name="send-inquiry")
]