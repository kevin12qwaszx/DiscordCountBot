import numpy as np
import cv2
import pyautogui
import pytesseract
import keyboard
import time
from PIL import Image
import imagehash


#pip install imagehash
#pip install opencv-python
#pip install numpy
#pip install pyautogui
#pip install pillow
#pip install opencv-python
#pip install pytesseract
#pip install keyboard



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
    
    pyautogui.FAILSAFE = False
    
    #-------------------------------------------------------------------------------------------
    while True: 
        if keyboard.is_pressed('ctrl'):
            break
            pyautogui.FAILSAFE = True
        #This could be a funtion to
        # 
        # 
        # ask for location
        # force use of ImageNotFoundException
        window_title = "Discord"
        target_window = pyautogui.getWindowsWithTitle(window_title)[0]
        target_window.activate()
            
            
        try:
            image_path_Match = r'C:\Users\kevin\OneDrive\Desktop\DiscordCountBot\countLocation.png'  # Replace with the path to your image
            location = pyautogui.locateOnScreen(image_path_Match, confidence=0.9)
            if location:
                print("Image found at:", location)
            else:
                print("Image not found")
                break
        except pyautogui.ImageNotFoundException:
            print('Image not found on the screen.')
            break
        except Exception as e:
            print("Error:", e)
        time.sleep(6)
        #This next step could be check if it has my next icon on screen shot location

        # need to play data location 
        x = location[0]  # X-coordinate of the top-left corner
        y = location[1]-100  # Y-coordinate of the top-left corner 
        #The in take of Y- coordinate should have 100 less
        print("------------------------")
        print(location[1])
        width = 350  # Width of the region
        height = 200  # Height of the region

        # Take the screenshot
        screenshot = pyautogui.screenshot(region=(int(x), int(y), int(width), int(height)))

        # Save the screenshot
        screenshot.save("boxofCompare.png")
        
        # this could make into a function and reutrn true and False
        def contains_image(image, template):
            result = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
            _, max_val, _, _ = cv2.minMaxLoc(result)
            return max_val > 0.8  # Adjust threshold as needed

        image = cv2.imread(r'C:\Users\kevin\OneDrive\Desktop\DiscordCountBot\userIcon.png')
        template = cv2.imread(r'C:\Users\kevin\OneDrive\Desktop\DiscordCountBot\boxofCompare.png')

        #set back to true/ i need to test------------------------
        hasImage=False
        if contains_image(image, template):
            #hasImage = True
            print("The image contains the template.")
        else:
            print("The image does not contain the template.")
            hasImage= False
        
        if hasImage==False:
                imag = cv2.imread(r'C:\Users\kevin\OneDrive\Desktop\DiscordCountBot\boxofCompare.png')
                gray = cv2.cvtColor(imag, cv2.COLOR_BGR2GRAY)

                # Performing OTSU threshold
                _, thresh_image = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
                cv2.imwrite('preprocessed_image.jpg', thresh_image)
                extracted_text = pytesseract.image_to_string(thresh_image)

                aNew= extracted_text.split("\n") 
                print(aNew)
                
                pyautogui.click(x+location[3]/2,y+100)
                # Write a number 
                keyboard.write('12345')
                
                # Press enter
                keyboard.press_and_release('enter')
                pyautogui.moveTo(0, 0)
                

        