import numpy as np
import cv2
import pyautogui
import pytesseract

from PIL import Image


#pip install opencv-python
#pip install numpy
#pip install pyautogui
#pip install pillow
#pip install opencv-python
#pip install pytesseract

# need to install the train data set on tesseract
# https://github.com/UB-Mannheim/tesseract/wiki
# "C:\Program Files\Tesseract-OCR\tesseract.exe" Add to your path env


class autoText: 
    def __init__(self):
        pyautogui.FAILSAFE = True
        
    def nav_and_take(self):
        pass

if __name__ == '__main__':
    
    # nees this path to ran the train data
    pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

    #----------------------------------------------------
    #This set take a screen shop and save it

    image = pyautogui.screenshot()
    #Add to your own path
    image.save(r"C:\Users\kevin\OneDrive\Desktop\DiscordCountBot\image1.png")
    
    #------------------------------------------------------------------
    #This set will read and product me all the text of the image 
    
    imag = cv2.imread(r'C:\Users\kevin\OneDrive\Desktop\DiscordCountBot\myTurn.png')
    gray = cv2.cvtColor(imag, cv2.COLOR_BGR2GRAY)

    # Performing OTSU threshold
    _, thresh_image = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
    cv2.imwrite('preprocessed_image.jpg', thresh_image)
    extracted_text = pytesseract.image_to_string(thresh_image)


    print(list[extracted_text])
    #------------------------------------------------------------
    # looks like i need to find my counting text and increase the image upward
    # then i will check if it i have my icon.
    # if not there i will check the number of the tab
    # After ward i will just need to input it.
    
    

    # Find the image/icon on the screen
    image_location = pyautogui.locateOnScreen('image.png')

    if image_location:
        # Take a screenshot of the region containing the image
        screenshot = pyautogui.screenshot(region=(image_location.left, image_location.top, image_location.width, image_location.height))
        screenshot.save('screenshot.png')
    else:
        print("Image not found.")

