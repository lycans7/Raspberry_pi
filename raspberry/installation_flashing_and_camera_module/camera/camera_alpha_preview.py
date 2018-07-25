import time
import picamera

with picamera.PiCamera() as ptr:
    # alpha can be varry between 0 to 255
    def alpha(integer):
        ptr.start_preview(alpha = integer)
        time.sleep(10)
        ptr.stop_preview()
        return
    
    count = 1
    while (count == 1):
        val = input("\n Enter value of \n alpha: 0 to 255 \n Exit: 777 \n")
        if(val >= 0 | val <=255):
            alpha(val)
            print "Entered value :=",val
        elif (val == 777):
            print "Exit"
            count = 0