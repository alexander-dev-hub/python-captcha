# draw histogram in python. 
import cv2
import numpy as np
 
print(cv2.__version__)


def morph_ero_dil():
    img = cv2.imread('test/alpha.jpg', cv2.IMREAD_GRAYSCALE)
    kernel = np.ones((3,3), np.uint8)

    erosion= cv2.erode(img, kernel, iterations=1)
    dilation= cv2.dilate(img, kernel, iterations=1)
    cv2.imshow("org", img)
    cv2.imshow("ersoiom", erosion)
    cv2.imshow("dilation",dilation)
    cv2.waitKey(0)

def morph_open_close():
    img1 = cv2.imread('test/opening.jpg', cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread('test/closing.jpg', cv2.IMREAD_GRAYSCALE)
    kernel = np.ones((5,5), np.uint8)

    opening= cv2.morphologyEx(img1,cv2.MORPH_OPEN,  kernel)
    closing= cv2.morphologyEx(img2,cv2.MORPH_CLOSE, kernel)
    
    cv2.imshow("opening", opening)
    cv2.imshow("closing",closing)
    cv2.waitKey(0)
def morph_sci_hub(imgpath):
    img1 = cv2.imread(imgpath, cv2.IMREAD_GRAYSCALE)
     
    kernel = np.ones((3,3), np.uint8)

    opening= cv2.morphologyEx(img1,cv2.MORPH_OPEN,  kernel)
    closing= cv2.morphologyEx(img1,cv2.MORPH_CLOSE, kernel)
    
    cv2.imshow("origin", img1)
    cv2.imshow("opening", opening)
    cv2.imshow("closing",closing)
    cv2.waitKey(0)

morph_sci_hub('test/sci-hub1.png')
