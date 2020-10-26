from django.urls import path
from speech_to_text.views import *


urlpatterns = [
    path("", index, name="index"),
]
