import serial
import time
from bluetooth import *
import RPi.GPIO as GPIO        #calling for header file which helps in using GPIOs of PI

LED=21
GPIO.setwarnings(False) 

GPIO.setmode(GPIO.BCM)     #programming the GPIO by BCM pin numbers. (like PIN40 as GPIO21)
GPIO.setup(LED,GPIO.OUT)  #initialize GPIO21 (LED) as an output Pin
GPIO.output(LED,0)

ser=serial.Serial("/dev/ttyUSB0",9600)  #change ACM number as found from ls /dev/tty/ACM*
ser.baudrate=9600

print("Socket Initialized...")
 
server_sock=BluetoothSocket( RFCOMM )   #TCP Protocol
server_sock.bind(("",PORT_ANY))
server_sock.listen(1) 
client_sock, client_info = server_sock.accept()

print ("Accepted connection from ",client_info)

while 1:

    read_ser=ser.readline()
    line=read_ser.rstrip('\r\n')
    print(line)
    if (line < "140"):
        print("Transmit Data")
        write = 'a'
        client_sock.send(write)
        GPIO.output(LED,GPIO.HIGH)
    else:
        write = 'b'
        client_sock.send(write)
        GPIO.output(LED,GPIO.LOW)


#while 1:
#    write = raw_input()
#    client_sock.send(write)

client_sock.close()
server_sock.close()
