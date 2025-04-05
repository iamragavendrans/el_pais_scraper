class TranslateRequest:
    def __init__(self, text, source_lang="es", target_lang="en"):
        self.text = text
        self.source_lang = source_lang
        self.target_lang = target_lang