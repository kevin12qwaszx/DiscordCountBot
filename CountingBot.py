import numpy as np
import cv2
import pyautogui
import pytesseract
import keyboard
import time
from PIL import Image
import threading

# Ensure required packages are installed:
# pip install pynput imagehash opencv-python numpy pyautogui pillow pytesseract keyboard

# Note: Install the tesseract training dataset from https://github.com/UB-Mannheim/tesseract/wiki
# Add "C:\\Program Files\\Tesseract-OCR\\tesseract.exe" to your PATH environment variable

class AutoTextBot:
    def __init__(self):
        pyautogui.FAILSAFE = False
        self.tesseract_path = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
        pytesseract.pytesseract.tesseract_cmd = self.tesseract_path

    @staticmethod
    def locate_image(image_path, confidence=0.9):
        try:
            location = pyautogui.locateOnScreen(image_path, confidence=confidence)
            if location:
                print("Image found at:", location)
                return location
            else:
                print("Image not found")
                return None
        except Exception as e:
            print("Error locating image:", e)
            return None

    @staticmethod
    def contains_image(template_path, screenshot_path, threshold=0.9):
        try:
            template = cv2.imread(template_path)
            screenshot = cv2.imread(screenshot_path)
            result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
            _, max_val, _, _ = cv2.minMaxLoc(result)
            return max_val > threshold
        except Exception as e:
            print("Error in image comparison:", e)
            return False

    @staticmethod
    def extract_text_from_image(image_path):
        try:
            img = Image.open(image_path)
            text = pytesseract.image_to_string(img)
            return text
        except Exception as e:
            print("Error extracting text from image:", e)
            return ""

    def run(self,inputlcation,userIcon ):
        event = threading.Event()

        def stop():
            event.set()
            print("Stopping bot...")

        keyboard.add_hotkey("esc", stop)

        while not event.is_set():
            image_path_match = inputlcation 

            location = self.locate_image(image_path_match)
            if not location:
                break

            x, y, width, height = int(location.left), int(location.top )- 100, 350, 200
            screenshot = pyautogui.screenshot(region=(x, y, width, height))
            screenshot_path = r'boxofCompare.png'
            screenshot.save(screenshot_path)

            user_icon_path = userIcon 
            has_image = self.contains_image(user_icon_path, screenshot_path)

            if not has_image:
                text = self.extract_text_from_image(screenshot_path)
                print("Extracted text:", text)

                try:
                    numbers = [int(item) for item in text.split() if item.isdigit()]
                    number_to_type = numbers[0] + 1 if numbers else 1

                    pyautogui.click(x + width / 2, y + 100)
                    keyboard.write(str(number_to_type))
                    keyboard.press_and_release('enter')
                    pyautogui.moveTo(0, 0)
                except Exception as e:
                    print("Error typing or clicking:", e)

            time.sleep(5)

if __name__ == '__main__':
    
    bot = AutoTextBot()
    bot.run(r'countLocation.png',r'userIcon.png')
