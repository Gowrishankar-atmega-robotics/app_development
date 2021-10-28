

#**********************************it's code not completed will update soon***************************************


from tkinter import *
from functools import partial
root = Tk();
root.geometry("500x500");

def one():
    global X ;
    #1 = str("1");
    
    Entry(root, textvariable= 1).place(x = 0,y = 40, width = 250 , height= 200 )
def two():
    global Y ;
   # 2  = str("2");
    Entry(root, textvariable= 2 ).place(x = 250 , y = 40 , width = 250 , height= 200)
#X = StringVar();
#Y = StringVar();
def addnum():
    global a , b ;
    a = X.get();
    b = Y.get();
    c = int(a)+int(b);
    print("sum = ", c);
    return 
Button(root, text = " advanced setting" ).place(x = 0 , y = 0 , width = 500 , height = 45 )
Entry(root,textvariable = X ).place(x = 0 , y = 40, width=500,height=200 );
#Entry(root, textvariable= Y ).place(x = 250 , y = 40 , width =250 , height=200);
#AddNum= partial(addnum, X,Y)
#bt1 = Button(root, text="Add", command = addnum).pack()
Button(root, text = "1" , command = one ).place(x = 0 , y = 420,width=90 , height=90);
Button(root, text ="2" , command = two).place(x = 90, y = 420 , width= 90 , height=90);
Button(root, text = "3").place(x = 180 , y = 420 , width = 90 , height = 90);
Button(root,text="4").place(x = 0 , y = 330 , width = 90 , height = 90);
Button(root,text="5").place(x = 90 , y = 330 , width = 90 , height= 90);
Button(root,text="6").place(x = 180, y = 330 , width = 90 , height= 90);
Button(root,text="7").place(x = 0 , y = 240 , width = 90 , height = 90);
Button(root,text="8").place(x = 90 , y = 240 , width = 90 , height = 90);
Button(root, text="9").place(x = 180 , y = 240 , width = 90 , height = 90);
#Button(root,text="10").pack()

root.mainloop()

#********************************************not completed**************************************************

