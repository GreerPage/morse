import RPi.GPIO as GPIO
import time
#import morseKey1

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

def dot():
	GPIO.output(18, True)
	print('.', end = '')
	time.sleep(0.2)
	GPIO.output(18, False)
	#print(' ', end = '')
	time.sleep(0.1)
def dash():
	 GPIO.output(18, True)
	 print('-', end = '')
	 time.sleep(0.6)
	 GPIO.output(18, False)
	 #print(' ', end = '')
	 time.sleep(0.1)
def space():
	GPIO.output(18, False)
	print('/ ', end = '')
	time.sleep(1.4)
def letterspace():
	GPIO.output(18, False)
	print(' ', end = '')
	time.sleep(0.6)
#morseKey1.texttomorse('hello i am greer')
