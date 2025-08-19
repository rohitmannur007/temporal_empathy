import cv2
import mediapipe as mp

mp_pose = mp.solutions.pose

class PoseDetector:
    def __init__(self):
        self.pose = mp_pose.Pose()
        self.mp_draw = mp.solutions.drawing_utils

    def detect_pose(self, frame):
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.pose.process(frame_rgb)
        pose_status = "Neutral"

        if results.pose_landmarks:
            self.mp_draw.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
            left_wrist = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST]
            right_wrist = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST]
            if left_wrist.y < 0.3 and right_wrist.y < 0.3:
                pose_status = "Excited"
        return pose_status