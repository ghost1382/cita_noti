import undetected_chromedriver.v2 as uc
from selenium.webdriver.chrome.options import Options


def check_appointment():
    print("🟡 Checking for appointment...")

    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    options.add_argument('--window-size=1920x1080')

    driver = uc.Chrome(options=options)

    driver.get("https://sede.administracionespublicas.gob.es/pagina/index/directorio/icpplus")
    html = driver.page_source
    driver.quit()

    return "No hay citas" not in html  # Just an example
