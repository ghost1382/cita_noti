from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller
import time


def check_appointment():
    chromedriver_autoinstaller.install()
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    try:
        print("🌐 Opening page...")
        driver.get(
            "https://sede.administracionespublicas.gob.es/pagina/index/directorio/icpplus"
        )
        time.sleep(2)

        print("🔘 Clicking 'Acceder al procedimiento'")
        acceder_btn = driver.find_element(
            "xpath", "//a[contains(text(),'Acceder al procedimiento')]")
        acceder_btn.click()
        time.sleep(2)

        print("📍 Selecting province: Tarragona")
        provincia = driver.find_element("name", "provincias")
        provincia.send_keys("TARRAGONA")
        driver.find_element("name", "aceptar").click()
        time.sleep(2)

        print("🏢 Selecting office: TORTOSA + trámite: HUELLAS")
        oficina = driver.find_element("name", "oficinas")
        oficina.send_keys("TORTOSA")
        tramite = driver.find_element("name", "tramites")
        tramite.send_keys("POLICIA - TOMA DE HUELLAS (EXPEDICION DE TARJETA)")
        driver.find_element("name", "aceptar").click()
        time.sleep(2)

        print("🔓 Clicking 'Sin certificado'")
        sin_cert_btn = driver.find_element(
            "xpath", "//a[contains(text(), 'Continuar sin certificado')]")
        sin_cert_btn.click()
        time.sleep(2)

        print("📄 Getting HTML...")
        html = driver.page_source
        print("✅ HTML loaded. Checking for text...")

        if "no hay citas disponibles" in html.lower():
            print("🚫 No appointments found.")
            return False
        else:
            print("✅ Appointment available!")
            return True

    except Exception as e:
        print("❌ Error in checker:", e)
        return False
    finally:
        driver.quit()
