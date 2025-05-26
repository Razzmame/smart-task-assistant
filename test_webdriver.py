from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Prueba de apertura de navegador
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.google.com")

print("Navegador abierto correctamente.")
input("Pulsa ENTER para cerrar el navegador...")
driver.quit()

