#------------------Funktion-HC-SR501-----------------------

from machine import Pin
import time
 
ldr = Pin(2, Pin.IN)     # create input pin on GPIO2

while True:
	if ldr.value():
            print("Detektiert")0
        else:
            print("NICHTS Detektiert")
	time.sleep(1)