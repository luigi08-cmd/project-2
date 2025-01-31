from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
import os
import json
from order_json_factuur import *

def create_pdf(json_file, pdf_folder_location, pdf_name):

    # create json
    with open(json_file + ".json") as file:
        data =json.load(file)

    order = data["factuur"]
    klant = order["klant"]

    totale_prijs_excl_btw = 0

    # create file location with correct json name
    
    # klant gegevens
    bedrijfsnaam = klant["naam"]
    address_klant = klant["address"]
    poscode_klant = klant["postcode"]
    vestegings_plaats_klant = klant["plaats"]
    factuur_nummer = order["factuur-nummer"]
    order_datum = order["factuur-datum"]
    betaal_termijn = order["uiterlijke-betaal-datum"]
        


    # create pdf

    # default sizes
    width, height = A4

    # create file location with correct pdf name
    pdf_name = pdf_name + ".pdf"
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
    for index in range(0, len(order["producten"])):
        product = order["producten"][index]
        canvas.drawString(1 * inch, height - (5 + 0.2 * index) * inch, str(product["aantal"]))
        canvas.drawString(2 * inch, height - (5 + 0.2 * index) * inch, product["product-naam"])
        
        canvas.drawString(4.7 * inch, height - (5 + 0.2 * index) * inch, f"€ {str(product["prijs-per-stuk"])}")
        canvas.drawString(5.6 * inch, height - (5 + 0.2 * index) * inch, f"€ {str(product["totale-prijs-excl"])}")
        totale_prijs_excl_btw += product["totale-prijs-incl"]
        stop = index + 1
        if stop == len(order["producten"]):
            # totaal
            canvas.line(0.5 * inch, height - (5.1 + 0.2 * index) * inch, 7.5 * inch, height - (5.1 + 0.2 * index) * inch)    
            canvas.drawString(5 * inch, height - (5.3 + 0.2 * index)* inch, "totaal")
            canvas.drawString(5.6 * inch, height - (5.3 + 0.2 * index) * inch, f"€ {str(round(totale_prijs_excl_btw, 2))}")




    canvas.save()