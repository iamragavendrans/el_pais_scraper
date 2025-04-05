from collections import Counter


class TextAnalyzer:
    @staticmethod
    def analyze_repeated_words(translated_titles):
        all_words = " ".join([item.translated for item in translated_titles]).lower().split()
        return {word: count for word, count in Counter(all_words).items() if count > 2}
