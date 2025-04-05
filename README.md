
# 📰 El Pais Scraper Framework

A robust and scalable automation framework that scrapes articles from [El Pais](https://elpais.com/), analyzes the content, translates it into English, and validates key aspects using **Selenium**, **Behave BDD**, and cloud execution via **BrowserStack**.

---

## 🚀 Tech Stack

- 🧪 **Selenium WebDriver**
- 🌐 **BrowserStack Integration**
- 🧾 **Behave BDD** with Gherkin Feature Files
- 🛠 **Custom Translator API & Text Analyzer**
- 📄 **.env Configuration** with dotenv
- 🐍 **Python 3.8+**

---

## 📁 Project Structure

```
el_pais_scraper
├── api                    # Translation API and models
│   ├── __init__.py
│   ├── translate_request.py
│   ├── translate_response.py
│   └── translator.py
│
├── driver                 # WebDriver and BrowserStack logic
│   ├── __init__.py
│   ├── driver_factory.py
│
├── model                  # Data models for articles
│   └── article.py
│
├── scraper                # Article scraping logic
│   └── article_fetcher.py
│
├── util                   # Utility classes
│   ├── __init__.py
│   ├── cookie_handler.py
│   ├── image_downloader.py
│   ├── language_verifier.py
│   ├── logger.py
│   ├── print_helper.py
│   ├── supporting_utilities.py
│   └── text_analyzer.py

features
├── el_pais_scraper.feature # Behave feature file
└── environment.py         # Behave environment setup
├── steps
│   └── step_defs.py       # Step definitions for Behave BDD
├── browserstack_config
│   └── capabilities_config.json       # Step definitions for Behave BDD

resources
├── Images/                          # Folder for storing downloaded images
├── .env.template                    # Template for environment variables
├── .env                             # Actual environment variable file
├── run_local.py                     # To run file locally
├── run_cross_browser_platform.py    # To run files in browser stack
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repo

```bash
git clone https://github.com/iamragavendrans/el_pais_scraper.git
cd el_pais_scraper
```

### 2️⃣ Configure Environment Variables

Rename `.env.template` → `.env` and update it with your BrowserStack credentials and any other necessary details.

```env
BROWSERSTACK_USERNAME=your_username
BROWSERSTACK_ACCESS_KEY=your_access_key
RAPIDAPI_KEY=your_rapidapi_key
```

### 3️⃣ Install Dependencies

Make sure you have **Python 3.8+** and **pip** installed. Then install the dependencies:

```bash
pip install -r requirements.txt
```

---

## 🧪 Running the Tests

You can run the tests using **Behave**:

```bash
behave
```

Or use the following command for more detailed output:

```bash
behave -v
```

---

## 🧠 Features Covered

- ✅ Web scraping of the latest El Pais articles
- ✅ Language detection and English translation
- ✅ Text analysis and keyword validation
- ✅ Download article-related images
- ✅ Cross-browser cloud execution via BrowserStack
- ✅ Retry mechanism for flaky tests
- ✅ Test lifecycle management via Hooks

---
