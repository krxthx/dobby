import pyttsx3
import speech_recognition as sr
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)
# voice female


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def greeting():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning!")
    elif hour >= 12 and hour < 17:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("This is Meenaakshi. How may I help you?")


def takeCommand():
    # It takes microphone input from user and gives a string o/p
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening.')
        r.pause_threshold = 1
        audio = r.listen(source)


if __name__ == "__main__":
    greeting()
