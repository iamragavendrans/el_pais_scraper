import time
from typing import Tuple

from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from util.logger import get_logger

logger = get_logger()


class SupportingUtilities:
    @staticmethod
    def safe_click_with_retry(driver, locator: Tuple[str, str], retries=3, wait_seconds=5):
        last_exception = None
        for attempt in range(1, retries + 1):
            try:
                WebDriverWait(driver, wait_seconds).until(ec.presence_of_element_located(locator))
                element = driver.find_element(*locator)
                driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
                WebDriverWait(driver, wait_seconds).until(ec.element_to_be_clickable(locator))

                try:
                    element.click()
                    logger.info(f"Clicked element via standard click on attempt {attempt}.")
                except ElementNotInteractableException:
                    driver.execute_script("arguments[0].click();", element)
                    logger.info(f"Clicked element via JS fallback on attempt {attempt}.")
                return
            except Exception as e:
                logger.warning(f"Click attempt {attempt} failed: {e}")
                last_exception = e
                time.sleep(1)

        logger.error(f"Failed to click element after {retries} attempts.")
        raise last_exception
