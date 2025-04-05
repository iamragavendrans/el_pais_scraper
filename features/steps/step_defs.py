from behave import given, when, then
from selenium.common import ElementNotVisibleException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from api.translator import Translator
from cookie_handler import handle_popups
from scraper.article_fetcher import ArticleFetcher
from util.language_verifier import LanguageVerifier
from util.logger import get_logger
from util.popup_handler import handle_cookie_wall, force_hide_cookie_wall
from util.print_helper import PrintHelper
from util.text_analyzer import TextAnalyzer

articles = []
translated_titles = []
logger = get_logger()


@given("I launch the El Pais website")
def step_launch_el_pais(context):
    context.driver.get("https://elpais.com")
    handle_cookie_wall(context.driver)
    force_hide_cookie_wall(context.driver)
    handle_popups(context.driver)

    try:
        WebDriverWait(context.driver, 10).until(ec.presence_of_element_located((By.CSS_SELECTOR, "header")))
        logger.info("El Pais homepage loaded.")
    except ElementNotVisibleException:
        logger.warning("Warning: Header not found, page may not have loaded completely.")


@given("I verify the El Pais website is in Spanish")
def step_verify_language_is_spanish(context):
    assert LanguageVerifier.verify_spanish(context), "El Pais site is not in Spanish"


@when("I navigate to the Opinion section and fetch 5 articles")
def step_fetch_opinion_articles(context):
    global articles
    articles = ArticleFetcher.fetch_articles(context.driver)
    PrintHelper.print_articles(articles, logger)


@when("I translate article titles")
def step_translate_article_titles(context):
    global translated_titles
    translated_titles = Translator.translate_titles(articles)
    PrintHelper.print_translations(translated_titles, logger)


@then("I analyze repeated words in translated titles")
def step_analyze_translated_title_words(context):
    repeated = TextAnalyzer.analyze_repeated_words(translated_titles)
    PrintHelper.print_repeated_words(repeated, logger)
