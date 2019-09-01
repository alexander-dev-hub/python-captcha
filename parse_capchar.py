#import the necessary packages
from PIL import Image
import pytesseract
import argparse
import cv2
import os
import re
#
def parse_captcha(filename):
	"""
	Return the text for thie image using Tesseract
	"""
	img = threshold(filename)
	text= tesseract(img)
	print(text)


def threshold(filename, limit=100):
	"""
	Make text more clear by thresholding all pixels above / below this limit to white / black
    """

	spos = filename.rfind('/')
	if spos:
		path=filename[:spos]
		fn= filename[spos+1:]
		path=path+'/'
    
    # read in colour channels
	img = Image.open(filename)
    # resize to make more clearer
	m = 1.5
	img = img.resize((int(img.size[0]*m), int(img.size[1]*m))).convert('RGBA')
	pixdata = img.load()

	for y in range(img.size[1]):
		for x in range(img.size[0]):
			if pixdata[x, y][0] < limit:
				# make dark color black
				pixdata[x, y] = (0, 0, 0, 255)
			else:
				# make light color white
				pixdata[x, y] = (255, 255, 255, 255)
	img.save(path+'threshold_' + fn)
	return img.convert('L') # convert image to single channel greyscale

def tesseract(image):
     
	result = pytesseract.image_to_string(image)


	return clean(result)


def clean(s):
    """Standardize the OCR output
    """
    # remove non-alpha numeric text
    return re.sub('[\W]', '', s)

parse_captcha('test/5.png')