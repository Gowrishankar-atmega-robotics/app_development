from tkinter import *
from tkPDFViewer import tkPDFViewer as pdf
from tkinter import filedialog
import pdftotext
root = Tk()
root.geometry("500x500");
root.title("PDFtoTEXT")
def BF():
    filename = filedialog.askopenfilename(title="Select pdf",filetypes=[("text files","*.pdf")])
    v1 = open(filename,"rb")
    pd = pdftotext.PDF(v1)
    v2 = open('/home/atmegarobotics/Desktop/app_development/Tkinter/text.txt','w')
    v2.write("".join(pd))
Button(root,text="PDF to TexT",command=BF , width= 100,height=1 , font= "Aerial 20" , bd=6).pack();
root.mainloop()
