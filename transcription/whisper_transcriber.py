import io
import wave

import numpy as np
from openai import OpenAI

from config import SAMPLE_RATE


class WhisperTranscriber:
    def __init__(self):
        self.client = OpenAI()

    def _to_wav_bytes(self, audio: np.ndarray) -> io.BytesIO:
        audio = audio.flatten().astype(np.float32)
        audio = np.clip(audio, -1.0, 1.0)
        audio_int16 = np.int16(audio * 32767)

        buffer = io.BytesIO()
        with wave.open(buffer, "wb") as wf:
            wf.setnchannels(1)
            wf.setsampwidth(2)
            wf.setframerate(SAMPLE_RATE)
            wf.writeframes(audio_int16.tobytes())

        buffer.seek(0)
        # A API da OpenAI usa a extensão do arquivo para detectar o formato,
        # então damos um nome com extensão .wav ao buffer em memória.
        buffer.name = "audio.wav"
        return buffer

    def transcribe(self, audio: np.ndarray) -> str:
        wav_file = self._to_wav_bytes(audio)

        response = self.client.audio.transcriptions.create(
            model="gpt-4o-mini-transcribe",
            file=wav_file,
            language="pt",
        )

        return response.text