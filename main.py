import threading
import queue
from OpenAI_SpeechToText import transcribe
from GettingAudio import record_audio
from functions import search_keyword


class SharedState:
    def __init__(self):
        self.state = False
        self.lock = threading.Lock()

    def set(self, value):
        with self.lock:
            self.state = value

    def get(self):
        with self.lock:
            return self.state


# Kuyruk oluştur
q = queue.Queue()
state = SharedState()

# Thread'leri oluştur
while True:
    q.empty()
    recorder_thread = threading.Thread(target=record_audio, args=(state,))
    transcriber_thread = threading.Thread(target=transcribe, args=(q,))
    searcher_thread = threading.Thread(target=search_keyword, args=(q, state, "Altyazı",))

    recorder_thread.start()
    transcriber_thread.start()
    recorder_thread.join()
    transcriber_thread.join()
    if state.get():
        print(3)
        state.set(False)
    else:
        searcher_thread.start()
        searcher_thread.join()


