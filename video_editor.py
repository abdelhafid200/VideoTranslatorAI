
import pysrt

def create_srt(segments, translations, srt_file):
    """Create an SRT file from transcribed + translated segments."""
    subs = pysrt.SubRipFile()
    for i, (seg, trans) in enumerate(zip(segments, translations), 1):
        start = seg["start"]
        end = seg["end"]

        start_s = pysrt.SubRipTime(seconds=int(start),
                                   milliseconds=int((start % 1) * 1000))
        end_s = pysrt.SubRipTime(seconds=int(end),
                                 milliseconds=int((end % 1) * 1000))

        subs.append(
            pysrt.SubRipItem(index=i, start=start_s, end=end_s, text=trans)
        )
    subs.save(srt_file, encoding="utf-8")
    print(f"[INFO] SRT file saved: {srt_file}")


