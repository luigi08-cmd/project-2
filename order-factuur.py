import os
import shutil
from json_factuur_pdf import *
from order_json_factuur import *

# makes the main folder
pdf_folder_location = os.path.join(os.path.dirname(__file__),"PDF_INVOICE")
if not os.path.exists(pdf_folder_location):
    os.makedirs(pdf_folder_location)


json_invoice_location = os.path.join(os.path.dirname(__file__), "JSON_INVOICE")
if not os.path.exists(json_invoice_location):
    os.makedirs(json_invoice_location)

json_order_location = os.path.join(os.path.dirname(__file__), "JSON_ORDER")
if not os.path.exists(json_order_location):
    os.makedirs(json_order_location)

json_processed_location = os.path.join(os.path.dirname(__file__), "JSON_PROCESSED")
if not os.path.exists(json_processed_location):
    os.makedirs(json_processed_location)


for name in os.listdir(json_order_location):
    name, _ = os.path.splitext(name)
    create_factuur_json(os.path.join(json_order_location, name), os.path.join(json_invoice_location, name))

for name in os.listdir(json_invoice_location):
    name, _ = os.path.splitext(name)
    create_pdf(os.path.join(json_invoice_location, name), pdf_folder_location, name)

for name in os.listdir(json_order_location):
    (os.path.join(json_order_location, name), os.path.join(json_processed_location, name))