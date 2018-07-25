#!/usr/bin/python
import time
import sys
import picamera

with picamera.PiCamera() as cam:
    
    def camara_image():
        cam.start_preview()
        time.sleep(2)
        cam.capture('/home/pi/parth/combine_image.jpg')
        cam.stop_preview()
        return;
    
    def camara_video():
        cam.start_preview()
        cam.start_recording('/home/pi/parth/combine_video.h264')
        time.sleep(10)
        cam.stop_recording()
        cam.stop_preview()
        return;
    print "Hello, Enter what you want to use! \n"
    count = 0
    while (count < 9):
        val = input("enter camara : 1, Recording : 2 , exit : 3 \n")
        if (val == 1):
            camara_image()
            print "Hello, you just click image! \n"
        elif (val == 2):
            camara_video()
            print "Hello, you just did recording! \n"
        else :
            count = 11
    
    print "Hello, Exit! \n"