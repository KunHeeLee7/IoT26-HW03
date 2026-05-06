# HW3

#import the necessary packages
from gpiozero import Button, MotionSensor
from picamera import PiCamera2
from time import sleep
from signal import pause

#create objects that refer to a button,
#a motion sensor and the PiCamera
button = Button(2)
pir = MotionSensor(4)
picam2 = PiCamera2()

#start the camera
picam2.configure(picam2.create_still_configuration())
picam2.start()

#image image names
i = 0

#stop the camera when the pushbutton is pressed
def stop_camera():
    picam2.stop()
    #exit the program
    exit()

#take photo when motion is detected
def take_photo():
    global i
    i = i + 1
    filename = f'/home/rpi/Desktop/image_{i}.jpg'
    picam2.capture_file(filename)
    print('A photo has been taken')
    sleep(10)

#assign a function that runs when the button is pressed
button.when_pressed = stop_camera
#assign a function that runs when motion is detected
pir.when_motion = take_photo

pause()
