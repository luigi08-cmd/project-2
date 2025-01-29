from reportlab.pdfgen.canvas import Canvas
import os

# makes the main folder
folder_location = os.path.dirname(__file__) + r"\PDF_INVOICE"
if not os.path.exists(folder_location):
    os.makedirs(folder_location)

# create file location with correct pdf name
pdf_name = "file_name.pdf"
file_location = os.path.join(folder_location , pdf_name) 
print(file_location)

# ask the user for information
text = "Hello World!"

# creates pdf
canvas = Canvas(file_location)
canvas.drawString(72,792, text)
canvas.save()