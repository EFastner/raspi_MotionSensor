import RPi.GPIO as GPIO
import time
import signal
import sys

#Define a function to clean up the GPIO board
def cleanpins(signal, frame):
    GPIO.cleanup()
    print("\n")
    sys.exit(0)

#Set cleanup handler to run on interupt
signal.signal(signal.SIGINT, cleanpins)

#Set GPIO to BCM
GPIO.setmode(GPIO.BCM)

#Set the pin with the output for the sensor
sensor_pin = 17

GPIO.setup(sensor_pin, GPIO.IN)

while True:
    state = GPIO.input(sensor_pin)

    if state == 1:
        print("Motion Detected")
    time.sleep(.1)
