import time
import numpy as np

from config import SILENCE_DURATION, SILENCE_THRESHOLD

class SpeechDetector:
    def __init__(self):
        self.buffer = []
        self.speaking = False
        self.silence_start = None

    def remove_silence(self, audio):
        return np.sqrt(np.mean(audio**2))

    def process(self, chunk): 
        volume = self.remove_silence(chunk)

        if volume > SILENCE_THRESHOLD:
            if not self.speaking:
                print("Speech detected...")

            self.speaking = True
            self.buffer.append(chunk)
            self.silence_start = None
            return None

        if self.speaking:
            self.buffer.append(chunk)

            if self.silence_start is None:
                self.silence_start = time.time()

            if time.time() - self.silence_start > SILENCE_DURATION:
                audio = np.concatenate(self.buffer)

                self.buffer = []
                self.speaking = False
                self.silence_start = None

                return audio

        return None