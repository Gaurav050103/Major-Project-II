from gtts import gTTS
import os

def generate_voice_chunks(translated_segments, session_dir, target_lang="hi", voice_profile="female"):
    chunk_paths = []
    
    # Configure accent mappings based on selected voice profiles
    # Top Level Domain controls accent tone parameters within Google Text-To-Speech
    tld_modifier = "com"
    if voice_profile == "male":
        if target_lang == "hi":
            tld_modifier = "co.in" # Distinct pitch settings for Indian locales
        elif target_lang == "en":
            tld_modifier = "co.uk" # British male configuration mapping
        else:
            tld_modifier = "co.za" # Alternates voice profiles for standard locales
            
    for i, seg in enumerate(translated_segments):
        text = seg["text"]
        chunk_path = os.path.join(session_dir, f"chunk_{i}.mp3")
        
        # Build synthesis track utilizing target codes and selected accent domain
        tts = gTTS(text=text, lang=target_lang, tld=tld_modifier)
        tts.save(chunk_path)
        
        chunk_paths.append({
            "start": seg["start"],
            "end": seg["end"],
            "audio_path": chunk_path
        })
    return chunk_paths