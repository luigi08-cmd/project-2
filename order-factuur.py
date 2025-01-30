import os
import shutil

# makes the main folder
pdf_folder_location = os.path.dirname(__file__) + r"\PDF_INVOICE"
if os.path.exists(pdf_folder_location):
    shutil.rmtree(pdf_folder_location)
os.makedirs(pdf_folder_location)

json_folder_location = os.path.dirname(__file__) + r"\JSON_INVOICE"
if os.path.exists(json_folder_location):
    shutil.rmtree(json_folder_location)
os.makedirs(json_folder_location)