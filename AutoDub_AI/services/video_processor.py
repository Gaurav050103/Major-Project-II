from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.audio.AudioClip import CompositeAudioClip
import os

def process_and_stitch(video_path, audio_chunks, output_path):
    print("[Stitch Engine] Resolving timelines and compiling layout streams...")
    video_clip = VideoFileClip(video_path)
    
    mixed_audios = []
    
    if video_clip.audio is not None:
        original_audio = video_clip.audio.with_volume_scaled(0.15)
        mixed_audios.append(original_audio)
    
    for chunk in audio_chunks:
        if not os.path.exists(chunk["audio_path"]):
            continue
            
        audio_clip = AudioFileClip(chunk["audio_path"])
        ideal_duration = chunk["end"] - chunk["start"]
        if audio_clip.duration > ideal_duration:
            audio_clip = audio_clip.subclipped(0, ideal_duration)
            
        positioned_audio = audio_clip.with_start(chunk["start"])
        mixed_audios.append(positioned_audio)
    
    final_audio = CompositeAudioClip(mixed_audios)
    final_audio.duration = video_clip.duration
    final_video = video_clip.with_audio(final_audio)
    
    final_video.write_videofile(
        output_path, 
        codec="libx264", 
        audio_codec="aac",
        audio=True,
        fps=video_clip.fps,
        logger=None
    )
    
    video_clip.close()
    final_video.close()
    print("[Stitch Engine] Task complete.")