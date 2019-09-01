#import the necessary packages
from PIL import Image
import pytesseract
import argparse
import cv2
import os
import re
#
config=('-l eng --oem 3 --psm 8')
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
    
   
	im_gray = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
	(thresh, im_bw) = cv2.threshold(im_gray, 127, 255, cv2.THRESH_TRUNC | cv2.THRESH_OTSU)
	cv2.imwrite(path+'threshold_' + fn, im_bw)
     
	print('threshold:',thresh )
	#cv2.imshow("Over the Clouds - gray", im_bw)
	#cv2.waitKey(0)
	return im_bw # convert image to single channel greyscale

def tesseract(image):
     
	result = pytesseract.image_to_string(image,  config=config)


	return clean(result)


def clean(s):
    """Standardize the OCR output
    """
    # remove non-alpha numeric text
    return re.sub('[\W]', '', s)

parse_captcha('test/4.png')