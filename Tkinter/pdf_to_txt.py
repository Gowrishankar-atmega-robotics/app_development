
import pdftotext
with open("/home/atmegarobotics/Desktop/app_development/Tkinter/Base.pdf", "rb") as f:
    pdf = pdftotext.PDF(f)
 
# Save all text to a txt file.
with open('/home/atmegarobotics/Desktop/app_development/Tkinter/text.txt', 'w') as f:
    f.write("\n\n".join(pdf))
