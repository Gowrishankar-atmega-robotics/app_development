from tkinter import *
#import playsound as playsound
root = Tk();
root.title("musicplayer");
root.geometry("500x500");
listbox = Listbox(root,width=10,height=10,bg="#6b6b6b");
listbox.insert(1,"python");
listbox.insert(2,"c++");
listbox.insert(3,"panda");
listbox.insert(4,"conda");
listbox.insert(5,"c");
listbox.pack();
#def play():
#    playsound('/home/atmegarobotics/Desktop/app_development/Tkinter/aud.mp3');
#Button(root,text="play").pack();
root.mainloop();