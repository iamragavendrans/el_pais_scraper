from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from util.logger import get_logger

logger = get_logger()


def accept_cookies_if_present(driver):
    try:
        cookie_consent = WebDriverWait(driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, "//button[@id='didomi-notice-agree-button']"))
        )
        cookie_consent.click()
        logger.info("Cookie consent accepted.")
    except TimeoutException:
        logger.info("Cookie consent not shown.")


def accept_subscription_popup_if_present(driver):
    try:
        subscription_button = WebDriverWait(driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Accept')]"))
        )
        subscription_button.click()
        logger.info("Subscription popup dismissed.")
    except TimeoutException:
        logger.info("Subscription popup not shown, continuing test.")


def handle_popups(driver):
    accept_subscription_popup_if_present(driver)
    accept_cookies_if_present(driver)
