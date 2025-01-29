from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
import os
import shutil
# makes the main folder
folder_location = os.path.dirname(__file__) + r"\PDF_INVOICE"
if os.path.exists(folder_location):
    shutil.rmtree(folder_location)
os.makedirs(folder_location)

# creates pdf
def create_pdf(json_file):
    # default sizes
    width, height = A4

    # create file location with correct pdf name
    pdf_name = json_file + ".pdf"
    file_location = os.path.join(folder_location , pdf_name) 
    canvas = Canvas(file_location)
    logo_location = os.path.join(os.path.dirname(__file__), "logo.png")

    # Factuur kop
    canvas.setFont("Helvetica-Bold", 20)
    canvas.drawString(1 * inch, height - 2.6 * inch, "Factuur")

    # vaste gegevens (Bedrijf gegevens afzender)
    canvas.setFont("Helvetica", 12)
    canvas.drawString(5.6 * inch, height - 0.8 * inch, "SD Solutions BV")
    canvas.drawString(5.6 * inch, height - 1.0 * inch, "Leerpark Promenade 100")
    canvas.drawString(5.6 * inch, height - 1.2 * inch, "3312 KW Dordcrecht")
    canvas.drawString(5.6 * inch, height - 1.6 * inch, "info@sd-solutions.nl")
    canvas.drawString(5.6 * inch, height - 1.8 * inch, "sdsolutions.nl")
    canvas.drawString(5.6 * inch, height - 2.0 * inch, "06 12345678")

    canvas.drawString(5.6 * inch, height - 2.4 * inch, "BTW-nummer: NL123456789B01")
    canvas.drawString(5.6 * inch, height - 2.6 * inch, "KvK-nummer: 27124701")
    canvas.drawImage(logo_location, 0.5 * inch, height - 2.3 * inch, 150, 150)
    canvas.line(0.5 * inch, height - 2.7 * inch, 7.5 * inch, height - 2.7 * inch)
    
    # klant gegevens
    bedrijfsnaam = "test"
    address_klant = "test"
    poscode_klant = "test"
    vestegings_plaats_klant = "test"
    kvk_nummer = "test"
    factuur_nummer = "test"
    order_datum = "test"
    betaal_termijn = "test"

    canvas.drawString(1 * inch, height - 3 * inch, bedrijfsnaam)
    canvas.drawString(1 * inch, height - 3.2 * inch, address_klant)
    canvas.drawString(1 * inch, height - 3.4 * inch, poscode_klant)
    canvas.drawString(1 * inch, height - 3.6 * inch, vestegings_plaats_klant)
    canvas.drawString(1 * inch, height - 4 * inch, kvk_nummer)
    canvas.drawString(1 * inch, height - 4.4 * inch, factuur_nummer)
    canvas.drawString(1 * inch, height - 4.6 * inch, order_datum)
    canvas.drawString(1 * inch, height - 4.8 * inch, betaal_termijn)

    # algemene product gegevens
    canvas.line(0.5 * inch, height - 5 * inch, 7.5 * inch, height - 5 * inch)
    canvas.drawString(1 * inch, height - 5.2 * inch, "aantal")
    canvas.drawString(2 * inch, height - 5.2 * inch, "omschrijving")
    canvas.drawString(5 * inch, height - 5.2 * inch, "prijs")
    canvas.drawString(5.6 * inch, height - 5.2 * inch, "totaal excl. btw")
    canvas.line(0.5 * inch, height - 5.3 * inch, 7.5 * inch, height - 5.3 * inch)

    # product gegevens
    

    canvas.save()
create_pdf("test")