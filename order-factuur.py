import os
import shutil
from json_factuur_pdf import *
from order_json_factuur import *

# makes the main folder
pdf_folder_location = os.path.join(os.path.dirname(__file__),"PDF_INVOICE")
if os.path.exists(pdf_folder_location):
    shutil.rmtree(pdf_folder_location)
os.makedirs(pdf_folder_location)

json_invoice_location = os.path.join(os.path.dirname(__file__), "JSON_INVOICE")
if os.path.exists(json_invoice_location):
    shutil.rmtree(json_invoice_location)
os.makedirs(json_invoice_location)

json_order_location = os.path.join(os.path.dirname(__file__), "JSON_ORDER")

json_processed_location = os.path.join(os.path.dirname(__file__), "JSON_PROCESSED")
if os.path.exists(json_processed_location):
    shutil.rmtree(json_processed_location)
os.makedirs(json_processed_location)

