import streamlit as st
import cv2
import numpy as np
from utils.hand_tracker import get_hand_landmarks
from utils.predictor import predict_gesture
from utils.alert import trigger_alert
from config.labels import GESTURE_LABELS
import sys
import os

st.title("🏥 Patient Gesture Alert System")

run = st.checkbox("Start Camera")

FRAME_WINDOW = st.image([])

camera = cv2.VideoCapture(0)

last_alert = None

while run:
    success, frame = camera.read()
    if not success:
        st.write("Camera not working")
        break

    data, frame = get_hand_landmarks(frame)

    if data:
        gesture = predict_gesture(data)
        message = GESTURE_LABELS.get(gesture, "Unknown")

        cv2.putText(frame, message, (50, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1,
                    (0, 0, 255), 3)

        # ALERT
        if message == "EMERGENCY" and last_alert != message:
            trigger_alert(message)
            last_alert = message

        st.success(f"Detected: {message}")

    # Convert to RGB for Streamlit
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    FRAME_WINDOW.image(frame)

camera.release()
