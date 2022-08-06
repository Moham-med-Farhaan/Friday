import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=8 and hour<=12:
        speak("Good Morning . Welcome! Good to have you Back sir  ")
    elif hour>12 and hour<=18:
        speak("Good Afternoon . Welcome! Good to have you Back sir  ")
    elif hour==10:
        speak("Time for bed sir . Good Night!")
    else:
        speak("Good Evening . Welcome! good to have you back sir ")
    speak("Please tell me How can i be useful to you...")
def take_commands():
    r = sr.Recognizer()
    with sr.Microphone()  as  source:
        speak("listening sir")
        print("listening")
        r.pause_threshold = 1
        r.energy_threshold = 200
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio,language='en-US')
        print(f"user said:{query}\n")
    except:
        speak("Come again please... I didnt get you")
        return"none"
    return query
def opencommands(query):
    if 'open youtube' in query:
        speak("opening sir")
        webbrowser.open("youtube.com")
    elif 'open google' in query:
        speak("opening sir")
        webbrowser.open("google.com")
    elif 'open stack overflow' in query:
        speak("opening sir")
        webbrowser.open("stackoverflow.com")

    
if __name__=="__main__":
    wishme()
    a=True
    while a==True:
        query= take_commands().lower()
        if 'wikipedia' in query:
            speak("searching wikipedia...")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            speak(results)
        elif 'who are you' in query:
            speak("Iam Friday , your personal assistant")
        elif 'stop' in query:
            speak("as your wish sir")
            a=False
        elif 'how' in query:
            speak("Browsing . this will take a moment")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            speak(results)
        elif 'about yourself' in query:
            speak("Iam Personal Assistant of Mr.Farhaan . I was built by him . Who are you by the way ? where is my boss? ")
        elif 'open' in query:
            opencommands(query)
            a=False
        elif 'hello' and 'hi' in query:
            speak("Hello ! How are you ? . I hope your doing well")
            a=False
            
            
            
        