import bluetooth as blue
import RPi.GPIO as gpio
import time as t

loop = True
while loop:
    result = blue.lookup_name('88:79:7E:2B:C1:25', timeout=20)
    if (result == None):
        print "not detected"
    else:
        print " Button found"
    break


t.sleep(5)

server_sock=blue.BluetoothSocket( blue.L2CAP )
port = 0x1001
server_sock.bind(("",port))
server_sock.listen(1)
print "listening on port %d" % port
bd_addr = '01:AC:78:E6:EF:7F'
service_matches = blue.find_service( name = None, uuid = None, address = bd_addr)

if len(service_matches) == 0:

    print "cound't find service"
    
first_match = service_matches[0]
port = first_match["port"]
name = first_match["name"]
host = first_match["host"]
protocol = first_match["protocol"]

print port
print name
print host
print protocol

server_sock.close()

gpio.setmode(gpio.BOARD)
gpio.setup(7,gpio.OUT)
gpio.setup(13,gpio.IN,pull_up_down=gpio.PUD_DOWN)
while(1):
    print"%d",gpio.input(13)
    a = gpio.input(13)
    if(a == 0):
        gpio.output(7,True)
    else:
       gpio.output(7,False)
gpio.cleanup()


