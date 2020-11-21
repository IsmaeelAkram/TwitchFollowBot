import speech_recognition as sr
import wget
import log

def recognize_audio(audio_file_url: str):
    r = sr.Recognizer()
    # audio_file = wget.download(audio_file_url)
    # captcha = sr.AudioFile(audio_file)
    captcha = sr.AudioFile(audio_file_url)
    with captcha as source:
        audio = r.record(source)
    code = r.recognize_google(audio)
    log.good(f'Captcha code: {code}')
    return code