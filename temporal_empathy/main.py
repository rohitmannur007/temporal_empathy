import cv2
from emotion_detector import detect_emotion
from pose_detector import PoseDetector
from voice_analyzer import record_audio, analyze_voice
from hand_gesture import HandGesture
from dashboard import show_emotional_map
import pyttsx3
import time

pose_detector = PoseDetector()
hand_detector = HandGesture()
emotion_history = []

engine = pyttsx3.init()
gesture_responses = {
    "One": "Hello!",
    "Two": "Hi Priyanka!",
    "Three": "Hiii Priyanka!"
}

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Facial emotion
    face_emotion = detect_emotion(frame)

    # Pose emotion
    pose_emotion = pose_detector.detect_pose(frame)

    # Voice emotion every 3 seconds
    if int(time.time()) % 3 == 0:
        audio = record_audio(duration=1)
        voice_emotion = analyze_voice(audio)
    else:
        voice_emotion = "Neutral"

    # Hand gesture detection
    gesture = hand_detector.detect_gesture(frame)
    if gesture in gesture_responses:
        engine.say(gesture_responses[gesture])
        engine.runAndWait()

    current_emotions = [face_emotion, pose_emotion, voice_emotion]
    emotion_history.extend(current_emotions)
    if len(emotion_history) > 50:
        emotion_history = emotion_history[-50:]

    # Show dashboard
    frame = show_emotional_map(frame, emotion_history)
    cv2.putText(frame, f"Gesture: {gesture}", (10,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

    cv2.imshow("Temporal Empathy + Gesture AI", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC
        break

cap.release()
cv2.destroyAllWindows()