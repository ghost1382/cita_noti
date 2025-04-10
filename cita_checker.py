from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def check_appointment():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Step 1: Open main page
        driver.get("https://sede.administracionespublicas.gob.es/icpplus/index.html")
        time.sleep(1)

        # Step 2: Click "Acceder al procedimiento"
        acceder_btn = driver.find_element(By.LINK_TEXT, "Acceder al procedimiento")
        acceder_btn.click()
        time.sleep(1)

        # Step 3: Select province
        provincia = driver.find_element(By.NAME, "provincias")
        provincia.send_keys("TARRAGONA")
        driver.find_element(By.NAME, "btnAceptar").click()
        time.sleep(1)

        # Step 4: Select oficina and trámite
        oficina = driver.find_element(By.NAME, "oficinas")
        oficina.send_keys("TORTOSA")
        tramite = driver.find_element(By.NAME, "tramites")
        tramite.send_keys("POLICIA – TOMA DE HUELLAS")
        driver.find_element(By.NAME, "btnAceptar").click()
        time.sleep(1)

        # Step 5: Click on "Entrar sin certificado"
        entrar_btn = driver.find_element(By.XPATH, "//input[@value='Entrar']")
        entrar_btn.click()
        time.sleep(2)

        # Step 6: Check for cita availability message
        page_source = driver.page_source.lower()

        if "no hay citas disponibles" in page_source:
            return False  # No citas
        else:
            return True   # Citas available!

    except Exception as e:
        print("⚠️ Error during cita check:", e)
        return False

    finally:
        driver.quit()
