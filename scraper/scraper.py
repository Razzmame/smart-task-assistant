# -----------------------------------------
# IMPORTACIONES
# -----------------------------------------
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

BASE_URL = "https://books.toscrape.com/catalogue/"
BOOK_CLASS = "product_pod"

# -----------------------------------------
# FUNCIONES
# -----------------------------------------
def scrape_page (url, driver):
    """
    Llama al driver de la url proporcionada, y extrae la lista de elementos por clase
    """

    driver.get(url)
    elements = driver.find_elements(By.CLASS_NAME, BOOK_CLASS)
    return books_from_page(elements)

def books_from_page (elements):
    """
    Extrae los libros visibles en la página actual y devuelve una lista de diccionarios con título, precio, etc.
    """

    books = []

    for book in elements:
        
        #Title
        title = book.find_element(By.TAG_NAME, "h3")
        
        #Price
        price = book.find_element(By.CLASS_NAME, "price_color")
        
        #Rating
        rating = book.find_element(By.CLASS_NAME, "star-rating")
        rating_classes = rating.get_attribute ("class")

        #Esto nos devuelve la cadena "star-rating [num_estrellas]"
        #Partimos la cadena y nos quedamos el último elemento

        rating = rating_classes.split()[-1]

        #Stock con selector
        stock = book.find_element(By.CSS_SELECTOR, "p.instock.availability")
        stock = stock.text.strip()

        #Aniadimos elemento a la lista
        books.append({
            "title": title.text,
            "price": price.text,
            "rating": rating,
            "availability": stock
        })

    return books
    
# -----------------------------------------
# CÓDIGO PRINCIPAL 
# -----------------------------------------

#Url de la primera página 
page = "page-1.html"
all_books = []

#Esto hace que las operaciones sobre el navegador se realicen en segundo plano
options = Options()
options.add_argument("--headless")

#Inicializamos el driver y le proporcionamos el sitio web
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get(BASE_URL + page)

#Esto parte el texto por el "of", nos quedamos con el elemento final
#Quitamos los espacios y convertimos en número
pags = driver.find_element(By.CLASS_NAME, "current")
pags = int(pags.text.split("of")[-1].strip())

#Escrapeamos primera página evitando redundar
elements = driver.find_elements(By.CLASS_NAME, BOOK_CLASS)
all_books += books_from_page (elements)

for i in range(2, 10):
    #Definimos la url para cada página
    url = BASE_URL + f"page-{i}.html"
    all_books += scrape_page(url, driver)
    print(f"Scrapeando página {i}/{pags}")

print(all_books)

driver.quit()


