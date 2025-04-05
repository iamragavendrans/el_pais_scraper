import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from model.article import Article
from util.logger import get_logger
from util.popup_handler import handle_cookie_wall, force_hide_cookie_wall

logger = get_logger()


class ArticleFetcher:
    @staticmethod
    def fetch_articles(driver):
        articles = []
        retries = 3
        clicked = False

        handle_cookie_wall(driver)
        force_hide_cookie_wall(driver)

        try:
            menu_btn = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Open menu'], .hamburger, .menu-toggle")
            if menu_btn.is_displayed():
                driver.execute_script("arguments[0].click();", menu_btn)
                logger.info("Mobile nav menu opened.")
                time.sleep(1)
        except NoSuchElementException:
            logger.info("No mobile menu toggle found or already visible.")

        try:
            for attempt in range(retries):
                try:
                    logger.info(f"Attempt {attempt + 1}: Locating and clicking 'Opinión' link")
                    opinion_link = WebDriverWait(driver, 10).until(
                        ec.presence_of_element_located((
                            By.XPATH, "//a[contains(text(),'Opinión') or contains(text(),'Opinion')]"
                        ))
                    )

                    driver.execute_script("""
                        const link = arguments[0];
                        link.scrollIntoView({block: 'center', behavior: 'instant'});
                        const rect = link.getBoundingClientRect();
                        const isVisible = (
                            rect.top >= 0 &&
                            rect.left >= 0 &&
                            rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
                            rect.right <= (window.innerWidth || document.documentElement.clientWidth)
                        );
                        if (isVisible) {
                            link.click();
                        } else {
                            throw new Error('Element not fully visible for click');
                        }
                    """, opinion_link)

                    logger.info("Successfully clicked 'Opinión' via JavaScript.")
                    clicked = True
                    break

                except Exception as e:
                    logger.warning(f"Attempt {attempt + 1} failed: {e}")
                    time.sleep(1)

            if not clicked:
                driver.save_screenshot(f"screenshot_opinion_click_fail_{int(time.time())}.png")
                raise Exception("Failed to click 'Opinión' link after retries.")

        except Exception as final_error:
            logger.error(f"Fatal error clicking 'Opinión' link: {final_error}")
            raise

        elements = driver.find_elements(By.CSS_SELECTOR, "article")[:5]
        if not elements:
            raise AssertionError("No articles found in the Opinion section")

        for i, element in enumerate(elements, start=1):
            try:
                title = element.find_element(By.CSS_SELECTOR, "h2, h3").text.strip()
                content = element.text.strip()
                image = element.find_element(By.TAG_NAME, "img").get_attribute("src") if element.find_elements(
                    By.TAG_NAME, "img") else "N/A"
                articles.append(Article(i, title, content, image))
            except NoSuchElementException:
                logger.warning(f"[Warning] Skipping article {i}: Missing elements")

        return articles
