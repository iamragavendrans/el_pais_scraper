from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

os.environ["RUN_ENV"] = "browserstack"
os.environ["BROWSER_CONFIG"] = "win11_chrome"
os.environ["BROWSER_CONFIG"] = "win10_edge"
os.environ["BROWSER_CONFIG"] = "mac_safari"
os.environ["BROWSER_CONFIG"] = "ios_safari"
os.environ["BROWSER_CONFIG"] = "android_chrome"

os.system("behave features/el_pais_scraper.feature")
