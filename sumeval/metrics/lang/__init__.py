def get_lang(lang=""):
    if lang == "ja":
        from .lang_ja import LangJA
        return LangJA()
    elif lang == "ru":
        from .lang_ru import LangRU
        return LangRU()
    else:
        from .lang_en import LangEN
        return LangEN()
