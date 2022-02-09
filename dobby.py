import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia as wiki
import webbrowser
import pyjokes
import pywhatkit

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice', voices[0].id)
engine.setProperty("rate", 220)


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
    speak("This is Dobby! How may I help you master?")


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
        if 'dobby' in query:
            query = query.replace('dobby', '')
        query = query.lower()
        print('Your message:', format(query))

    except Exception as e:
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
    if 'what is' in query:
        speak('Searching Wikipedia')
        query = query.replace('what is', '')
        print(query)
        results = wiki.summary(query, sentences=2)
        speak("According to wikipedia,")
        speak(results)

    # Open YouTube.
    if 'open youtube' in query:
        speak("Okay. YouTube opening now.")
        webbrowser.open('youtube.com')
        # break

    # Open StackOverflow.
    if 'open stack overflow' in query:
        speak("Okay. StackOverflow opening now.")
        webbrowser.open('stackoverflow.com')
        # break

    # Open Google.
    if 'open google' in query:
        speak("Okay. Google opening now.")
        webbrowser.open('google.com')

    # Random jokes
    if 'joke' in query:
        speak(pyjokes.get_joke())

    # Thank you response
    if 'thank you' in query:
        speak("Anytime!")

    # Play some music
    if 'play' in query:
        song = query.replace('play', '')
        speak('playing ' + song)
        pywhatkit.playonyt(song)

    if 'bye' in query:
        speak("See you later!")
        exit()

    # Bye Note.
    # if 'bye' or 'good bye' or 'goodbye' or 'tata' in query:
    #     speak('Call me if you need anything. Have a nice day.')
    #     speak('Bye!')
    #     # exit()

    # else:
    #     speak("I'm sorry, could you please repeat that?")

    return query


if __name__ == "__main__":
    greeting()

    while True:
        takeCommand()
