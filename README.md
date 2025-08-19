# Temporal Empathy Vision System

A **real-time AI system** that detects emotions, body poses, and voice sentiment using your **built-in webcam and microphone**. Designed to run smoothly on **Mac M1/M2**, **Windows**, and Linux systems.

---

## 🔹 Features

- **Facial Emotion Detection**: Detect micro-expressions in real-time using DeepFace.
- **Body Pose Analysis**: Track gestures and body posture with MediaPipe.
- **Voice Sentiment Analysis**: Capture audio and detect excitement or calmness.
- **Emotional Dashboard**: Visualize the overall emotional state with a live dashboard.
- **Cross-Platform**: Works on Mac (with `tensorflow-metal` for GPU), Windows, and Linux.

---

## 🛠️ Folder Structure
temporal_empathy/
│
├─ temporal_empathy/      # Python source files
│   ├─ main.py
│   ├─ emotion_detector.py
│   ├─ pose_detector.py
│   ├─ voice_analyzer.py
│   └─ dashboard.py
├─ requirements.txt       # Dependencies
├─ README.md
└─ venv/                  # Virtual environment (ignored in Git


---

## ⚡ Requirements

Install Python 3.11 or later.  

**Dependencies (cross-platform):**
opencv-python
mediapipe
deepface
numpy
pyttsx3
sounddevice
librosa
matplotlib
scipy
torch
tensorflow


> For Mac M1/M2, replace `tensorflow` with:
>
> tensorflow-macos
tensorflow-metal
>
> ---

## 🚀 Installation

1. Clone the repository:

```bash
git clone https://github.com/rohitmannur007/temporal_empathy.git
cd temporal_empathy

	2.	Create and activate a virtual environment:
python3.11 -m venv venv
source venv/bin/activate   # Mac/Linux
# .\venv\Scripts\activate  # Windows


	3.	Upgrade pip and install dependencies:
pip install --upgrade pip
pip install -r requirements.txt

🎬 How to Run
source venv/bin/activate   # Mac/Linux
# .\venv\Scripts\activate  # Windows

python temporal_empathy/main.py

	•	The webcam opens and detects facial emotions and body poses.
	•	Microphone analyzes voice sentiment every 3 seconds.
	•	Emotional dashboard shows a real-time map of all detected emotions.
	•	Press ESC to exit.

⸻

💡 Future Enhancements
	•	Multi-person tracking
	•	Gesture-based AI suggestions
	•	Integration with AR/VR for immersive emotional interaction
	•	Logging and analytics for emotion trends over time

⸻

📝 License

MIT License © 2025 Rohit Mannur

⸻

🔗 Contact
	•	GitHub: rohitmannur007

	•	The webcam opens and detects facial emotions and body poses.
	•	Microphone analyzes voice sentiment every 3 seconds.
	•	Emotional dashboard shows a real-time map of all detected emotions.
	•	Press ESC to exit.

⸻

💡 Future Enhancements
	•	Multi-person tracking
	•	Gesture-based AI suggestions
	•	Integration with AR/VR for immersive emotional interaction
	•	Logging and analytics for emotion trends over time

⸻

📝 License

MIT License © 2025 Rohit Mannur

⸻

🔗 Contact
	•	GitHub: rohitmannur007

	•	The webcam opens and detects facial emotions and body poses.
	•	Microphone analyzes voice sentiment every 3 seconds.
	•	Emotional dashboard shows a real-time map of all detected emotions.
	•	Press ESC to exit.

⸻

💡 Future Enhancements
	•	Multi-person tracking
	•	Gesture-based AI suggestions
	•	Integration with AR/VR for immersive emotional interaction
	•	Logging and analytics for emotion trends over time

⸻

📝 License

MIT License © 2025 Rohit Mannur

⸻

🔗 Contact
	•	GitHub: rohitmannur007
---

