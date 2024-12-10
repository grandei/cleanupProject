import time
from motor_control import MotorControl
from obstacle_detection import ObstacleDetection
from trash_detection import TrashDetection

#Initialize
motor = MotorControl()
ultrasonic = ObstacleDetection(trigger_pin=18, echo_pin=24)  #replace with GPIO pins
trashDetector = TrashDetection(model_path="model.tflite")  #optional - TensorFlow Lite model

# Main loop
try:
    while True:
        distance = ultrasonic.get_distance()

        if distance < 20:  #detection of obstacle within 20 cm
            print(f"Obstacle detected at {distance} cm. Turning...")
            motor.stop()#stop before next movement
            motor.turn_left()  #adjust course and turn
            time.sleep(1)  #turn for 1 second
            motor.forward()#move again
        else:
            print("No obstacle. Moving forward.")
            motor.forward()

        #trash detection (might need adjusting)
        trash_detected = trashDetector.detect_trash()  #if trash is detected, return True
        if trash_detected: #if True then...
            print("Trash detected. Collecting...")
            motor.stop()
            #******************************** add collection logic here ********************************

        time.sleep(0.1)  # Loop delay
except KeyboardInterrupt:
    print("Shutting down.")
    motor.stop()
