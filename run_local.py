import os
os.environ["PYTHONPATH"] = os.path.abspath("src")
os.system("behave features/el_pais_scraper.feature")
