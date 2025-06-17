import cv2
import mediapipe as mp

class HandDetector:
    def __init__(self, maxHands=1):
        self.handsModule = mp.solutions.hands
        self.hands = self.handsModule.Hands(max_num_hands=maxHands)
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, img):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        hands = []
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                lmList = []
                for id, lm in enumerate(handLms.landmark):
                    h, w, c = img.shape
                    lmList.append((int(lm.x * w), int(lm.y * h)))
                hands.append(lmList)
                self.mpDraw.draw_landmarks(img, handLms, self.handsModule.HAND_CONNECTIONS)
        return hands
