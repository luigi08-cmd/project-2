import os
import shutil
from json_factuur_pdf import *
from order_json_factuur import *

# makes the main folder
pdf_folder_location = os.path.dirname(__file__) + r"\PDF_INVOICE"
if os.path.exists(pdf_folder_location):
    shutil.rmtree(pdf_folder_location)
os.makedirs(pdf_folder_location)

json_invoice_location = os.path.dirname(__file__) + r"\JSON_INVOICE"
if os.path.exists(json_invoice_location):
    shutil.rmtree(json_invoice_location)
os.makedirs(json_invoice_location)

json_order_location = os.path.dirname(__file__) + r"\JSON_ORDER"
if os.path.exists(json_order_location):
    shutil.rmtree(json_order_location)
os.makedirs(json_order_location)

json_processed_location = os.path.dirname(__file__) + r"\JSON_PROCESSED"
if os.path.exists(json_processed_location):
    shutil.rmtree(json_processed_location)
os.makedirs(json_processed_location)

