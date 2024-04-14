import re
from pdfminer.high_level import extract_pages, extract_text

def script(pdf):
    for page in extract_pages(str(pdf)):
        for element in page:
            print(element)