import pdftotext

f = open("/home/atmegarobotics/Desktop/app_development/Tkinter/Base.pdf","rb");

pdf = pdftotext.PDF(f);

f = open('/home/atmegarobotics/Desktop/app_development/Tkinter/text.txt','w')

f.write("".join(pdf))