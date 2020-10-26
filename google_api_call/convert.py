import os

from google.cloud import speech

# Indicate the api key
credential_path = "google_credentials.json"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credential_path


def convert_to_text(audio):
    client = speech.SpeechClient()

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        language_code="en-US",
    )
    # Detects speech in the audio file
    response = client.recognize(config=config, audio=audio)

    txt = "Empty"
    for result in response.results:
        txt += "Transcript: {}".format(result.alternatives[0].transcript)

    return txt
