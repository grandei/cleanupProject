import RPi.GPIO as GPIO
import time

class ObstacleDetection:
    def __init__(self, trigger_pin, echo_pin):
        self.trigger_pin = trigger_pin
        self.echo_pin = echo_pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(trigger_pin, GPIO.OUT)
        GPIO.setup(echo_pin, GPIO.IN)
    
    def get_distance(self):
        # Send trigger pulse
        GPIO.output(self.trigger_pin, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(self.trigger_pin, GPIO.LOW)

        # Wait for echo pulse
        while GPIO.input(self.echo_pin) == 0:
            start_time = time.time()
        while GPIO.input(self.echo_pin) == 1:
            end_time = time.time()

        # Calculate distance (in cm)
        duration = end_time - start_time
        distance = (duration * 34300) / 2
        return distance
