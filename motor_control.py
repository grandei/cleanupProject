import RPi.GPIO as GPIO

class MotorControl:
    def __init__(self, motor_left_pins=(23, 24), motor_right_pins=(27, 22)):
        GPIO.setmode(GPIO.BCM)
        self.motor_left_pins = motor_left_pins
        self.motor_right_pins = motor_right_pins
        
        # Initialize pins
        for pin in motor_left_pins + motor_right_pins:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.LOW)

    def forward(self):
        GPIO.output(self.motor_left_pins[0], GPIO.HIGH)
        GPIO.output(self.motor_left_pins[1], GPIO.LOW)
        GPIO.output(self.motor_right_pins[0], GPIO.HIGH)
        GPIO.output(self.motor_right_pins[1], GPIO.LOW)

    def stop(self):
        for pin in self.motor_left_pins + self.motor_right_pins:
            GPIO.output(pin, GPIO.LOW)

    def turn_left(self):
        GPIO.output(self.motor_left_pins[0], GPIO.LOW)
        GPIO.output(self.motor_left_pins[1], GPIO.HIGH)
        GPIO.output(self.motor_right_pins[0], GPIO.HIGH)
        GPIO.output(self.motor_right_pins[1], GPIO.LOW)

    def turn_right(self):
        GPIO.output(self.motor_left_pins[0], GPIO.HIGH)
        GPIO.output(self.motor_left_pins[1], GPIO.LOW)
        GPIO.output(self.motor_right_pins[0], GPIO.LOW)
        GPIO.output(self.motor_right_pins[1], GPIO.HIGH)

    def cleanup(self):
        GPIO.cleanup()
