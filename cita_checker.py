from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller


def check_appointment():
    print("🟡 Checking for appointment...")

    chromedriver_autoinstaller.install()

    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    options.add_argument('--window-size=1920x1080')

    driver = webdriver.Chrome(options=options)

    # Open the Cita website
    driver.get("https://sede.administracionespublicas.gob.es/pagina/index/directorio/icpplus")

    # Get the page HTML and close the browser
    html = driver.page_source
    driver.quit()

    # Check if the phrase "No hay citas" appears (meaning no appointments)
    return "No hay citas" not in html
