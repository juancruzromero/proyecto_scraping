""" Archivo principal del proyecto """
import requests
import lxml.html as html
from scraper_model import Libro

"""
1) Constantes: El primer paso es ir al navegador
e identificar los datos que quiero scrapear.
"""
URL = 'http://books.toscrape.com/'
NAME = '//h3/a/text()'
PRICE = '//article[@class="product_pod"]/div[@class="product_price"]/p[@class="price_color"]/text()'
STOCK = '//article[@class="product_pod"]/div[@class="product_price"]/p[@class="instock availability"]/text()'


def extraer():
    """
    Método para conextarme a la url
    y extraer información
    """
    try:
        responese = requests.get(URL)
        if responese.status_code == 200:
            # Transformo caracteres especiales.
            home = responese.content.decode('utf-8')
            parsed = html.fromstring(home)
            name = parsed.xpath(NAME)
            price = parsed.xpath(PRICE)
            stock = parsed.xpath(STOCK)
            print(name[0])
            print(price[0])
            print(stock[0])
            guardar_libro(0,str(name[0]),str(price[0]))

        else:
            print('No nos pudimos conectar al sitio')
    except:
        pass

def guardar_libro(indice,nombre, precio):
    miLibro = Libro()
    miLibro.ingresar_dato(indice, nombre, precio)

def ejecutar():
    extraer()

if __name__ == "__main__":
    ejecutar()