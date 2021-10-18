from tkinter import *
root = Tk();
img = PhotoImage(file='/home/atmegarobotics/Desktop/app_development/Tkinter/bg.png')
bgl = Label(root,image=img);
bgl.place(x=0,y=0,relwidth=1,relheight=1);
root.geometry("1080x607");
root.title("bg");
root.mainloop();