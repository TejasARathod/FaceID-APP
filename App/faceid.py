# Import kivy dependencies first
from asyncio.log import logger
import imp
from turtle import color
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

# import kivy UX components
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.label import Label

from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.logger import Logger

# Import other dependencies
import cv2
import tensorflow as tf
from torch import layout
from layers import L1Dist
import os
import numpy as np

# Build App and Layout
class CamApp(App):

    def build(self):
        # Main Layout components
        self.web_cam = Image(size_hint=(1,.8))
        self.button = Button(text="Verify",on_press=self.verify, size_hint=(1,.1))
        self.verification_label = Label(text="Verification Uninitiated", size_hint=(1,.1))

        # Add items to layout
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(self.web_cam)
        layout.add_widget(self.button)
        layout.add_widget(self.verification_label)

        # Load tensorflow/keras model
        self.model = tf.keras.models.load_model('siamesemodel.h5', custom_objects={'L1Dist':L1Dist})

        # Setup video capture devices
        self.capture = cv2.VideoCapture(0)
        Clock.schedule_interval(self.update, 1.0/33.0)

        return layout

    # Run continously to get webcam feed
    def update(self, *args):
        
        # read frame from opencv
        ret, frame = self.capture.read()
        frame = frame[120:120+250, 200:200+250, :]

        # Flip horizontal and convert image to texture 
        buf = cv2.flip(frame, 0).tostring()
        img_texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
        img_texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
        self.web_cam.texture = img_texture

    # Load img from file and convert to 100x100px
    def preprocess(self, file_path):

        # read in img from file path
        byte_img = tf.io.read_file(file_path)
        # load in the img
        img = tf.io.decode_jpeg(byte_img)
        # Preprocessing steps - resizing the img to 100x100
        img = tf.image.resize(img, (100,100))
        # scale image between 1 & 0
        img = img/255.0
        return img

    # Verification function
    def verify(self, *args):
        verification_threshold = 0.7
        detection_threshold = 0.7

        # Capture input image from our webcam
        SAVE_PATH = os.path.join('application_data', 'input_image', 'input_image.jpg')
        ret, frame = self.capture.read()
        frame = frame[120:120+250, 200:200+250, :]
        cv2.imwrite(SAVE_PATH, frame)

        # Build results array
        results = []
        for image in os.listdir(os.path.join('application_data', 'verification_images')):
            input_img = self.preprocess(os.path.join('application_data', 'input_image', 'input_image.jpg'))
            validation_img = self.preprocess(os.path.join('application_data', 'verification_images', image))
            
            # Make Predictions
            result = self.model.predict(list(np.expand_dims([input_img, validation_img], axis=1)))
            results.append(result)

        # Detection Threshold: Metric above which a prediction is considered positive
        detection = np.sum(np.array(results) > detection_threshold)
        
        # Verification Threshold: Proportion os positive predictions / total positive samples
        verification = detection / len(os.listdir(os.path.join('application_data', 'verification_images')))
        verified = verification > verification_threshold

        # Set verification text
        self.verification_label.text = 'Verified' if verified == True else 'Unverified'

        # Log out details 
        Logger.info(results)
        Logger.info(np.sum(np.array(results)>0.2))
        Logger.info(np.sum(np.array(results)>0.4))
        Logger.info(np.sum(np.array(results)>0.6))
        Logger.info(np.sum(np.array(results)>0.8))

        Logger.info(results)
        Logger.info(detection)
        Logger.info(verification)
        Logger.info(verified)

  
        
        if verified == True:
            print(verification)
        else:
            print(verification)

        
        return results, verified



if __name__ == '__main__':
    CamApp().run()