import speech_recognition as sr
from datetime import datetime
import webbrowser
import time
from gtts import gTTS
from playsound import playsound
import random
import os

r = sr.Recognizer()

def record(ask = False):
    
    with sr.Microphone() as source:
        if ask == True:
            speak(ask)
        audio = r.listen(source)
        voice = ''
        try:
            voice = r.recognize_google(audio,language = 'en-EN')
        except sr.UnknownValueError:
            speak("i could not understand")
        except sr.RequestError:
            speak("system does not work")
        return voice    

def response(voice):
    if 'how are you' in voice:
        speak("i am fine, you?")
    if 'what time is it' in voice:
        speak(datetime.now().strftime('%H:%M:%S'))
    if 'search something' in voice:
        speak('what do you want to search')
        search = record()
        url = 'https://google.com/search?q='+search
        webbrowser.get().open(url)
        speak(search + ' i found for the search' )
    if 'open' in voice:
        search = record()
        if search == 'youtube':
            url = 'https://youtube.com'
            webbrowser.get().open(url)
            speak('youtube are opening')
            
        
        
    
         
        
        
    if 'yes' in voice:
        speak('goodbye')
        exit()
        
        
def speak(string):
    gTTS(string,lang = 'en')
    rand = random.randint(1,10000)
    file = 'audio-'+str(rand)+'.mp3'
    tts.save(file)
    playsound(file)
    os.remove(file)
   
speak("how can i help you")
time.sleep(1)
while 1:
    voice = record()
    print(voice)
    response(voice)




