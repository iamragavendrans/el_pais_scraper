from tabulate import tabulate
from util.image_downloader import ImageDownloader
import os

class PrintHelper:
    @staticmethod
    def print_articles(articles, logger):
        logger.info("\nOpinion Articles (Top 5)")
        table = []
        for a in articles:
            if a.image != "N/A":
                filename = f"article_{a.index}.jpg"
                path = ImageDownloader.download(a.image, filename, save_dir="src/output/image")
                display_name = f"[link]({os.path.relpath(path)})" if path else "image_not_available"
            else:
                display_name = "N/A"
            table.append([a.index, a.title, display_name, a.content[:60]])
        logger.info("\n" + tabulate(table, headers=["#", "Title", "Image", "Content"], tablefmt="fancy_grid", stralign="left"))

    @staticmethod
    def print_translations(translated, logger):
        logger.info("\nTranslated Titles")
        table = [[idx + 1, t.original, t.translated] for idx, t in enumerate(translated)]
        logger.info("\n" + tabulate(table, headers=["#", "Original", "Translated"], tablefmt="fancy_grid", stralign="left"))

    @staticmethod
    def print_repeated_words(counter, logger):
        logger.info("\nRepeated Words (Count > 2)")
        table = [[word, count] for word, count in counter.items()]
        logger.info("\n" + tabulate(table, headers=["Word", "Count"], tablefmt="fancy_grid", stralign="left"))
