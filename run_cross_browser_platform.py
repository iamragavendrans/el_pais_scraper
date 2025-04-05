import os
import subprocess

from dotenv import load_dotenv

load_dotenv()

BROWSER_CONFIGS = [
    "win11_chrome",
    "win10_edge",
    # "mac_safari",
    # "ios_safari",
    # "android_chrome"
]

processes = []

for config in BROWSER_CONFIGS:
    env = os.environ.copy()
    env["RUN_ENV"] = "browserstack"
    env["BROWSER_CONFIG"] = config

    cmd = ["behave", "features/el_pais_scraper.feature"]
    print(f"Starting test on: {config}")
    p = subprocess.Popen(cmd, env=env)
    processes.append((config, p))

# Wait for all to finish
for config, p in processes:
    p.wait()
    print(f"Finished test on: {config}")
