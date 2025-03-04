import os
import webbrowser
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def buscar_producto(codigo):
    """
    Busca un producto en la página go-upc.com con un código UPC.
    """
    url = "https://go-upc.com/"
    driver = webdriver.Chrome()
    try:
        driver.get(url)
        time.sleep(2)
        
        # Busca el campo de entrada y envía el código
        input_box = driver.find_element(By.NAME, "upc")
        input_box.send_keys(codigo)
        input_box.submit()
        time.sleep(3)
        
        # Extrae el nombre del producto
        soup = BeautifulSoup(driver.page_source, "html.parser")
        producto = soup.find("h1").text.strip()
        print(f"Producto encontrado: {producto}")
        return producto
    except Exception as e:
        print("No se encontró el producto:", e)
        return None
    finally:
        driver.quit()

def buscar_imagen(query):
    """
    Busca imágenes en Bing basándose en el nombre del producto.
    """
    url = f"https://www.bing.com/images/search?q={query.replace(' ', '+')}"
    print(f"Buscando imágenes para: {query}")
    webbrowser.open(url)

if __name__ == "__main__":
    codigo = input("Ingrese el código UPC: ")
    producto = buscar_producto(codigo)
    if producto:
        buscar_imagen(producto)
    else:
        print("No se pudo realizar la búsqueda de imágenes.")
