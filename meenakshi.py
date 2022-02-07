import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia as wiki
import webbrowser
import pyjokes
import pywhatkit

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)


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
    # It takes microphone i/p from user and gives a string o/p
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Clearing background noises...Please wait")
        r.adjust_for_ambient_noise(source, duration=0.5)
        print('Listening.')
        recordedaudio = r.listen(source)
    try:
        query = r.recognize_google(recordedaudio, language='en-in')
        if 'meenakshi' in query:
            query = query.replace('Meenakshi', '')
        query = query.lower()
        print('Your message:', format(query))

    except Exception as e:
        # speak("I'm sorry, could you please repeat that?")
        return "None"

    # Functionalities.
    # Wiki Searches.
    if 'wikipedia' in query:
        speak('Searching Wikipedia')
        query = query.replace('wikipedia', '')
        results = wiki.summary(query, sentences=2)
        speak("According to wikipedia,")
        speak(results)

    # Definitions.
    elif 'what is' in query:
        speak('Searching Wikipedia')
        query = query.replace('what is', '')
        print(query)
        results = wiki.summary(query, sentences=2)
        speak("According to wikipedia,")
        speak(results)

    # Open YouTube.
    elif 'open youtube' in query:
        speak("Okay. YouTube opening now.")
        webbrowser.open('youtube.com')
        # break

    # Open StackOverflow.
    elif 'open stack overflow' in query:
        speak("Okay. StackOverflow opening now.")
        webbrowser.open('stackoverflow.com')
        # break

    # Open Google.
    elif 'open google' in query:
        speak("Okay. Google opening now.")
        webbrowser.open('google.com')

    # Random jokes
    elif 'joke' in query:
        speak(pyjokes.get_joke())

    # Thank you response
    elif 'thank you' in query:
        speak("Anytime!")

    # Play some music
    if 'play' in query:
        song = query.replace('play', '')
        speak('playing ' + song)
        pywhatkit.playonyt(song)

    # Bye Note.
    elif 'bye' or 'good bye' or 'goodbye' or 'tata' in query:
        speak('Call me if you need anything. Have a nice day.')
        speak('Bye!')
        # exit()

    else:
        speak("I'm sorry, could you please repeat that?")

    return query


if __name__ == "__main__":
    greeting()
    while True:
        takeCommand()
