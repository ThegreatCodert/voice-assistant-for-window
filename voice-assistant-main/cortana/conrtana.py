from gtts import gTTS
import playsound
import speech_recognition as sr
import wikipedia
import os
from datetime import datetime
import time
import webbrowser
import pyjokes


def speak(x):
    tts = gTTS(text=x, lang="en")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception:
            speak("sorry I dont know that")
            print("Sorry I dont know that one")
    return said


query = get_audio()
try:
    if "time" in query:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        speak(current_time)
        print("Current Time =", current_time)
        speak("Done")

    if "open Chrome" in query:
        codePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        os.startfile(codePath)
        speak("Done")

    if "class" in query:
        codePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        os.startfile(codePath)
        codePath2 = "C:\\Program Files (x86)\\Zoom\\bin\\Zoom.exe"
        os.startfile(codePath2)
        codePath3 = "C:\\Users\\aaran\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
        os.startfile(codePath3)
        speak("Done")

    if "code" in query:
        codePath4 = "C:\\Users\\aaran\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath4)
        speak("Done")
    if "Wiki" in query:
        # speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)

    if "go" in query:
        now = datetime.now()
        current_time = now.strftime("%d - %H - %M - %S")
        speak("GO: ")
        text = get_audio()
        file = open("C:\\Users\\aaran\\OneDrive\\Desktop\\" +
                    current_time + ".txt", "w")
        file.write(text)
        file.close()
        speak("Done")

    if "spotify" in query:
        webbrowser.open('https://open.spotify.com/')
        speak("Done")

    if "hello" in query:
        speak("Good morning")

    if "who are you" in query:
        speak("I am Friday your virtual assistant")

    if "joke" in query:
        joke = pyjokes.get_joke(language='en', category='neutral')
        speak(joke)
        print(joke)
        speak("hahahahah")

    def reminder():
        print("What shall I remind you about?")
        text = str(input())
        print("In how many minutes?")
        local_time = float(input())
        local_time = local_time * 60
        time.sleep(local_time)
        speak(text)
        playsound.playsound("c.mp3")
    if "remind" in query:
        reminder()

    if "alarm" in query:
        try:
            Your_time = input("Write: ")
            now = datetime.now()
            current_time = now.strftime("%H")
            y = int(Your_time)
            x = int(current_time)
            local_time = (x - y) * 60
            time.sleep(local_time)
            playsound.playsound("c.mp3")
        except ValueError:
            local_time = (y - x)*60
            time.sleep(local_time)
            playsound.playsound("c.mp3")
except PermissionError:
    pass
