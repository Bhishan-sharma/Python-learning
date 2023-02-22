from sys import executable
import os
import datetime
import webbrowser
from tkinter import *
import pywhatkit
import wikipedia

#JARVIS GREETING THE USER - method wishme runs only for once
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour < 12:
        print("Good Morning sir")
    elif hour >= 12 and hour < 18:
       print("Good Afternoon sir")
    else:
        print("Good evening sir")

#GIVING COMMAND TO JARVIS - by creating a method - take_command
def take_command():
    r = input()
    print("recognizing..")

#Try statement is used here to not to stop our program our jarvis can't do it 
    try:
        querry = r
        print(f"User said: {querry}\n")

    except Exception as e:
        print("type that again please...")
        return "None"
    return querry

#if __name__ == "__main__" is a block used to allow or prevent parts of codes from being run when the modules are imported 
if __name__ == "__main__":
    wishme()

#making the program to run infine times
    while True:
       querry = take_command()

#OPPENING ONLINE WEBSITES - by giving path of websites and using webbrowser module
       if "youtube" in querry:
           webbrowser.open("https://www.youtube.com")
        
       elif "google" in querry:
           webbrowser.open("https://www.google.com")

       elif "stackoverflow" in querry:
           webbrowser.open("https://stackoverflow.com")

       elif "shutdown" in querry:
           os.system("shutdown /s /t 1")
       
       elif "time" in querry:
           strTime = datetime.datetime.now().strftime("%H:%M:%S")
           print(f"the time is {strTime}")
       
       elif "hello" in querry:
           wishme()
           print("Hello sir how are")

       elif "i am fine" in querry:
           print("Gud bless you! I wish you for your bright future")
           print("Now tell me sir how can I help you..")

#openning an app on window by using path and start it by startfile funtion of os module 
       elif "open code" in querry:
           path="C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
           os.startfile(path)
      
#OPENNING SELF CREATED WEBSITES
       elif "ace" in querry:
           path = "C:\\Users\\hp\\Desktop\\websites\\ace_cwh\\index.html"
           os.startfile(path)

       elif "play" in querry:
           video = querry.replace("play", "")
           pywhatkit.playonyt(video)

       elif "who is" in querry:
           person = querry.replace("who is", "")
           info = wikipedia.summary(person ,1)
           print(info)

#OPPENING NOTEPAD
       elif "open notepad" in querry:
        path = "C:\\Windows\\system32\\notepad.exe"
        os.startfile(path)

#jarvis introducing itself
       elif "who are you" in querry:
           print('''I am an AI created by Great Bhishan Sir 
           my name is jarvis''')

       elif "help" in querry:
           print('''I can do some functions like:-,openning vs code,openning notepad,openning Youtube,openning google,creating folder,creating file''')

       elif "create folder" in querry:
           print("enter the name for the folder")
           file_name = input()
           os.mkdir(file_name)
           os.chdir(f"C:\\Users\\hp\\Desktop\\{file_name}")

       elif "remove file" in querry:
           print("enter the name of the file")
           file_name = input()
           os.rmdir(f"C:\\Users\\hp\\Desktop\\{file_name}")
           print("file deleted")

       elif "remove folder" in querry:
           print("enter the name of the folder")
           folder_name = input()
           os.removedirs(f"C:\\Users\\hp\\Desktop\\{folder_name}")
           print("file deleted")

#f is a formatted string literal it is prefixed with 'f' these strings contain replacement fields {}
       elif "create file" in querry:
           print("Enter the name of the folder in which you want to create it")
           folder_name = input()
           os.chdir(f"C:\\Users\\hp\\Desktop\\{folder_name}")
           print("enter the type of file you want")
           file_state = input()
           print("enter the content")
           content = input()
           with open(file_state, "w") as f:
               f.write(content)

       elif "quit" in querry:
           executable(exit())

       else:
           print("Sorry sir! please type the command again")