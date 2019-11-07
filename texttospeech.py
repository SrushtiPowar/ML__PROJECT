from PIL import Image
import pytesseract
import pyttsx3
import time
import cv2
camera_port = 0
camera = cv2.VideoCapture(camera_port)
time.sleep(0.1)  # If you don't wait, the image will be dark
return_value, image = camera.read()
cv2.imwrite("opencv2.png", image)
imgtxt=pytesseract.image_to_string(Image.open('opencv2.png'))
print(imgtxt)
engine = pyttsx3.init()
rate = engine.getProperty('rate')           #getting details of current speaking rate
#print (rate)                               #printing current voice rate
engine.setProperty('rate', 125)
voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)
engine.say('The text is')
engine.say(imgtxt)
engine.runAndWait()
