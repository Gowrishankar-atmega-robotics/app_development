from tkinter import *
from docx2pdf import convert
from tkinter import filedialog
from tkinter.ttk as ttk 
from tkinter.messagebox import showinfo

root = Tk();
root.title("word to pdf");
def openfile():
    filename = filedialog(filetype=[("docx","*.docx")]);
    convert(file.name,'/convert.pdf')
    showinfo("Done","File Succesfully Converted")

label = tk.Label(root, text= "Choose File:- ")
label.grid(row=0, column=0)

button = ttk.Button(root, text="Select", width=30, command=openfile)
button.grid(row=0, column=1)

root.mainloop()