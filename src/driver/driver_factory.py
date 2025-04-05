import os
import json
from selenium import webdriver
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver

def create_driver():
    run_env = os.getenv("RUN_ENV", "local").lower()
    browser_config = os.getenv("BROWSER_CONFIG", "win11_chrome")

    if run_env == "browserstack":
        config_path = "features/browserstack_config/capabilities_config.json"
        with open(config_path) as f:
            caps = json.load(f)

        if browser_config not in caps:
            raise Exception(f"BROWSER_CONFIG '{browser_config}' not found in capabilities_config.json")

        desired_caps = caps[browser_config]
        username = os.getenv("BROWSERSTACK_USERNAME")
        access_key = os.getenv("BROWSERSTACK_ACCESS_KEY")

        if not username or not access_key:
            raise Exception("Set BROWSERSTACK_USERNAME and BROWSERSTACK_ACCESS_KEY in .env")

        bs_url = f"https://{username}:{access_key}@hub-cloud.browserstack.com/wd/hub"


        options = ChromeOptions()
        for key, value in desired_caps.items():
            options.set_capability(key, value)
        return RemoteWebDriver(command_executor=bs_url, options=options)

    else:
        edge_options = EdgeOptions()
        edge_options.add_argument("--start-maximized")
        return webdriver.Edge(options=edge_options)
