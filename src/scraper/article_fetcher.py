import time

from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from model.article import Article
from util.logger import get_logger

logger = get_logger()


class ArticleFetcher:
    @staticmethod
    def fetch_articles(driver):
        articles = []
        retries = 3

        try:
            opinion_link = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//a[contains(text(),'Opinión') or contains(text(),'Opinion')]"))
            )
            driver.execute_script("arguments[0].scrollIntoView(true);", opinion_link)
            time.sleep(1)

            for attempt in range(retries):
                try:
                    ActionChains(driver).move_to_element(opinion_link).click().perform()
                    logger.info("Opinión link clicked successfully.")
                    break
                except StaleElementReferenceException:
                    if attempt < retries - 1:
                        logger.warning(f"Attempt {attempt + 1} failed: StaleElementReferenceException. Retrying...")
                        opinion_link = WebDriverWait(driver, 10).until(
                            EC.presence_of_element_located(
                                (By.XPATH, "//a[contains(text(),'Opinión') or contains(text(),'Opinion')]"))
                        )
                    else:
                        logger.error("Failed to click 'Opinión' link after retries.")
                        raise
                except Exception as e:
                    logger.warning(f"Click failed due to: {e}. Trying JavaScript click.")
                    driver.execute_script("arguments[0].click();", opinion_link)
                    break

        except (NoSuchElementException, TimeoutException) as e:
            logger.error(f"Failed to find or click the 'Opinión' link: {e}")

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
