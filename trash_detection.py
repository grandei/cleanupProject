import tensorflow as tf
import cv2

class TrashDetection:
    def __init__(self, model_path):
        self.interpreter = tf.lite.Interpreter(model_path=model_path)
        self.interpreter.allocate_tensors()
        self.input_details = self.interpreter.get_input_details()
        self.output_details = self.interpreter.get_output_details()
        self.camera = cv2.VideoCapture(0)  # Initialize camera

    def detect_trash(self):
        ret, frame = self.camera.read()
        if not ret:
            return False

        # Preprocess image
        resized_frame = cv2.resize(frame, (224, 224))
        input_data = resized_frame.astype('float32') / 255.0
        input_data = input_data.reshape((1, 224, 224, 3))

        # Run inference
        self.interpreter.set_tensor(self.input_details[0]['index'], input_data)
        self.interpreter.invoke()
        output_data = self.interpreter.get_tensor(self.output_details[0]['index'])

        # Assume output is a binary classification (trash vs non-trash)
        return output_data[0][0] > 0.5
