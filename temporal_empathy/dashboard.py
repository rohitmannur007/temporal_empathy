import cv2

def show_emotional_map(frame, emotion_list):
    emotions = ['happy','sad','angry','surprise','fear','disgust','neutral','Excited','Calm','Unknown']
    counts = {e:0 for e in emotions}
    for e in emotion_list:
        if e in counts:
            counts[e] += 1

    h, w, _ = frame.shape
    bar_w = int(w / len(emotions))
    for idx, e in enumerate(emotions):
        cv2.rectangle(frame, (idx*bar_w, h-50), ((idx+1)*bar_w, h-50-counts[e]*10), (0,255,0), -1)
        cv2.putText(frame, e, (idx*bar_w+5, h-5), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (255,255,255), 1)
    return frame