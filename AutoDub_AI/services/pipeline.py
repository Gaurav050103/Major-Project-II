import os
import uuid
import subprocess
from moviepy.video.io.VideoFileClip import VideoFileClip
from models.whisper_model import transcribe_with_timestamps
from models.translate import translate_segments
from models.tts import generate_voice_chunks
from services.video_processor import process_and_stitch

# Change the function definition line to accept voice parameters
def run_autodub_pipeline(video_path, target_lang="hi", voice_profile="female"):
    session_id = str(uuid.uuid4())[:8]
    session_dir = os.path.join("uploads", session_id)
    os.makedirs(session_dir, exist_ok=True)
    
    # Phase 1: Native Stream Isolation
    print(f"\n--- [Session {session_id}] Phase 1: Isolating Raw Audio Tracks ---")
    video = VideoFileClip(video_path)
    extracted_audio_path = os.path.join(session_dir, "source_audio.wav")
    video.audio.write_audiofile(extracted_audio_path, logger=None)
    video.close()
    
    # Phase 2: Structural Automatic Speech Recognition
    print(f"\n--- [Session {session_id}] Phase 2: Processing Whisper Timestamp Matrix ---")
    segments = transcribe_with_timestamps(extracted_audio_path)
    
    # Phase 3: Text Conversion Routing
    print(f"\n--- [Session {session_id}] Phase 3: Executing Machine Translation Layer ---")
    translated_segments = translate_segments(segments, target_lang)
    
    # Phase 4: Acoustic Synthesis (UPDATED TO RECEIVE LANG & PROFILE)
    print(f"\n--- [Session {session_id}] Phase 4: Constructing Speech Audio Fragments ---")
    audio_chunks = generate_voice_chunks(translated_segments, session_dir, target_lang, voice_profile)
    
    # Phase 4.5: Normalizing Audio Frequencies
    print(f"\n--- [Session {session_id}] Phase 4.5: Normalizing Audio Frequencies ---")
    for chunk in audio_chunks:
        mp3_path = chunk["audio_path"]
        wav_path = mp3_path.replace(".mp3", ".wav")
        
        cmd = f'ffmpeg -i "{mp3_path}" -ar 44100 -ac 2 "{wav_path}" -y'
        subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        chunk["audio_path"] = wav_path
    
    # Phase 5: Frame Level Composition
    print(f"\n--- [Session {session_id}] Phase 5: Reassembling Master Assets ---")
    output_filename = f"dubbed_{session_id}.mp4"
    final_output_path = os.path.join("outputs", output_filename)
    
    process_and_stitch(video_path, audio_chunks, final_output_path)
    
    return final_output_path, output_filename