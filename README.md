# Text to Speech converter 

## get started 

1- Get your google credentials, paste them to the JSON file called `google_credentials.json`

```text
├── Pipfile
├── Pipfile.lock
├── README.md
├── converter
├── db.sqlite3
├── google_api_call
├── google_credentials.json   <--- here
├── manage.py
└── speech_to_text
```

2- then,
```bash
pipenv shell

python manage.py migrate

python manage.py runserver
```

now, visit http://127.0.0.1:8000/

you should expect something like this:

```markdown
# Welcome to the txtToSpeech converter!!
you should expect something like that:
----------------------
EmptyTranscript: the Birch canoes slid on the smooth planksTranscript: glue the sheet to the dark blue backgroundTranscript: it is easy to tell the death of a well.Transcript: These days a chicken leg is a verb dish.Transcript: Rice is often served in round bowls.Transcript: The juice of lemons makes find punch.Transcript: The box was down beside the park truck.Transcript: the Hogs of sub shop corn and garbageTranscript: 4 hours of study work fastestTranscript: a large size in stockings is hard to sell.
----------------------

### the output of this audio file is:
EmptyTranscript: the Birch canoes slid on the smooth planksTranscript: glue the sheet to the dark blue backgroundTranscript: it is easy to tell the death of a well.Transcript: These days a chicken leg is a verb dish.Transcript: Rice is often served in round bowls.Transcript: The juice of lemons makes find punch.Transcript: The box was down beside the park truck.Transcript: the Hogs of sub shop corn and garbageTranscript: 4 hours of study work fastestTranscript: a large size in stockings is hard to sell.
```