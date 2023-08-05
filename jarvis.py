from email.policy import strict
import pyttsx3
import speech_recognition as sr  
import datetime
import wikipedia  
import webbrowser
import random
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning sir!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon sir!")

    elif hour >= 18 and hour < 20:
        speak("Good Evening sir!")

    else:
        speak("Good Night sir!")

    speak("I am alex. your personal assistant. Rahul Sir. Please tell me how may I help you....")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        #print("e")
        print("Say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('rahul30dh@gmail.com','rahul30dh1998')
    server.sendmail('rahul30dh@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    takeCommand()
    while True:
        #if 1:
        query = takeCommand().lower()
         #Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=10)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open whatsapp' in query:
            webbrowser.open("https://web.whatsapp.com/")

        elif 'open instagram' in query:
            webbrowser.open("https://www.instagram.com/accounts/login/")  
        
        elif 'play apna' in query:
            webbrowser.open("https://youtu.be/AX4GjsLdrNI")  

        elif 'play ipl' in query:
            webbrowser.open("https://www.jiocinema.com/")

        elif 'open my class attendance' in query:
            webbrowser.open("http://ipeclive.ipec.org.in/")

        elif 'play music' in query:
            #n = random.randint(0,10)
            music_dir = 'D:\music' #D:\\Non Critical\\songs\\Favorite Songs2
            songs = os.listdir(music_dir)
            print(songs)
            #print(n)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'what the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
   
        elif 'the date' in query:
            strDate = datetime.datetime.now().strftime("%DD:%MM:%YY")
            speak(f"Sir, the date is {strDate}")                                           

        elif 'open code' in query:
            codePath = ("C:\\Users\\dhima\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
            os.startfile(codePath)
        elif 'are you ok alex' in query:
            speak("yes sir i am fine ")
        
        elif 'email to satyam' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = ("satyampanday1305@gmail.com")
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir . I am not able to send this email")
