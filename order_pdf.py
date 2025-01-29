from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
import os

# makes the main folder
folder_location = os.path.dirname(__file__) + r"\PDF_INVOICE"
if not os.path.exists(folder_location):
    os.makedirs(folder_location)

# creates pdf
def create_pdf(file_name):
    # default sizes
    width, height = A4

    # create file location with correct pdf name
    pdf_name = file_name + ".pdf"
    file_location = os.path.join(folder_location , pdf_name) 

    # ask the user for information
    canvas = Canvas(file_location)
    canvas.drawString(72,792, )
    canvas.save()