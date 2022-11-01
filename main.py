import tkinter
from tkinter import ttk,messagebox
import speech_recognition as sr
import googletrans
from deep_translator import GoogleTranslator
import pyttsx3 as pt
speaker=pt.init()
recognizer=sr.Recognizer()
with sr.Microphone() as mic:
    x = True
    while x is True:
        try:
            recognizer.adjust_for_ambient_noise(mic,0.1)
            print("listening")
            speaker.say("What is your name?")
            name= recognizer.listen(mic)
            name = recognizer.recognize_google(name)
            speaker.say(f"I am listening to you {name}")
            audio=recognizer.listen(mic)
            text=recognizer.recognize_google(audio)
            speaker.say(str(text))
            speaker.runAndWait()
            print(text)
            if text.upper() == "STOP":
                x = False
        except:
            print(" come again")
