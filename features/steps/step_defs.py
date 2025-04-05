from behave import given, then
from selenium.webdriver.common.by import By
import time


@given("I launch the El Pais website")
def step_launch_site(context):
    context.driver.get("https://elpais.com")
    time.sleep(3)  # Allow time for full page load (can be replaced by WebDriverWait)

@given("I verify the El Pais website is in Spanish")
def step_verify_language(context):
    html_lang = context.driver.find_element(By.TAG_NAME, "html").get_attribute("lang")
    print(f"[Debug] HTML lang attribute: {html_lang}")
    assert "es" in html_lang.lower(), f"Expected 'es' in lang attribute, but got: {html_lang}"