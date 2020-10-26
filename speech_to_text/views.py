import io

from google.cloud import speech
from django.shortcuts import render
from django.contrib.staticfiles import finders

from google_api_call.convert import convert_to_text


def index(request):
    file_name = "OSR_us_000_0010_8k.wav"
    file_system_path = finders.find(file_name)

    with io.open(file_system_path, "rb") as audio_file:
        content = audio_file.read()
        audio = speech.RecognitionAudio(content=content)

    text = convert_to_text(audio)

    context = {"text": text}
    return render(request, "page.html", context)
