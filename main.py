import pyttsx3     #(Text to speach module)           
import speech_recognition as sr     #(to recognize the speach)      
import datetime
import wikipedia as wk
import webbrowser
import os
import smtplib
import pyaudio
# pip install pipwin 
# pipwin install pyaudio (for pyaudio)

print("Intializing Jarvis...")

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

ADMIN = "Ronak"

# speak function will speak the text which we will passes
def speak(text):
    engine.say(text)
    engine.runAndWait()

## wishMe function will Greet the ADMIN
def grettings_sir():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning.." + ADMIN)
    elif hour>=12 and hour<=16:
        speak("Good Afternoon..." + ADMIN)
    else:
        speak("Good Evening..." + ADMIN)
    
    speak("I am Jarvis , How may i help you?")



"""
### It is used to find the index of the microphone.. which is in our case is 0
p = pyaudio.PyAudio()
for i in range(p.get_device_count()):
    info = p.get_device_info_by_index(i)
    print(info['index'],info['name'])
"""

#  takeCommand function will take command from the ADMIN with the help of microfone

def takeCommand():
    r = sr.Recognizer()
    mic = sr.Microphone(device_index=0)
    with mic as source:
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recoginzing...")
        query = r.recognize_google(audio,language='en-in')
        print("You said :",query)

    except Exception as e:
        speak("Sorry i can't get you...")
        speak("can you repete that again?")
        #takeCommand()
        query = None
    return query

def sendEmail(to,context):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com','password')
    server.sendmail("hello mr. navadiya", to, context)
    server.close()




## function for executing tasks as per command
def applyCommand(task):
    task = task.lower()
    if 'open code' in task:
        codepath = r"C:\Users\ronak\AppData\Local\Programs\Microsoft VS Code\Code.exe"
        os.startfile(codepath)
    elif 'wikipedia' in task:
        speak('Searching wikipedia...')
        task = task.strip("wikipedia")
        task = task.strip("search")
        print(task)
        result = wk.summary(task, sentences = 2)
        print(result)
        speak(result)

    elif 'open' in task:
        task = task.strip("open")
        url = task + ".com"
        print(url)
        chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'play music' in task:
        songs_dir = "C:/Users/ronak/Music/Songs"
        songs = os.listdir(songs_dir)
        print(songs)
        """speak("Which song do like to here sir..")
        specific_song = takeCommand()
        print(specific_song)
        index = songs.index(specific_song)
        """
        print(index)
        index=0
        os.startfile(os.path.join(songs_dir,songs[index]))
    
    elif 'the time' in task:
        currenttime = datetime.datetime.now().strftime("%H:%M:%S")
        query = "sir the time is :" + currenttime
        speak(query)
    
    elif 'email to ronak navadiya' in task:
        try:
            speak("What should I send?")
            content = takeCommand()
            to = "ronaknavadiya30@gmail.com"
            sendEmail(to,content)
            speak("Email has been sent successfully")
        except Exception as e:
            print(e)

    elif 'close jarvis' in task or 'you can go' in task:
        speak("ohk bye bye..")
    


    
### Main Proggram Start ###

def main():
    speak("Setting up Jarvis..")
    grettings_sir()
    query = takeCommand()
    applyCommand(query)

main()

