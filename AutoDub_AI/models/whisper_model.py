import whisper
import os

model = whisper.load_model("base")

def transcribe_with_timestamps(audio_path):
    if not os.path.exists(audio_path):
        raise FileNotFoundError(f"Audio asset missing at path: {audio_path}")
        
    print("[Whisper Core] Starting high-fidelity audio transcription...")
    result = model.transcribe(audio_path)
    
    segments = []
    for seg in result["segments"]:
        segments.append({
            "start": seg["start"],
            "end": seg["end"],
            "text": seg["text"].strip()
        })
    return segments