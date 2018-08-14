import serial
import RPi.GPIO as gpio
import bluetooth
import time as t

LED=7

ser=serial.Serial("/dev/ttyUSB0",9600)  #change ACM number as found from ls /dev/tty/ACM*
ser.baudrate=9600

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
gpio.setup(7,gpio.OUT)
gpio.setup(13,gpio.IN,pull_up_down=gpio.PUD_DOWN)

server_socket=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
 
port = 1
server_socket.bind(("",port))
server_socket.listen(1)
 
client_socket,address = server_socket.accept()
print "Accepted connection from ",address

while 1:
    read_ser=ser.readline()
    line=read_ser.rstrip('\r\n')
    print(line)
    if (line < "140"):
        print("Transmit Data")
        write = 'a'
        client_socket.send(write)
        gpio.output(LED,gpio.HIGH)
    else:
        write = 'b'
        client_socket.send(write)
        gpio.output(LED,gpio.LOW)
gpio.cleanup()

client_socket.close()
server_socket.close()
