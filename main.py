import subprocess

from starter import start
from audio.microphone import Microphone
from speech.speech_detector import SpeechDetector
from transcription.whisper_transcriber import WhisperTranscriber
from assistant import ChatAssistant
from dotenv import load_dotenv


def main():
    load_dotenv()

    microphone = Microphone()
    speech_detector = SpeechDetector()
    transcriber = WhisperTranscriber()
    assistant = ChatAssistant()

    start()
    microphone.start()

    while True:
        audio = microphone.read()
        speech = speech_detector.process(audio)
        if speech is not None:
            text = transcriber.transcribe(speech)
            print(text)

            normalized_text = text.strip().lower()
            if "stop the program" in normalized_text:
                print("Encerrando por comando de voz 'stop'.")
                break

            
            # Enviar o texto completo para o assistente
            answer = assistant.respond(text)
            print(f"Josué: {answer}")

            # Evitar que o áudio do 'say' volte para o microfone
            microphone.stop()
            microphone.clear_queue()
            subprocess.run(["say", answer])
            microphone.start()

    microphone.stop()


if __name__ == "__main__":
    main()