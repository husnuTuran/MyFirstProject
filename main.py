import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Lütfen bir şeyler söyleyin...")
    audio = r.listen(source)

try:
    text = r.recognize_google(audio, language="tr")
    print("Ses tanındı: " + text)
except sr.UnknownValueError:
    print("Ses anlaşılamadı.")
except sr.RequestError as e:
    print("Ses tanıma servisi çalışmıyor: {0}".format(e))
