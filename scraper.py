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
            #Stock Pendiente a codear.
            print(stock[0])
            num_indice = input("Ingrese índice del libro: ")
            guardar_libro(0,str(name[int(num_indice)]),str(price[int(num_indice)]))
            # TODO: Terminar el menú y funciones de este archivo.

        else:
            print('No nos pudimos conectar al sitio')
    except:
        pass

def guardar_libro(indice,nombre, precio):
    '''Método que se conecta con el modelo para guardar el libro'''
    miLibro = Libro()
    miLibro.ingresar_dato(indice, nombre, precio)

def crear_ddbb():
    ''' Validar mejor'''
    miLibro = Libro()
    respuesta = input('Desea crear la base de datos. (S o N)') 
    if respuesta == "S":
        miLibro.crear_db()
    else:
        print('Ya se creó la bbdd')

def ejecutar():
    '''Función para inciar otras funciones'''
    extraer()

if __name__ == "__main__":
    ejecutar()