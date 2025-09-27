from transformers import pipeline

def translate_texts(texts, src_lang="tr", tgt_lang="ar"):
    """
    Translate list of texts from src_lang -> tgt_lang.
    Default: Turkish -> Arabic.
    """
    model_name = f"Helsinki-NLP/opus-mt-{src_lang}-{tgt_lang}"
    translator = pipeline("translation", model=model_name)

    translations = []
    for t in texts:
        if t.strip():
            out = translator(t, max_length=512)[0]["translation_text"]
            translations.append(out)
        else:
            translations.append("")
    return translations