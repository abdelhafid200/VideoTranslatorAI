import ffmpeg

def extract_audio(video_path, audio_path):
    """Extract audio from video using ffmpeg."""
    (
        ffmpeg
        .input(video_path)
        .output(audio_path, ac=1, ar="16k")
        .overwrite_output()
        .run()
    )
    print(f"[INFO] Audio extracted to {audio_path}")
