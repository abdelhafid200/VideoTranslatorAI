Sure! Here’s a **complete README template** for your GitHub repo that explains what the project is, its requirements, and how to run it:

---

# VideoTranslatorAI

**Automatically translate videos into multiple languages with AI-powered subtitles.**
Extract audio, transcribe speech with Whisper, translate with Hugging Face models, generate subtitles, and optionally burn them into the video. Supports long videos, Turkish, English, French, Arabic, and more.

---

## Features

* Extract audio from any video (`.mp4`, `.mkv`, etc.)
* Transcribe speech using **OpenAI Whisper**
* Translate speech to multiple languages (Arabic, French, etc.) using Hugging Face models
* Generate `.srt` subtitle files
* Burn subtitles into videos with ffmpeg
* Supports long videos (1–2 hours)

---

## Requirements

* Python 3.10+
* [ffmpeg](https://ffmpeg.org/download.html) installed and added to PATH
* Python packages:

  ```
  ffmpeg-python
  openai-whisper
  transformers
  torch
  pysrt
  ```

You can install them using:

```bash
pip install -r requirements.txt
```

---

## Project Structure

```
video_translator/
│── main.py               # main pipeline script
│── audio_extractor.py    # extract audio from video
│── transcriber.py        # speech-to-text (Whisper)
│── translator.py         # translate text (HF/Google)
│── subtitle_generator.py # create .srt file
│── video_editor.py       # burn subtitles into video
│── requirements.txt      # dependencies
```

---

## Usage

1. **Place your video** in the project folder.
2. Update the config in `main.py`:

```python
INPUT_VIDEO = "your_video.mp4"
SRC_LANG = "en"           # Source language (detected by Whisper)
TRANSLATION_LANG = "ar"   # Target language (ar = Arabic, fr = French)
WHISPER_MODEL = "small"   # Whisper model size: tiny, small, medium, large
```

3. **Run the pipeline**:

```bash
python main.py
```

4. **Output**:

* `subtitles.srt` → translated subtitles file
* `output.mp4` → video with subtitles burned in

---

## Notes

* For Arabic subtitles, make sure **Noto Sans Arabic** or a similar font is installed.
* For very long videos, consider splitting audio into chunks to avoid memory issues.
* Whisper automatically detects spoken language, but you can force a source language if needed.

---

## Example

```python
INPUT_VIDEO = "english_video.mp4"
SRC_LANG = "en"
TRANSLATION_LANG = "ar"
WHISPER_MODEL = "small"
```

Result: A video with Arabic subtitles ready to watch or share.


