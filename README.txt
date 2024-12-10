***Boat Cleanup Project***

Obstacle Avoidance Tools
- RPi.GPIO: For working with sensors like bumpers or sensors
- pyserial: For communication with microcontrollers, if used. (might use, might not)

Motion Control Tools
- Adafruit_MotorKit: If using motors from Adafruit, this library simplifies motor control
- GPIO Zero: A beginner-friendly library for motor control, easy to work with DC motors, stepper motors, and servos. Includes built-in support for H-bridge motor drivers
- pymotors: General-purpose library for motor control. (unless you know what to use already)
- pigpio: A more advanced GPIO library for Raspberry Pi, useful for PWM signals to control motors

Autonomous Navigation Tools
- numpy and scipy: Useful for calculations related to navigation and path planning
- opencv-python: If you include a camera or object detection
- sensor: For working with sensors like ultrasonic or LiDAR

Data Collection and Analysis Tools
- pandas: For logging data, such as sensor readings or travel history
- matplotlib: For visualizing collected data or debugging navigation paths

Networking and Remote Monitoring
- socket or asyncio: For creating a communication system to monitor and control the boat remotely
- MQTT (using paho-mqtt): For IoT-based communication.

Environment-Specific Libraries
- pybluez: If using bluetooth for communication with devices.
- requests: For making HTTP requests, incase you use cloud integration.

AI and Automation (Optional)
- TensorFlow: Machine learning for better obstacle detection or navigation.
- scikit-learn: For lighter-weight machine learning models.
- YOLOv5 or YOLOv8: For trash detection using a camera.

***Workflow Example***

1. Obstacle Detection:
    - Use ultrasonic sensors connected via GPIO, controlled by RPi.GPIO or pigpio.
    - For detecting floating obstacles or trash, pair with simple logic for navigation adjustments.
2. Navigation Logic:
    - Calculate directions and movement paths using numpy and GPIO motor libraries.
3. Trash Collection:
    - Activate motors or servos using Adafruit_MotorKit to control a collection mechanism.
4. Data Logging:
    - Use pandas to record real-time data like detected distances, object types, and movements.
5. Monitoring:
    - Build a simple web dashboard using Flask or Dash to display data and control the boat remotely.
6. Object Identification (Optional):
    - Deploy TensorFlow Lite or OpenCV models to classify objects as sea life, plastic, or hard surfaces.
