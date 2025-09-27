# main.py (snippet)

from audio_extractor import extract_audio
from subtitle_generator import burn_subtitles
from transcriber import transcribe_audio
from translator import translate_texts
from video_editor import create_srt



INPUT_VIDEO = './Videos.mp4'
AUDIO_FILE = "audio.wav"
SRT_FILE = "subtitles.srt"
OUTPUT_VIDEO = "output.mp4"

SRC_LANG = "en"   
TRANSLATION_LANG = "ar"  
WHISPER_MODEL = "small"

if __name__ == "__main__":
    # Step 1: Extract audio
    extract_audio(INPUT_VIDEO, AUDIO_FILE)

    # Step 2: Transcribe
    segments = transcribe_audio(AUDIO_FILE, WHISPER_MODEL)

    # Step 3: Translate
    texts = [seg["text"] for seg in segments]
    translations = translate_texts(texts, SRC_LANG, TRANSLATION_LANG)

    # Step 4: Generate SRT
    create_srt(segments, translations, SRT_FILE)

    # Step 5: Burn subtitles
    burn_subtitles(INPUT_VIDEO, SRT_FILE, OUTPUT_VIDEO)
