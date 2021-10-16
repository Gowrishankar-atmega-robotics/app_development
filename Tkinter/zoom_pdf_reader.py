from tkinter import *
from tkinter import filedialog 
from tkPDFViewer import tkPDFViewer as pdf

root = Tk();

root.geometry("500x500");
def inc():
    global x ;
    global y;
    x = 500 
    y = 500
    x+=100;
    y+=100;
    root.geometry(f'{x}x{y}')
def dec():
    global x , y ;
    x , y = 400 , 400 ;
    x-=100
    y-=100
    root.geometry(f'{x}x{y}')
        
root.title("PDF_READER");
root.configure(bg="gray");
     
def BF():
    filename=filedialog.askopenfilename(title="Select PDF",filetypes=[("select file","*.pdf"),("select text","*.txt")]);
    v1 = pdf.ShowPdf();
    v2 = v1.pdf_view(root,width=70 , height= 100 ,pdf_location=open(filename,'r')).pack(pady=(0,0))
Button(root, text="+",command= inc).pack()
Button(root, text="-" ,command = dec).pack()
Button(root,text="Open a PDF file " ,command = BF , width = 80 , font = " aerial 20",bd= 4).pack();
root.mainloop();