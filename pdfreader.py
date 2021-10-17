from tkPDFViewer import tkPDFViewer as PDF
from tkinter import *
from tkinter import filedialog

root = Tk();
root.geometry("630x700+400+100");
root.title("pdf viewer");
#bg = PhotoImage(file="img19.jpg")
root.configure(background="gray");
def BF():
    fileName = filedialog.askopenfilename(title="select a PDF" , filetypes=[("text files","*.*")]);
    v1 = PDF.ShowPdf()
    v2 = v1.pdf_view(root,pdf_location = open(fileName,"r"),width=77,height=100)
    v2.pack(pady=(0,0))
Button(root,text="Open a PDF",command= BF, width=80,font= "arial 20 ",bd=4).pack();
root.mainloop();
