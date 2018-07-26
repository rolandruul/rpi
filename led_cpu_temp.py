# RPi 3 CPU Temperature indicator
import re
import time
import commands
import RPi.GPIO as GPIO

# Temperature limit
# Limit where the led switch takes place
TEMP_LIMIT = 53

# Broadcom PIN-s
PIN_LED_BLUE = 18
PIN_LED_RED = 23

# Broadcom SOC Channel
GPIO.setmode(GPIO.BCM)

# Set up the pins
GPIO.setup(PIN_LED_BLUE, GPIO.OUT)
GPIO.setup(PIN_LED_RED, GPIO.OUT)

try :

    while True:
    
        # Get and format temp
        data = commands.getstatusoutput("/opt/vc/bin/vcgencmd measure_temp")[1]   
        temp = float(re.sub('[^0-9,.]', '', data))
    
        # Print current temp
        print 'RPI3 Temperatuur: ' + str(temp)

        # It's 'hot' when its >= 53 degrees Celsius (just for testing)
        if temp >= TEMP_LIMIT:
            GPIO.output(PIN_LED_BLUE, False)
            GPIO.output(PIN_LED_RED, True)
        else:
            GPIO.output(PIN_LED_BLUE, True)
            GPIO.output(PIN_LED_RED, False)    

        time.sleep(1)

except KeyboardInterrupt:
    
    # Turn off the leds
    GPIO.output(PIN_LED_BLUE, False)
    GPIO.output(PIN_LED_RED, False)

    # GPIO cleanup
    GPIO.cleanup()
