from openai import OpenAI
from functions import remove_punctuation,whitespace_indexes,sentiments
from credentials import API_KEY

audio_path = ("./records/records.mp3")

def transcribe(q, audio_path=audio_path, API_KEY=API_KEY):
  client = OpenAI(api_key=API_KEY)
  audio_file = open(audio_path, "rb")
  transcript = client.audio.transcriptions.create(
    model="whisper-1",
    file=audio_file,
    language="tr"
  )

  text = remove_punctuation(transcript.text)

  index_of_whitespaces = whitespace_indexes(text)
  sentiment = sentiments(text, index_of_whitespaces)
  print(sentiment)

  #for sentiment in sentiment:
  q.put(sentiment)

