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
    driver.get("https://sede.administracionespublicas.gob.es/pagina/index/directorio/icpplus")
    print("✅ Page loaded.")
    html = driver.page_source
    return "No hay citas" not in html
except Exception as e:
    print("❌ Error during check:", e)
    return False
finally:
    driver.quit()
