import queue
import sounddevice as sd
from config import SAMPLE_RATE, BLOCK_DURATION


class Microphone:
    def __init__(self):
        self.queue = queue.Queue()

    def callback(self, indata, frames, time, status):
        self.queue.put(indata.copy())

    def start(self, samplerate: int = SAMPLE_RATE, block_duration: float = BLOCK_DURATION):
        blocksize = int(samplerate * block_duration)
        self.stream = sd.InputStream(
            samplerate=samplerate,
            channels=1,
            blocksize=blocksize,
            callback=self.callback,
        )
        self.stream.start()

    def read(self):
        return self.queue.get()

    def stop(self):
        if hasattr(self, "stream"):
            self.stream.stop()
            self.stream.close()