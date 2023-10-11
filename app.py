from flask import Flask
from pdf2image import convert_from_path
import pytesseract

def convert_pdf_to_str(filename: str):
    images = convert_from_path(filename)
    full_text = ''
    for i, image in enumerate(images):
        text = pytesseract.image_to_string(image)
        full_text += text
    return full_text

print(convert_pdf_to_str(input('Enter filename to be converted:' )))
