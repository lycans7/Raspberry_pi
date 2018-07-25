# so many different effect we work on this code

import time
import picamera
from picamera import PiCamera ,Color # special case if import multiple from super , PiCamera object 
with picamera.PiCamera() as cam:
    # in the function we change resolution and framerate 1 for default for both
    
    def resolutionFramerate(int1,int2,int3):
        cam.resolution = (int1 ,int2)
        cam.framerate = int3
        cam.start_preview()
        cam.capture('/home/pi/parth/effect_resolutionFramerate.jpg')
        time.sleep(3)
        cam.stop_preview()
        return
    
    # change the text and height of text
    
    def annotation(string,size):
        cam.annotate_text = string
        cam.annotate_text_size = size
        cam.annotate_background = Color('blue')
        cam.annotate_foreground = Color('yellow')
        cam.start_preview()
        cam.capture('/home/pi/parth/effect_annotation_size.jpg')
        time.sleep(3)
        cam.stop_preview()
        return
        
    # brightness and the contrast default is 50 50
    
    def brightnessContrast(brightness,contrast):
        cam.resolution = (8192,4320)
        cam.brightness = brightness
        cam.contrast = contrast
        cam.start_preview()
        cam.capture('/home/pi/parth/effect_brightness_contrast.jpg')
        time.sleep(3)
        cam.stop_preview()
        return

    def colorchanges(int):
        if(int == 1):
            cam.image_effect = 'colorswap'
            cam.start_preview()
            cam.capture('/home/pi/parth/effect_colorswap.jpg')
            time.sleep(3)
            cam.stop_preview()
        elif(int == 2):
            cam.start_preview()
            for effect in cam.IMAGE_EFFECTS:
                cam.image_effect = effect
                cam.annotate_text = "Effect: %s" % effect
                time.sleep(3)
            cam.stop_preview()
        elif(int == 3):
            cam.start_preview()
            cam.awb_mode = 'sunlight'
            time.sleep(5)
            cam.capture('/home/pi/parth/sunlight.jpg')
            cam.stop_preview()
        elif(int == 4):
            cam.start_preview()
            cam.exposure_mode = 'beach'
            time.sleep(5)
            cam.capture('/home/pi/parth/beach.jpg')
            cam.stop_preview()
        return
            
    count = 1
    while (count == 1):
        int = input("\n Enter the choice \n 1: resolution framerate \n 2: annotation \n 3: brightness contrast \n 4: colorchange \n 5: exit \n")
        if (int == 1):
            int1 = input("\n Enter the resolution width = 1 for default \n")
            int2 = input("\n Enter the resolution height = 1 for default \n")
            int3 = input("\n Enter the framerate = 1 for default \n")
            if(int1 == 1 | int2 == 1 & int3 != 1):
                resolutionFramerate(8192,4320,15)
            elif(int3 == 1 & int1 != 1 | int2 != 1):
                resolutionFramerate(int1,int2,15)
            elif(int3 == 1 & int1 == 1 | int2 == 1):
                resolutionFramerate(1920,1080,15)
            else:
                resolutionFramerate(int1,int2,int3)    
        elif(int == 2):
            str = raw_input('Enter the string ')
            print"hello :-",str
            size = input("\n height of string \n")
            annotation(str,size)
        elif(int == 3):
             brightness = input("\n Enter the brightness = 1 for default \n")
             contrast = input("\n Enter the contrast = 1 for default \n")
             if(brightness == 1 & contrast != 1):
                 brightnessContrast(50,contrast)
             elif (brightness != 1 & contrast == 1):
                 brightnessContrast(brightness,50)
             elif (brightness == 1 & contrast == 1):
                 brightnessContrast(50,50)
             else:
                 brightnessContrast(brightness,contrast)
        elif(int == 4):
            int = input("\n Enter the value \n 1: colorswap \n 2: IMAGE_EFFECTS \n 3: sunlight \n 4: beach \n")
            colorchanges(int)
        elif(int == 5):
            print"\n Exit \n"
            count = 0