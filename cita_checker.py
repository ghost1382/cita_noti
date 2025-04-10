import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def check_appointment():
    print("🟡 Checking for appointment...")

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920x1080")

    driver = uc.Chrome(options=options, use_subprocess=True)

try:
    driver.get("https://example.com")
    print("✅ Page loaded.")
except Exception as e:
    print("❌ Error loading page:", e)
