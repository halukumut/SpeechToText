import threading
import queue
import time
from OpenAI_SpeechToText import transcribe
from GettingAudio import record_audio
from functions import search_keyword

# Kuyruk oluştur
q = queue.Queue()

# Thread'leri oluştur
while True:
    q.empty()
    recorder_thread = threading.Thread(target=record_audio, args=(5,))
    transcriber_thread = threading.Thread(target=transcribe, args=(q,))
    searcher_thread = threading.Thread(target=search_keyword, args=(q, "İbrahim",))

    recorder_thread.start()
    transcriber_thread.start()
    searcher_thread.start()

    recorder_thread.join()
    transcriber_thread.join()
    searcher_thread.join()
