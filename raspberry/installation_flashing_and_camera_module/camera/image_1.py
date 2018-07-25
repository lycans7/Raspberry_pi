import time

import picamera

with picamera.PiCamera() as camera:

    camera.start_preview()
    
    time.sleep(5) #delay 5 sec.

    camera.capture('/home/pi/parth/test.jpg')

    camera.stop_preview()
