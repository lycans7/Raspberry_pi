import time
import picamera

with picamera.PiCamera() as cam:
    
    def rotate90():
        cam.rotation = 90
        cam.start_preview()
        time.sleep(10)
        cam.stop_preview()
        return;

    def rotate180():
        cam.rotation = 180
        cam.start_preview()
        time.sleep(10)
        cam.stop_preview()
        return;

    def rotate270():
        cam.rotation = 270
        cam.start_preview()
        time.sleep(10)
        cam.stop_preview()
        return;

    def rotate0():
        cam.rotation = 0
        cam.start_preview()
        time.sleep(10)
        cam.stop_preview()
        return;

    data = 1
    while (data == 1):
        val = input("\n Enter the choice to rotate the camera\n 0: default \n 1: 90 \n 2: 180 \n 3: 270 \n anykey: exit \n")
        if(val == 1):
            rotate90()
            print "\n you rotate 90* \n"
        elif (val == 2):
            rotate180()
            print "\n you rotate 180* \n"
        elif (val == 3):
            rotate270()
            print " \n you rotate 270* \n"
        elif (val == 0):
            rotate0()
            print "\n you rotate Default \n"
        else:
          print "\n Exit \n"
          data = 0