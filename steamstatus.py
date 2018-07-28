import time
import json
import requests as req
import RPi.GPIO as GPIO

class URL:
	self = 'https://ruulr.ee/steam/getUserState.php'
	cheese = 'https://ruulr.ee/steam/getUserState.php?steamid=76561198125118572'

# PINs
PIN_R = 23
PIN_G = 18
PIN_B = 24

# GPIO
GPIO.setmode(GPIO.BCM)

GPIO.setup(PIN_R, GPIO.OUT)
GPIO.setup(PIN_G, GPIO.OUT)
GPIO.setup(PIN_B, GPIO.OUT)

try:
	while True:

		# Get state
		res = req.get(URL.cheese)
		data = res.json()
		state = data['state']

		print 'Current state: ' + str(state)

		# Offline
		if state == 0:
			GPIO.output(PIN_R, False)
			GPIO.output(PIN_G, False)
			GPIO.output(PIN_B, False)
		# Online
		elif state == 1:
			GPIO.output(PIN_R, False)
			GPIO.output(PIN_G, True)
			GPIO.output(PIN_B, False)
		# Busy
		elif state == 2:
			GPIO.output(PIN_R, True)
			GPIO.output(PIN_G, False)
			GPIO.output(PIN_B, False)

		# Away
		elif state == 3:
			GPIO.output(PIN_R, False)
			GPIO.output(PIN_G, False)
			GPIO.output(PIN_B, True)

		# Other - unnecessary
		else:
			GPIO.output(PIN_R, False)
			GPIO.output(PIN_G, False)
			GPIO.output(PIN_B, False)

		time.sleep(1)

except KeyboardInterrupt:
	GPIO.cleanup()
