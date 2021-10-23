
from tkinter import *
from functools import partial 
from tkinter import messagebox
import math
root= Tk()
root.geometry("400x400")
root.title("Calculator")
def AddNum(X,Y):
    A = X.get()
    B = Y.get()
    C= int(A)+int(B)
    print("Sum =",C)
    #Entry(root, text = C ).pack()
    messagebox.showinfo("sum", C)
    return
def SubNum(X,Y):
    a = X.get();
    b = Y.get();
    c = float(a)- float(b);
    messagebox.showinfo("difference", c)
def MultiNum():
    a = X.get();
    b = Y.get();
    c = float(a)*float(b);
    messagebox.showinfo("mutliple", c);
def DiviNum():
    a = X.get();
    b = Y.get();
    c = float(a)/float(b)
    messagebox.showinfo("divided",c)
def Square():
    a = X.get();
    c = int(a)
    e = math.sqrt(c);
    messagebox.showinfo("Squareroot",e)
def percentage():
    a = X.get()
    b = Y.get()
    c = (int(a)/int(b))*100
    messagebox.showinfo("percentage",c);
def expo():
    a = X.get();
    b = Y.get();

    c = int(a)**int(b) ;
    messagebox.showinfo("expo",c)
X = StringVar()
Y = StringVar()
entr1 = Entry(root,textvariable=X).place(x = 0 , y = 0 , width = 200 , height = 200)
entr2 = Entry(root,textvariable=Y).place(x= 200 , y = 0 , width = 200 , height= 200)
Button(root, text="+", command = AddNum).place(x=0 , y = 200 ,width= 100, height = 100);
Button(root, text = "-", command = SubNum).place(x = 0, y = 300, width = 100, height = 100);
Button(root, text = "x", command = MultiNum ).place( x = 100 , y = 200 , width = 100, height= 100);
Button(root, text = "/", command = DiviNum ).place(x = 100 , y = 300 , width = 100 , height = 100) 
Button(root, text ="SquareRoot", command = Square).place(x = 200, y = 200 , width = 100 , height = 100);
Button(root, text ="percentage", command = percentage).place(x= 200 , y = 300, width = 100, height = 100)
Button(root, text ="expoential",command = expo ).place(x = 300 , y = 200, width = 100 , height = 100);
Button(root, text ="Clear").place(x = 300 , y = 300 , width = 100 , height = 100)
root.mainloop()

