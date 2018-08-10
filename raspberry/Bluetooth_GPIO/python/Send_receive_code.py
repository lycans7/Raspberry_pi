import RPi.GPIO as gpio
import bluetooth
import time as t

LED=7

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

while(1):
    a = gpio.input(13)
    if(a == 0):
        client_socket.send("water\n")
        gpio.output(7,True)
        t.sleep(2)
    else:
       gpio.output(7,False)
gpio.cleanup()
print "Accepted connection from ",address
client_socket.close()
server_socket.close()