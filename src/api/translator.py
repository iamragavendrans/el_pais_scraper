import os
import requests
import time
from api.translate_response import TranslateResponse
from util.logger import get_logger

logger = get_logger()


class Translator:
    API_KEY = os.getenv("RAPIDAPI_KEY")
    HOST = "google-translate113.p.rapidapi.com"
    ENDPOINT = "https://google-translate113.p.rapidapi.com/api/v1/translator/text"

    MAX_RETRIES = 3
    RETRY_DELAY = 5

    @staticmethod
    def translate_titles(articles):
        headers = {
            "Content-Type": "application/json",
            "x-rapidapi-key": Translator.API_KEY,
            "x-rapidapi-host": Translator.HOST
        }

        translated = []

        for article in articles:
            if not article.title:
                continue

            json_payload = {
                "from": "es",
                "to": "en",
                "text": article.title
            }

            for attempt in range(Translator.MAX_RETRIES):
                try:
                    response = requests.post(
                        Translator.ENDPOINT,
                        json=json_payload,
                        headers=headers
                    )

                    if response.status_code == 200:
                        result = response.json().get("trans", "")
                        translated.append(TranslateResponse(article.title, result))
                        break
                    elif response.status_code == 429:
                        logger.warning(
                            f"Rate limit exceeded. Retrying article {article.index} after {Translator.RETRY_DELAY}s...")
                        time.sleep(Translator.RETRY_DELAY)
                    else:
                        logger.warning(f"Translation failed for article {article.index}: Status {response.status_code}")
                        translated.append(
                            TranslateResponse(article.title, f"[Translation Failed: {response.status_code}]"))
                        break
                except Exception as e:
                    logger.warning(f"Exception translating article {article.index}: {e}")
                    translated.append(TranslateResponse(article.title, "[Translation Exception]"))
                    break

        return translated
