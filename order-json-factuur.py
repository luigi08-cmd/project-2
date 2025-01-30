import json
import datetime

def create_factuur_json(json_file_name):
    with open('2000-096.json') as file:
        data =json.load(file)

    order = data["order"]
    klant = order["klant"]

    bedrijfsnaam = klant["naam"]
    address_klant = klant["adres"]
    poscode_klant = klant["postcode"]
    vestegings_plaats_klant = klant["stad"]
    factuur_nummer = order["ordernummer"]
    order_datum = order["orderdatum"]
    betaal_termijn = order["betaaltermijn"]
    betaal_datum = order_datum + datetime.timedelta(30)
    
    for index in range(0, len(order["producten"])):
        product = order["producten"][index]
        aantal_producten = product["aantal"]
        product_naam = product["productnaam"]
        btw_percentage = product["btw_percentage"]
        btw = 1 + btw_percentage / 100
        prijs_per_stuk_excl_btw = product["prijs_per_stuk_excl_btw"]
        product_prijs = prijs_per_stuk_excl_btw * aantal_producten
        totale_prijs = product_prijs * btw
        producten_dict = {
            "product-naam": product_naam,
            "aantal": aantal_producten,
            "prijs-per-stuk": prijs_per_stuk_excl_btw,
            "totale-prijs-excl": product_prijs,
            "totale-prijs-incl": totale_prijs
        }