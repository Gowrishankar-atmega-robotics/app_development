from tkinter import *
from tkPDFViewer import tkPDFViewer as pdf
import convertapi
from tkinter import filedialog
root = Tk();
root.geometry("500x500");
root.title("ODT_to_PDF_Converter");
def files():
    filename=filedialog.askopenfilename(filetypes=[("all files","*.*")])
    convertapi.api_secret = 'VBU2YahJGZ4FM8PX'
    convertapi.convert('pdf',{'File': filename }, from_format = 'odt').save_files('/home/atmegarobotics/Desktop/app_development/Tkinter/')
    
Button(root,text="Open files",command= files ,width=100 , height=1, bd=6).pack();
root.mainloop()