import RPI.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BCM)

pirpin=6
GPIO.setup(pirpin, GPIO.IN)
counter=1
time.sleep(4)

while True:
	if GPIO.input(pirpin):
		print("motion detected")

		time.sleep(1)
		counter=counter+1

	else:
		print("testing")
		
