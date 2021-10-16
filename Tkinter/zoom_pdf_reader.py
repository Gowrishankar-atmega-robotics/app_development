from tkinter import *
from tkinter import filedialog 
from tkPDFViewer import tkPDFViewer as PDF

root = Tk();
root.geometry("630x700+400+100");
root.title("PDF_READER");
root.configure(bg="gray");


Button(root,text="Open a PDF file " , width = 80 , font = " aerial 20",bd= 4).pack();
root.mainloop();