import RPi.GPIO as GPIO 
import time

def configuration():
  GPIO.cleanup()
	GPIO.setmode(GPIO.BOARD) ## Use board pin numbering
	GPIO.setup(11, GPIO.OUT) ## Setup GPIO Pin 11 to OUT

def allumer_led(duree):
	configuration()
	GPIO.output(11,True) 
	time.sleep(duree)
	GPIO.output(11,False)
	GPIO.cleanup()

if __name__ == "__main__":
	configuration()
	allumer_led(5)
	
