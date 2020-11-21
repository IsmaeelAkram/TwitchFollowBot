import speech_recognition as sr
import wget

def recognize_audio(audio_file_url: str):
    r = sr.Recognizer()
    audio_file = wget.download(audio_file_url)
    captcha = sr.AudioFile(audio_file)
    with captcha as source:
        audio = r.record(source)
    code = r.recognize_google(audio)
    print(code)