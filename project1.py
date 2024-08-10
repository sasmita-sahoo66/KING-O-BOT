import pyttsx3                      #text to speech conversion
import speech_recognition as sr
import webbrowser
import pywhatkit
import os
import datetime
import cv2
import random
import pyautogui
import keyboard
import pyqrcode 
from pyqrcode import QRCode
 #text to speech

Assistant = pyttsx3.init()
voices = Assistant.getProperty('voices')          #get property of voices from the Assistent varible in which we initialise the pyttsx3
Assistant.setProperty('voices',voices[0].id)
Assistant.setProperty("rate", 180)
#print(voices[1].id)

#creat function to speak
def speak(audio):
    Assistant.say(audio)
    print("  ")
    print(audio)
    print("  ")
    Assistant.runAndWait()
# create a fun to take command from user
def takecommand():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening you sir...........")
        command.pause_threshold = 1
        audio = command.listen(source)
        try:
            print('Recognizing.........')
            query = command.recognize_google(audio,language='en-in')
            print(f'you said:{query}')
        except Exception as Error:
            return "None"
        return query.lower()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning sir!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon sir!")
    else:
        speak("Good Evening sir!")
    speak("I am king o ! Please tell me how may I help you?")
def password_generator(passlen):
    passlen = int(input("enter the length of password"))
    s="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
    p = "".join(random.sample(s,passlen ))
    print(p)

def generate_qr_code(s):
    s = input("Enter the Link Here: ")
    url = pyqrcode.create(s)
    url.svg("myyoutube.svg", scale = 8)
def rock_papper():
    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)
    player = False
    cpu_score = 0
    player_score = 0
    while True:
        player = takecommand().lower()
        ## Conditions of Rock,Paper and Scissors
        if player =="computer":
            print("Tie!")
        elif player == "rock":
            if computer == "paper":
                print("You lose!", computer, "covers", player)
                speak("You lose paper covers rock")
                cpu_score+=1
            else:
                print("You win!", player, "smashes", computer)
                speak("You win rock smashes paper")
                player_score+=1
        elif player == "paper":
            if computer == "scissors":
                print("You lose!", computer, "cut", player)
                speak("You lose scissors cut paper")
                cpu_score+=1
            else:
                print("You win!", player, "covers", computer)
                speak("You win paper covers scissors")
                player_score+=1
        elif player == "scissors":
            if computer == "rock":
                print("You lose...", computer, "smashes", player)
                speak("You lose rock smashes scissors")
                
                cpu_score+=1
            else:
                print("You win scissors cut rock")
                player_score+=1
        elif player=='End':
            print("Final Scores:")
            print(f"CPU:{cpu_score}")
            print(f"Player:{player_score}")
            break

def taskexecution():
    wishMe()
    while True:
        query = takecommand().lower()
        if "hello" in query:
            speak("hello sir,I am kingo,")
            speak("Your personal AI assistant!")
            speak("How may i help you")
        elif "how are you" in query:
            speak("I am fine sir !")
            speak("what about you")
        elif "fine " in query:
            speak("oh! good to hear it sir")
        elif "not fine" in query:
            speak("what happen sir is every thing alright")
        elif "everything alright" in query:
            speak("oh! thank god sir if you have any problem please tell me sir")
        elif "take a break " in query:
            speak(" ok sir. you can call me any time !")
            break
        elif "ok bye kingo" in query:
            speak("ok sir ,bye!")
            break
        elif "youtube search" in query:
            speak("Ok sir ,This what i found for your search")
            query = query.replace("youtube search","")
            web = "https://www.youtube.com/results?search_query="+query
            webbrowser.open(web)
            speak('done sir!')
        elif "google search" in query:
            speak("THIS IS WHAT I FOUND FOR YOU SIR")
            query = query.replace("google search","")
            pywhatkit.search(query)
            speak("Done sir!")
        elif "launch website" in query:
            speak("PLEASE TELL ME THE NAME OF WEBSITE SIR!!")
            name = takecommand()
            web = "https://www." + name + ".com"
            webbrowser.open(web)
            speak(" Done sir!!")
        elif "wikipedia" in query:
            speak('searching wikipedia...')
            query=query.replace("wikipedia","")
            wiki = wikipedia.summary(query,2)
            speak(f"According to wikipedia :{wiki}")
        elif "open notepad" in query:
            path = "C:\\windows\\system32\\notepad.exe"
            os.startfile(path)
        elif "open command prompt" in query:
            os.system("start cmd")
        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k == 27:
                    break
            cap.release()
            cv2.destroyAllWindows()
        elif "play music" in query:
            musicdir =Music
            songs = os.listdir(musicdir)
            rd = random.choice(songs)
            os.startfile(os.path.join(musicdir, rd))
        elif "play song on youtube" in query:
            speak("which song do you want to play")
            musnam=takecommand()
            pywhatkit.playonyt(musnam)
            speak("your song has been started , enjoy sir!!")
        elif "take screenshot" in query or "take a screenshot" in query:
            speak("okk boss, what should i name that file")
            name = takecommand().lower()
            speak("please sir hold the  screen for few seconds,i am taking screenshot ")
            ss = pyautogui.screenshot()
            ss.save(f"{name}.png")
            speak("i am done sir ,the screenshot is saved in main folder ,now i am ready for next command")
        elif "code " in query:
            os.startfile("C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code")
        elif "whatsapp" in query:
            os.startfile("C:\\Users\\hp\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
        elif "facebook" in query:
            webbrowser.open("https://www.facebook.com/")
        elif "instagram" in query:
            webbrowser.open("https://www.instagram.com/")
        elif "maps" in query:
            webbrowser.open("https://www.google.co.in/maps/place/Webskitters+Technology+Solutions+Pvt.+Ltd./@22.5751527,88.4253259,17z/data=!3m1!4b1!4m5!3m4!1s0x3a0275927b0061ad:0x496c2fab98874c86!8m2!3d22.5751527!4d88.4275146")

        elif "pause" in query:
            keyboard.press("space bar")
        elif "restart" in query:
            keyboard.press("0")
        elif "mute" in query:
            keyboard.press("m")
        elif "skip" in query:
            keyboard.press("l")
        elif "back" in query:
            keyboard.press("j")
        elif "full sreen" in query:
            keyboard.press("f")
        elif "film mode" in query:
            keyboard.press("t")
        elif "generate password" in query:
            speak("Sir, Tell me the length of the password you want")
            passlen1 = takecommand().lower()
            passlen = int(passlen1)
            password_generator(passlen)
            speak("Here is your encrypted password sir")
        elif "generate qr code" in query:
            speak("Sir Please give me the link")
            s = "https://www.webskitters.com/"
            generate_qr_code(s)
        elif "play game" in query:
            speak("Enter your choices and have fun sir")
            rock_papper()
            
            

if __name__ == '__main__':
    taskexecution()

