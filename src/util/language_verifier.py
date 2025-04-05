from selenium.common.exceptions import NoSuchElementException

class LanguageVerifier:
    @staticmethod
    def verify_spanish(context):
        try:
            lang = context.driver.find_element("tag name", "html").get_attribute("lang")
            return lang and "es" in lang.lower()
        except NoSuchElementException:
            return False