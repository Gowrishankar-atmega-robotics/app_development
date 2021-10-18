from tkinter import *
root = Tk();
root.geometry("500x500");
root.title("MusicPlayer");
#Button(root,text="play",width=10,height=5).pack(side="bottom",padx=(100,0), pady=(0,10));
#Button(root,text="pause",width=10,height=5).pack(side="left",padx=(0,0),pady=(300,0))
Button(root,text="play").place(x=250,y=400,width=100,height=50);
Button(root,text='pause').place(x=150,y=400,width=100,height=50);
root.mainloop();