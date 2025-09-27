import ffmpeg

def burn_subtitles(video_path, srt_file, output_path):
    """Burn subtitles into video with ffmpeg."""
    (
        ffmpeg
        .input(video_path)
        .output(output_path, vf=f"subtitles={srt_file}:force_style='FontName=Noto Sans Arabic'")
        .overwrite_output()
        .run()
    )
    print(f"[INFO] Video with subtitles saved: {output_path}")
