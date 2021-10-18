from tkinter import *
root = Tk();
filename = PhotoImage(file='/home/atmegarobotics/Desktop/app_development/Tkinter/167.png')
bgl = Label(root,image=filename);
bgl.place(x=0,y=0,relwidth=1,relheight=1);
root.geometry("1366x768");
root.title("bg");
root.mainloop();