# About

You may be wondering what good a project like this would be? It's a good question. As I was walking home one day, it occurred to me that HTML code could be extracted directly from images on a PDF file, as it does. So I figured I would code it as a proof of concept to see how reliably OCR could be used to read HTML. Using Flask as a middle-man in the procedure was an easy way to test this concept, so I went ahead and coded this.

The OCR implemented in the project can be fine-tuned to support code better, however I am not sure whether I will work on it too much considering the proof of concept is done, and the current version is able to read HTML moderately well. JS seems to push its boundaries due to the syntax's use of characters such as \` or ' which are often interpreted as one or the other, causing issues.

Now that this concept has been coded, I suppose I could use it improve my handwriting..

# How To Use

## 1. Environment

I coded this on a Lubuntu 22.04 with Python 3.10.12. Anything higher than Python 3.8 should in theory work as it would support type annotations and the libraries used in the project.

While tesserract does work on Windows, this readme assumes you have Ubuntu, or something that can run apt. 

## 2. Setting up venv

It may be worthwhile setting up a virtual environment (or venv, for short):

`$ python3 -m venv venv`

and it may then be useful to hop over to that venv:

`$ source venv/bin/activate`

## 3. Installing requirements

First we need to install tesseract itself:

`$ sudo apt install tesseract-ocr`

Now we can proceed to installing the pip modules:

`$ pip3 install -r requirements.txt`

## 4. Tossing some PDFs where they belong

Make a folder `pdfs` if it is not present in the root folder of the web app already. Toss any PDFs in this folder that will be used in the web app.

## 5. Run the web app!

Now, the finishing touch:

`$ flask run`

# Support

If anyone does for some reason decide to use this library I made, feel free to reach out.

