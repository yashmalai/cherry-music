import vosk
import sys
import sounddevice as sd
import queue
import json


model = vosk.Model(
    model_path="model/vosk-model-small-ru-0.22"
)


q = queue.Queue()

def callback(indata, frames, time, status):
    if status:
        print(status)
    q.put(bytes(indata))

def listen():
    with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                           channels=1, callback=callback):
        rec = vosk.KaldiRecognizer(model, 16000)
        print("Слушаю...")
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                text = result.get("text", "").strip()
                if text:
                    return text
            else:
                # partial = json.loads(rec.PartialResult())
                pass