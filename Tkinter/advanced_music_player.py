from tkinter import *
from tkinter import filedialog
from pygame import *

root = Tk();
mixer.init();

def list_():
    global filename ;
    #filename = mixer.music.load('/home/atmegarobotics/Desktop/app_development/Tkinter/aud.mp3');
    filename = mixer.music.load(filedialog.askopenfilename(filetypes=[("files types","*.mp3")]))
def play():  
    mixer.music.play()
def pause():
    mixer.music.pause();
def stop():
    mixer.music.unpause();
root.geometry("1080x607");
root.title("MusicPlayer");

img = PhotoImage(file="/home/atmegarobotics/Desktop/app_development/Tkinter/bg(1).png");
play_icon = PhotoImage(file='/home/atmegarobotics/Desktop/app_development/Tkinter/play.png');
pause_icon = PhotoImage(file='/home/atmegarobotics/Desktop/app_development/Tkinter/pause.png');
resume_icon = PhotoImage(file="/home/atmegarobotics/Desktop/app_development/Tkinter/resume.png");
music_icon = PhotoImage(file='/home/atmegarobotics/Desktop/app_development/Tkinter/music_icon.png')
#top_icon = PhotoImage(file='/home/atmegarobotics/Desktop/app_development/Tkinter/play.png')
#root.iconphoto(False,top_icon)
bgl = Label(root,image=img); 
bgl.place(x=0,y=0,relwidth=1,relheight=1);
Button(root,image=play_icon,command = play , bd = 6).place(x=400,y=470,width=90,height=90);
Button(root,image=pause_icon,command = pause , bd = 6).place(x=500,y=470,width=90,height=90);
Button(root,image=resume_icon,command = stop , bd =6 ).place(x=600,y=470,width=90, height=90)
Button(root,image = music_icon,command= list_ ,bd=6).place(x=100,y=100,width=250,height=250)

root.mainloop();