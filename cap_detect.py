import cv2
import numpy as np
import pytesseract

#config=('-l eng --oem 3 --psm 8  -c tessedit_char_whitelist=0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
config=('-l eng --oem 1 --psm 8 ')
def dialation_kernel( dia_elem, dia_size):
    dia_type=0
    if dia_elem==0:
        dia_type=cv2.MORPH_RECT
    elif dia_elem==1:
        dia_type=cv2.MORPH_CROSS
    elif dia_elem==2:
        dia_type=cv2.MORPH_ELLIPSE
    
    elem=cv2.getStructuringElement(dia_type, (2*dia_size+1,2*dia_size+1 ))

    print("dia type:", dia_elem,"dia size:", dia_size, elem)
    return elem

def erosion_kernel( ero_elem, ero_size):
    ero_type=0
    if ero_elem==0:
        ero_type=cv2.MORPH_RECT
    elif ero_elem==1:
        ero_type=cv2.MORPH_CROSS
    elif ero_elem==2:
        ero_type=cv2.MORPH_ELLIPSE
    
    elem=cv2.getStructuringElement(ero_type, (2*ero_size+1,2*ero_size+1 ))

    print("ero type:", ero_elem,"ero size:", ero_size, elem)
    return elem

def detectCaptchaImage(impath):
     

    img=cv2.imread(impath)
    cv2.imshow("original", img)

    ret,gray=cv2.threshold(img,127,255,cv2.THRESH_BINARY)

    cv2.imshow("threashold", gray)

    dia_elem=0
    dia_size=1

    ero_elem=1
    ero_size=1

    dia_kernel = dialation_kernel(dia_elem, dia_size)
    gray=cv2.dilate(gray, dia_kernel)
    cv2.imshow("dia", gray)

    ero_kernel = erosion_kernel(ero_elem, ero_size)
    gray=cv2.erode(gray, ero_kernel)
    cv2.imshow("ero", gray)

    
  
    result = pytesseract.image_to_string(gray,  config=config)

    print(result)
    cv2.waitKey(0)
file="test/6.png"
detectCaptchaImage(file)
