from cvzone.HandTrackingModule import HandDetector
import cv2
import mediapipe as mp

class HandDetector:
    def __init__(self, detectionCon=0.5, maxHands=2):
        # Initialize the HandDetector with parameters
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            min_detection_confidence=detectionCon,  # Set the minimum detection confidence
            max_num_hands=maxHands  # Set the maximum number of hands to detect
        )
        self.mp_draw = mp.solutions.drawing_utils

    def findHands(self, frame, draw=True):
        # Convert the image color
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(frame_rgb)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                if draw:
                    self.mp_draw.draw_landmarks(frame, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)

        return results


import mediapipe as mp

def initialize_detector():
    mp_hands = mp.solutions.hands
    hands_detector = mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)
    return hands_detector, mp_hands

def is_hand_raised(results, frame_height):
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Assuming the first landmark (wrist) is a good indicator of hand position
            wrist_y = hand_landmarks.landmark[0].y * frame_height
            # Check if the wrist is raised beyond a threshold
            if wrist_y < frame_height * 0.3:  # Customize this threshold as needed
                return True
    return False

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

def process_hand_landmarks(image, hands_detector):
    image_rgb = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
    results = hands_detector.process(image_rgb)
    image_bgr = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2BGR)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                image_bgr,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )

    return image_bgr