import sounddevice as sd
import numpy as np
import librosa

def record_audio(duration=1, fs=22050):
    audio = sd.rec(int(duration*fs), samplerate=fs, channels=1)
    sd.wait()
    return np.squeeze(audio)

def analyze_voice(audio, fs=22050):
    try:
        rms = np.mean(librosa.feature.rms(y=audio))
        if rms > 0.03:
            return "Excited"
        else:
            return "Calm"
    except:
        return "Neutral"