from tkinter import *
from tkinter import filedialog
from pygame import *
root = Tk();
root.geometry("1080x607");
root.title("MusicPlayer");
img = PhotoImage(file="/home/atmegarobotics/Desktop/app_development/Tkinter/bg.png");
start_icon = PhotoImage(file='/home/atmegarobotics/Desktop/app_development/Tkinter/start.png');
pause_icon = PhotoImage(file='/home/atmegarobotics/Desktop/app_development/Tkinter/pause.png');
bgl = Label(root,image=img);
bgl.place(x=0,y=0,relwidth=1,relheight=1);
Button(root,image=start_icon,bd = 6).place(x=550,y=470,width=64,height=64);
Button(root,image=pause_icon,bd = 6).place(x=482,y=470,width=64,height=64);
root.mainloop();