from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from util.logger import get_logger

logger = get_logger()

def handle_cookie_wall(driver):
    try:
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((
                By.CSS_SELECTOR, "div[role='dialog'] button, div[class*='cookie'] button"
            ))
        )
        buttons = driver.find_elements(By.CSS_SELECTOR, "div[role='dialog'] button, div[class*='cookie'] button")
        for btn in buttons:
            try:
                btn_text = btn.text.strip().lower()
                if "accept" in btn_text or "continuar" in btn_text or "aceptar" in btn_text:
                    driver.execute_script("arguments[0].click();", btn)
                    logger.info(f"Clicked cookie modal button: {btn_text}")
                    return
            except Exception as e:
                logger.warning(f"Cookie button click failed: {e}")
    except TimeoutException:
        logger.info("No cookie modal detected.")

def force_hide_cookie_wall(driver):
    try:
        js = """
        let modals = document.querySelectorAll("div[role='dialog'], div[class*='cookie']");
        modals.forEach(m => m.remove());
        """
        driver.execute_script(js)
        logger.info("Cookie modal forcibly removed via JavaScript.")
    except Exception as e:
        logger.warning(f"Failed to force-hide cookie modal: {e}")
