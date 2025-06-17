# Hand-Gesture-Virtual-Keyboard

🖐️ Hand Gesture Controlled Virtual Keyboard 

📝 Project Overview

This project implements a virtual keyboard that is controlled using hand gestures via webcam. It uses MediaPipe to detect hand landmarks and allows users to type characters by hovering their index finger over virtual keys.

Built with:

* OpenCV for video processing

* MediaPipe for hand tracking

* Streamlit for a clean and easy-to-use interface

* PyAutoGUI to simulate key presses

* Real-time name input display on screen

✨ Features

🖐️ Hand gesture detection via webcam

- ⌨️ Virtual keyboard interface drawn directly on video

- 💬 Real-time display of typed name/text

- 🔡 Supports alphabets, space, backspace, and enter

- 💻 Streamlit app for user interface (click "Start Camera" to begin)

- 🛡️ Debounce system to avoid rapid unintended key presses


💡 How it Works

* MediaPipe tracks 21 hand landmarks.

* We extract the position of the index finger tip (landmark[8]).

* If the finger is inside a key box, that key is considered pressed.

* A debounce timer prevents accidental multiple presses.

* Pressed characters are displayed live on the video stream.


📥 Requirements.txt

opencv-python
mediapipe
streamlit
numpy
pyautogui


📂 Project Structure

hand-gesture-keyboard/
│
├── app.py              
├── gesture_module.py     
├── virtual_keyboard.py  
├── requirements.txt      
└── README.md    

✅ Controls

 Gesture        Action                 
 ------------ | ---------------------- 
 Hover on A-Z | Types that character   
 Space key    | Adds a space           
 Backspace    | Deletes last character 
 Enter        | Inserts a line break   


🛠️ Installation

📦 Requirements

* Python 3.8 or higher

* Webcam-enabled device
  

🔧 Setup

1. Clone the repo
git clone https://github.com/yourusername/hand-gesture-keyboard.git
cd hand-gesture-keyboard

2. Create a virtual environment
python -m venv .venv
source .venv/bin/activate  or .venv\Scripts\activate on Windows

3. Install dependencies
pip install -r requirements.txt

🚀 Running the App

streamlit run app.py


