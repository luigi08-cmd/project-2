from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
import os
import shutil
import json
from order_json_factuur import *

# makes the main folder
pdf_folder_location = os.path.dirname(__file__) + r"\PDF_INVOICE"
if os.path.exists(pdf_folder_location):
    shutil.rmtree(pdf_folder_location)
os.makedirs(pdf_folder_location)

json_folder_location = os.path.dirname(__file__) + r"\JSON_INVOICE"
if os.path.exists(json_folder_location):
    shutil.rmtree(json_folder_location)
os.makedirs(json_folder_location)

def create_pdf(json_file):

    # create json
    with open('2000-096.json') as file:
        data =json.load(file)

    order = data["order"]
    klant = order["klant"]

    totale_prijs_excl_btw = 0

    # create file location with correct json name
    pdf_name = json_file + ".json"
    file_location = os.path.join(json_folder_location , pdf_name)
    
    # klant gegevens
    bedrijfsnaam = klant["naam"]
    address_klant = klant["adres"]
    poscode_klant = klant["postcode"]
    vestegings_plaats_klant = klant["stad"]
    factuur_nummer = order["ordernummer"]
    order_datum = order["orderdatum"]
    betaal_termijn = order["betaaltermijn"]
        


    # create pdf

    # default sizes
    width, height = A4

    # create file location with correct pdf name
    pdf_name = json_file + ".pdf"
    file_location = os.path.join(pdf_folder_location , pdf_name) 
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
    
    
    

    canvas.drawString(1 * inch, height - 3 * inch, bedrijfsnaam)
    canvas.drawString(1 * inch, height - 3.2 * inch, address_klant)
    canvas.drawString(1 * inch, height - 3.4 * inch, poscode_klant)
    canvas.drawString(1 * inch, height - 3.6 * inch, vestegings_plaats_klant)
    canvas.drawString(1 * inch, height - 4.0 * inch, factuur_nummer)
    canvas.drawString(1 * inch, height - 4.2 * inch, order_datum)
    canvas.drawString(1 * inch, height - 4.4 * inch, betaal_termijn)

    # algemene product gegevens
    canvas.line(0.5 * inch, height - 4.5 * inch, 7.5 * inch, height - 4.5 * inch)
    canvas.drawString(1 * inch, height - 4.7 * inch, "aantal")
    canvas.drawString(2 * inch, height - 4.7 * inch, "omschrijving")
    canvas.drawString(5 * inch, height - 4.7 * inch, "prijs")
    canvas.drawString(5.6 * inch, height - 4.7 * inch, "totaal excl. btw")
    canvas.line(0.5 * inch, height - 4.8 * inch, 7.5 * inch, height - 4.8 * inch)

    # product gegevens 
    # for index in range(0, len(order["producten"])):
    #     product = order["producten"][index]
    #     canvas.drawString(1 * inch, height - (5 + 0.2 * index) * inch, str())
    #     canvas.drawString(2 * inch, height - (5 + 0.2 * index) * inch, )
        
    #     canvas.drawString(4.7 * inch, height - (5 + 0.2 * index) * inch, f"€ {str()}")
    #     canvas.drawString(5.6 * inch, height - (5 + 0.2 * index) * inch, f"€ {str()}")
    #     totale_prijs_excl_btw += 
    #     stop = index + 1
    #     if stop == len(order["producten"]):
    #         # totaal
    #         canvas.line(0.5 * inch, height - (5.1 + 0.2 * index) * inch, 7.5 * inch, height - (5.1 + 0.2 * index) * inch)    
    #         canvas.drawString(5 * inch, height - (5.3 + 0.2 * index)* inch, "totaal")
    #         canvas.drawString(5.6 * inch, height - (5.3 + 0.2 * index) * inch, f"€ {str(totale_prijs_excl_btw)}")




    canvas.save()
create_pdf("test")
create_pdf("test2")
create_pdf("test3")