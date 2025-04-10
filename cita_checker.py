import undetected_chromedriver.v2 as uc
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller
import time

def check_appointment():
    print("🟡 Checking for appointment...")

    # Auto install the chromedriver if it's not present
    chromedriver_autoinstaller.install()

    # Setup Chrome options for headless mode
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    options.add_argument('--window-size=1920x1080')

    # Initialize the WebDriver (undetected chromedriver)
    driver = uc.Chrome(options=options)

    # Open the website
    driver.get("https://sede.administracionespublicas.gob.es/pagina/index/directorio/icpplus")
    time.sleep(3)  # Let the page load properly

    # Extract the page source
    html = driver.page_source

    # Close the WebDriver
    driver.quit()

    # If "No hay citas" is not in the HTML, then citas are available
    if "No hay citas" in html:
        print("🚫 No citas available.")
        return False
    else:
        print("✅ CITA FOUND!")
        return True
