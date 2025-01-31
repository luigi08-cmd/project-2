import json
import datetime

def create_factuur_json(json_file_location):
    with open(json_file_location + '.json') as file:
        data =json.load(file)

    order = data["order"]
    klant = order["klant"]

    bedrijfsnaam = klant["naam"]
    address_klant = klant["adres"]
    poscode_klant = klant["postcode"]
    vestegings_plaats_klant = klant["stad"]
    order_nummer = order["ordernummer"]
    order_datum = order["orderdatum"]
    order_datum = order_datum.split("-")
    order_datum = datetime.date(int(order_datum[2]), int(order_datum[1]), int(order_datum[0])) 
    betaal_termijn = order["betaaltermijn"]
    betaal_termijn = float(betaal_termijn.replace("-dagen", ""))
    betaal_datum = order_datum + datetime.timedelta(betaal_termijn)
    producten_list = []
    
    for index in range(0, len(order["producten"])):
        product = order["producten"][index]
        aantal_producten = product["aantal"]
        product_naam = product["productnaam"]
        btw_percentage = product["btw_percentage"]
        btw = 1 + btw_percentage / 100
        prijs_per_stuk_excl_btw = product["prijs_per_stuk_excl_btw"]
        product_prijs = prijs_per_stuk_excl_btw * aantal_producten
        totale_prijs = product_prijs * btw
        totale_prijs = round(totale_prijs, 2)
        product_dict = {
            "product-naam": product_naam,
            "aantal": aantal_producten,
            "prijs-per-stuk": prijs_per_stuk_excl_btw,
            "totale-prijs-excl": product_prijs,
            "totale-prijs-incl": totale_prijs
        }
        producten_list.append(product_dict)

    json_structure = {
        "factuur": {
            "factuur-nummer": order_nummer,
            "factuur-datum":str( order_datum),
            "uiterlijke-betaal-datum": str(betaal_datum),
            "klant": {
                "naam": bedrijfsnaam,
                "address": address_klant,
                "postcode": poscode_klant,
                "plaats": vestegings_plaats_klant,
            },
            "producten": producten_list
        }
    }
    with open(json_file_location + "-factuur.json", mode="w", encoding="utf-8") as write_file:
        json.dump(json_structure, write_file)

create_factuur_json("2000-096")