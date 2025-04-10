import undetected_chromedriver as uc

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def check_appointment():
    print("🟡 Checking for appointment...")

    try:
        options = uc.ChromeOptions()
        options.headless = True
        driver = uc.Chrome(options=options)

        driver.get("https://sede.administracionespublicas.gob.es/pagina/index/directorio/icpplus")
        html = driver.page_source
        driver.quit()

        print("✅ Page loaded.")
        return True  # Force simulate cita found

    except Exception as e:
        print("❌ Error during check:", e)
        return False

    finally:
        driver.quit()
