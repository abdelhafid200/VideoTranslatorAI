import whisper

def transcribe_audio(audio_path, model_name="small"):
    """Transcribe audio with Whisper."""
    model = whisper.load_model(model_name)
    result = model.transcribe(audio_path, task="transcribe")
    return result["segments"]  # list of dicts with text + timestamps