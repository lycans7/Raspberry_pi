import time

import picamera



with picamera.PiCamera() as camera:

    camera.start_preview()

    camera.start_recording('/home/pi/parth/test_video.h264')

    time.sleep(30)

    camera.stop_recording()

    camera.stop_preview()