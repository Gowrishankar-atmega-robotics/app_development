from tkinter import *
from tkinter import filedialog
from pygame import *
root = Tk();
mixer.init();

def play():
    global filename ;
    #filename = mixer.music.load('/home/atmegarobotics/Desktop/app_development/Tkinter/aud.mp3');
    filename = mixer.music.load(filedialog.askopenfilename(filetypes=[("files types","*.mp3")]))
    mixer.music.play()
def stop():
    mixer.music.stop();
def pause():
    mixer.music.pause();
root.geometry("1080x607");
root.title("MusicPlayer");

img = PhotoImage(file="/home/atmegarobotics/Desktop/app_development/Tkinter/bg.png");
start_icon = PhotoImage(file='/home/atmegarobotics/Desktop/app_development/Tkinter/start.png');
pause_icon = PhotoImage(file='/home/atmegarobotics/Desktop/app_development/Tkinter/pause.png');
stop_icon = PhotoImage(file="");
bgl = Label(root,image=img);
bgl.place(x=0,y=0,relwidth=1,relheight=1);
Button(root,image=start_icon,command = play , bd = 6).place(x=400,y=470,width=64,height=64);
Button(root,image=pause_icon,command = stop , bd = 6).place(x=500,y=470,width=64,height=64);
Button(root,text="stop",bd =6 ).place(x=600,y=470,width=64, height=64)
root.mainloop();