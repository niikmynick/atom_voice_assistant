import pvporcupine
from pvrecorder import PvRecorder
import vosk
import pyttsx3

import time
import struct
import json

from config import *


def listen_to_wake_word(voice_model: pvporcupine.Porcupine, mic: PvRecorder):
    try:
        mic.start()

        while True:
            keyword_index = voice_model.process(mic.read())
            if keyword_index >= 0:
                print("Распознано:  Привет Атом")

                mic.stop()
                return True

    except KeyboardInterrupt:
        mic.stop()


def listen_to_command(voice_model: vosk.KaldiRecognizer, mic: PvRecorder, start_time: float):
    try:
        mic.start()

        while time.time() - start_time <= 5:
            pcm = mic.read()
            sp = struct.pack("h" * len(pcm), *pcm)

            if voice_model.AcceptWaveform(sp):
                mic.stop()
                print(json.loads(voice_model.Result()))
                answer()
                start_time = time.time()
                mic.start()

        mic.stop()

    except KeyboardInterrupt:
        mic.stop()


def answer():
    # text-to-speech engine
    engine = pyttsx3.init()

    # speed and volume of the voice
    engine.setProperty('rate', 150)  # 150 words per minute
    engine.setProperty('volume', 0.8)  # 80% volume

    text = 'Я вас услышал'

    engine.say(text)
    engine.runAndWait()


if __name__ == '__main__':

    # wake word recogniser
    porcupine = pvporcupine.create(
        access_key=picovoice_access_key,
        model_path=picovoice_model_path,
        keyword_paths=[picovoice_keyword_path]
    )

    # commands recogniser
    vosk_model = vosk.Model(vosk_model_path)
    samplerate = 16000
    recogniser = vosk.KaldiRecognizer(vosk_model, samplerate)

    # mic listener
    recorder = PvRecorder(
        device_index=-1,
        frame_length=porcupine.frame_length
    )

    print(f'Используется устройство: {recorder.selected_device}')
    print(f"Атом запущен ...")
    time_mark = time.time()
    stopped = False

    while not stopped:
        listen_to_wake_word(porcupine, recorder)

        time_mark = time.time()

        listen_to_command(recogniser, recorder, time_mark)

    porcupine.delete()
    recorder.delete()
