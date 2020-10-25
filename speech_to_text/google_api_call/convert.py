import io
import os

# Imports the Google Cloud client library
from google.cloud import speech

### to indicate the api key
credential_path = "C:\the path to file.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path


def convert_to_text(audio):
    # Instantiates a client
    client = speech.SpeechClient()

    # The name of the audio file to transcribe
    #file_name = os.path.join(os.path.dirname(__file__), "C:\\Users\\hala\\Documents\\Ma formation", audio)

    # Loads the audio into memory
    #with io.open(file_name, "rb") as audio_file:
    content = audio.read()
    audio = speech.RecognitionAudio(content=content)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="en-US",
    )

    # Detects speech in the audio file
    response = client.recognize(config=config, audio=audio)

    return response
    #for result in response.results:
    #    print("Transcript: {}".format(result.alternatives[0].transcript))

