import PyPDF2
pdf = open("/home/atmegarobotics/Desktop/app_development/Tkinter/Base.pdf","rb");

pdf1 = PyPDF2.PdfFileReader(pdf);

x = int(input("enter the pages you want to extract :",));
pdf2 = pdf1.getPage(x);

text = pdf2.extractText();

file1 = open(r"/home/atmegarobotics/Desktop/app_development/Tkinter/text.txt","a");
file1.writelines(text)
print("extracted successfully");
