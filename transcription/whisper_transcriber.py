import numpy as np
from faster_whisper import WhisperModel

from config import COMPUTE_TYPE, MODEL_SIZE

class WhisperTranscriber:
    def __init__(self):
        self.model = WhisperModel(
            MODEL_SIZE,
            compute_type=COMPUTE_TYPE,
        )

    def transcribe(self, audio):

        audio = audio.flatten().astype(np.float32)

        segments, _ = self.model.transcribe(audio)

        text = []

        for segment in segments:
            text.append(segment.text)

        return " ".join(text)