from flask import Flask, request, render_template
from pdf2image import convert_from_path
import pytesseract

PDF_PATH = "pdfs/"

def convert_pdf_to_str(filename: str):
    try:
        images = convert_from_path(PDF_PATH + filename)
        full_text = ''
        for i, image in enumerate(images):
            text = pytesseract.image_to_string(image)
            full_text += text
        return full_text
    except:
        return ''

app: Flask = Flask(__name__)

@app.route("/")
def homepage():
    filename = request.args.get('filename')
    if filename is not None:
        output = convert_pdf_to_str(filename)
        if output != '':
            return output
    return render_template('home.html')
