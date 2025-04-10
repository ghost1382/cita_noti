import undetected_chromedriver as uc

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def check_appointment():
    print("🟡 Checking for appointment...")

    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    options.add_argument('--window-size=1920x1080')

    try:
        driver = uc.Chrome(options=options)
        driver.get("https://sede.administracionespublicas.gob.es/pagina/index/directorio/icpplus")
        time.sleep(3)  # wait for page to load
        print("✅ Page loaded.")
        html = driver.page_source
        return "No hay citas" not in html
    except Exception as e:
        print("❌ Error checking appointment:", e)
        return False
    finally:
        driver.quit()
