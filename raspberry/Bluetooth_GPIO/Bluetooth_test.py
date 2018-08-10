#/usr/bin/env python

import time
import bluetooth
from wakeonlan import send_magic_packet as wol

phone = "88:79:7E:2B:C1:25"

def search():         
  devices = bluetooth.discover_devices(duration = 5, lookup_names = True)
  print devices
  return devices
print "0"
True = 1
while True:
    
    print "0"
    results = search()
    print "1"
    for addr, name in results:
        if addr == phone:
            wol.send_magic_packet('88:79:7E:2B:C1:25')

    time.sleep(3)