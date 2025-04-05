import os
import subprocess
import time
from dotenv import load_dotenv

load_dotenv()

BROWSER_CONFIGS = [
    "win11_chrome",
    "win10_edge",
    "mac_safari",
    "ios_safari",
    "android_chrome"
]

build_id = f"ElPais_Scraper_Build_{int(time.time())}"

processes = []

for config in BROWSER_CONFIGS:
    env = os.environ.copy()
    env["RUN_ENV"] = "browserstack"
    env["BROWSER_CONFIG"] = config
    env["BUILD_ID"] = build_id

    cmd = ["behave", "features/el_pais_scraper.feature"]
    print(f"Starting test on: {config}")
    p = subprocess.Popen(cmd, env=env)
    processes.append((config, p))

for config, p in processes:
    p.wait()
    print(f"Finished test on: {config}")
