import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import pyautogui
import time
import pyfirmata

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Masood !")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Masood ! ")
    else:
        speak("Good Evening Masood !")

    speak("Hello Masood i am Masood junior your assisstant how may i help you " )

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 0.8
        r.energy_threshold = 500
        audio = r.listen(source)

    try:
        ("recognizing...")
        query = r.recognize_google(audio , language= 'en-pk')
        print(f"user said : {query}\n")

    
    except Exception as e :
        print("Say that again please...")
        return "none"
    return query

if __name__ == "__main__":
    wishMe()

    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query :
            speak('searching Wikipedia...')
            query = query.replace("wikipedia" , "")
            results = wikipedia.summary(query , sentences=2)
            speak("according to wikipedia")
            speak(results)

        elif 'open youtube' in query:
            speak('ok sir')
            webbrowser.open('https://www.youtube.com/')

        elif "what's my name" in query:
            speak('Sir your name is masood')

        elif 'open google' in query:
            speak('ok sir')
            webbrowser.open('google.com')

        elif 'play nasheed' in query:
            speak('ok sir')
            webbrowser.open('https://www.youtube.com/watch?v=6t1k2W_sxtU')
        
        
        elif 'close ' in query:
            speak('ok sir')
            pyautogui.hotkey('ctrl','w')
        
        elif 'stop' in query:
            speak('ok sir')
            pyautogui.hotkey('space')
            
        elif 'continue' in query:
            speak('ok sir')
            pyautogui.hotkey('space')

        elif 'break' in query:
            speak('what is your name')
            result = takeCommand().lower()
            if 'masood' in result:
                speak('ok sir as you wish')
                exit()
            else:
                speak('i only hear to my boss')
        elif 'close tab ' in query:
            speak ('ok sir')
            pyautogui.hotkey('ctrl','w')
        elif 'hey junior' in query:
            speak('hmm sir how may i help you')
        elif 'open facebook' in query:
            speak('ok sir as you wish')
            webbrowser.open('https://www.facebook.com/')
        elif 'thank you' in query:
            speak('i am glad to work for you')
        elif 'mute' in query:
            speak('ok sir')
            pyautogui.hotkey('m')
        elif 'unmute' in query:
            speak('ok sir')
            pyautogui.hotkey('m')
        elif ' tab forward' in query:
            speak ('ok sir')
            pyautogui.hotkey('ctrl','tab')
        elif 'tab backward' in query:
            speak('ok sir')
            pyautogui.hotkey('ctrl','shift','tab')
        elif 'go to facebook tab' in query:
            speak('ok sir')
            webbrowser.open_new_tab('https://www.facebook.com/')
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f"sir the time is{strTime}")