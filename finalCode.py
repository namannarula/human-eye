import os
import RPi.GPIO as GPIO
from gtts import gTTS
import vlc


from google.cloud import vision
client = vision.ImageAnnotatorClient()

GPIO.setmode(GPIO.BCM)

GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def capture():
    os.system('fswebcam -r 320x240 -S 3 --jpeg 50 --save /home/pi/Desktop/image.jpg')

def final():
    capture() 
 

    with open('image.jpg', 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.logo_detection(image=image)


    response = client.label_detection(image=image)
    labels = response.label_annotations
    str = " "
    
    for label in labels:   
        str += label.description + " | "
        

    print(str)
    strObj = "Hello. Some of of the relevant results are, ." + str  
    tts = gTTS(strObj, lang='en')    
    tts.save("labels.mp3")
    player = vlc.MediaPlayer("labels.mp3")
    player.play()
    


while True:
    input_state = GPIO.input(24)   
    if input_state == False:
        final()

    
