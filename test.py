from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas

def create_invoice_pdf(filename):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter

    # Factuur kop
    c.setFont("Helvetica-Bold", 20)
    c.drawString(1 * inch, height - 1 * inch, "Factuur")

    # Bedrijfsinformatie
    c.setFont("Helvetica", 12)
    c.drawString(1 * inch, height - 1.5 * inch, "Bedrijf Naam")
    c.drawString(1 * inch, height - 1.7 * inch, "Adresregel 1")
    c.drawString(1 * inch, height - 1.9 * inch, "Adresregel 2")
    c.drawString(1 * inch, height - 2.1 * inch, "Telefoon: 012-3456789")
    c.drawString(1 * inch, height - 2.3 * inch, "Email: info@bedrijf.nl")

    # Lijn
    c.line(0.5 * inch, height - 2.5 * inch, 7.5 * inch, height - 2.5 * inch)

    # Factuurregels kop
    c.drawString(1 * inch, height - 2.7 * inch, "Omschrijving")
    c.drawString(4 * inch, height - 2.7 * inch, "Aantal")
    c.drawString(5.5 * inch, height - 2.7 * inch, "Prijs")
    c.drawString(6.5 * inch, height - 2.7 * inch, "Totaal")

    # Lijn
    c.line(0.5 * inch, height - 2.8 * inch, 7.5 * inch, height - 2.8 * inch)

    # Factuurregels (zonder data)
    for i in range(5):  # Voor 5 lege regels
        c.drawString(1 * inch, height - (3 + i * 0.5) * inch, "Omschrijving...")
        c.drawString(4 * inch, height - (3 + i * 0.5) * inch, "0")
        c.drawString(5.5 * inch, height - (3 + i * 0.5) * inch, "€ 0,00")
        c.drawString(6.5 * inch, height - (3 + i * 0.5) * inch, "€ 0,00")

    # Lijn
    c.line(0.5 * inch, height - (3 + 5 * 0.5) * inch, 7.5 * inch, height - (3 + 5 * 0.5) * inch)

    # Totaal
    c.drawString(5.5 * inch, height - (3 + 5 * 0.5 + 0.5) * inch, "Totaal:")
    c.drawString(6.5 * inch, height - (3 + 5 * 0.5 + 0.5) * inch, "€ 0,00")

    c.save()

# Maak de PDF
create_invoice_pdf("factuur.pdf")