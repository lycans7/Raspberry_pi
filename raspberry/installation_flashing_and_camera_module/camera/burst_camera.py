import time
import picamera

with picamera.PiCamera() as p:
    def burstClick(int):
        p.start_preview()
        for i in range (int):
            time.sleep(3)
            p.capture('/home/pi/parth/burst/image%s.jpg' % i)
        p.stop_preview()
        return
        
    count = 1
    while (count == 1):
        int = input("\n Number of burst \n Exit: 0 \n")
        if(int > 0 ):
            burstClick(int)
            print " \n Entered value :=",int
        else:
            print "\n Exit \n"
            count = 0