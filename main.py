import threading
import queue
import keras
from OpenAI_SpeechToText import transcribe
from GettingAudio import record_audio
from functions import search_keyword
from shared_state import SharedState
from nn import tokenizer, load_model, predict


q = queue.Queue()
state = SharedState()
model = load_model()
tokenizer = tokenizer()

# Thread'leri oluştur
while True:
    q.empty()
    recorder_thread = threading.Thread(target=record_audio, args=(state,))
    transcriber_thread = threading.Thread(target=transcribe, args=(q,))
    searcher_thread = threading.Thread(target=search_keyword, args=(q, state, "Altyazı",))
    command_thread = threading.Thread(target=predict, args=(q, model, tokenizer))

    recorder_thread.start()
    transcriber_thread.start()
    recorder_thread.join()
    transcriber_thread.join()
    if state.get():
        recorder_thread.start()
        command_thread.start()
        state.set(False)
    else:
        searcher_thread.start()
        searcher_thread.join()


