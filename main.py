from starter import start
from audio.microphone import Microphone
from speech.speech_detector import SpeechDetector
from transcription.whisper_transcriber import WhisperTranscriber


def main():
    microphone = Microphone()
    speech_detector = SpeechDetector()
    transcriber = WhisperTranscriber()

    start()
    microphone.start()

    while True:
        audio = microphone.read()
        speech = speech_detector.process(audio)
        if speech is not None:
            text = transcriber.transcribe(speech)
            print(text)

            normalized_text = text.strip().lower()
            if "stop" in normalized_text:
                print("Encerrando por comando de voz 'stop'.")
                break

    microphone.stop()


if __name__ == "__main__":
    main()