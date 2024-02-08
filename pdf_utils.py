import os
from PyPDF2 import PdfReader
from wand.image import Image

def extract_pdf_pages(pdf_path):
    pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]
    folder_path = os.path.dirname(pdf_path)
    
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PdfReader(pdf_file)
        
        for page_num in range(len(pdf_reader.pages)):
            with Image(filename=f'{pdf_path}[{page_num}]') as img:
                img.save(filename=f'{folder_path}/{pdf_name}_{page_num + 1}.png')
