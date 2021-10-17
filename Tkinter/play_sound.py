from playsound import playsound
from tkinter import *
root = Tk();
root.geometry("250x250");
root.title("musicplayer")
def playsong():
    playsound("/home/atmegarobotics/Desktop/app_development/Tkinter/aud.mp3");
Button(root,text="play",width=100,height=1,command=playsong );
root.mainloop()