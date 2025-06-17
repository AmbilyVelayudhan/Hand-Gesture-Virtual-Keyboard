import streamlit as st
import cv2
import numpy as np
import time
from gesture_module import HandDetector
from virtual_keyboard import draw_keyboard, get_pressed_key
import pyautogui

st.title("🖐️ Hand Gesture Name Input & Virtual Keyboard")
run = st.checkbox("Start Camera")

FRAME_WINDOW = st.image([])
detector = HandDetector()


typed_text = ""


last_key = None
last_time = 0
debounce_delay = 0.7  

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

while run:
    success, frame = cap.read()
    if not success:
        st.warning("Camera not available.")
        break

    frame = cv2.flip(frame, 1)
    hands = detector.findHands(frame)
    draw_keyboard(frame)

    key = None
    if hands:
        hand = hands[0]
        index_finger = hand[8]
        x, y = index_finger
        cv2.circle(frame, (x, y), 15, (255, 0, 255), cv2.FILLED)

        key = get_pressed_key(x, y)
        if key:
            current_time = time.time()
            if key != last_key or (current_time - last_time) > debounce_delay:
                if key == "Space":
                    typed_text += " "
                elif key == "Backspace":
                    typed_text = typed_text[:-1]
                elif key == "Enter":
                    typed_text += "\n"
                else:
                    typed_text += key

                last_key = key
                last_time = current_time

    
    y_offset = 100
    for i, line in enumerate(typed_text.splitlines()[-5:]):  
        cv2.putText(frame, line, (20, y_offset + i * 40), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 3)

    FRAME_WINDOW.image(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

cap.release()
