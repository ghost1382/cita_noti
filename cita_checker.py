# cita_checker.py
import requests
from bs4 import BeautifulSoup

URL = "https://icp.administracionelectronica.gob.es/icpplus/citar"


def check_appointment(province_id="12", service_code="HUELLAS"):
    session = requests.Session()
    session.headers.update({"User-Agent": "Mozilla/5.0"})

    payload = {"provincia": province_id, "procedimiento": service_code}

    try:
        response = session.get(URL)
        if "En este momento no hay citas disponibles" in response.text:
            return False
        return True
    except Exception as e:
        print("Error checking cita:", e)
        return False
