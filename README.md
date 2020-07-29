# Proyecto Web Scraper #

El proyecto consta en traer datos de la web de venta de libros http://books.toscrape.com/, y poder almacenar en una base de datos relacional sqlite3 el título y su precio.

- Aclaraciones Importantes: Este proyecto aún está en desarrollo.

## Consideraciones Legales ##

Siempre que sea realice un scraping de la web, debemos considerar que en la raiz de la web, hay un archivo llamado "Robots.txt" en donde nos pueden limitar nuestro scraping en algunos sectores del sitio.

## Version de Python, Librerias y SQLite ##

- Se trabajó con la versión 3.8.2 de python y las librerías que se utilizaron en este proyecto están en requirements.txt

- Más información de entornos virtuales y manejo de paquetes pip en la documentación oficial de python:
https://docs.python.org/3/tutorial/venv.html#managing-packages-with-pip

- Por último, es necesario tener instalado SQLite, por eso comparto su web para instalarlo, dependiendo de tu sistema operativo:
https://www.sqlite.org/download.html

## Configuración del entorno para ejecutar este proyecto ##

### Paso 1 ###
Se debe configurar el entorno virtual. Yo, personalmente por convención lo llemé venv y lo ignoré en archivo .gitignore antes de subirlo al repositorio.
Luego instalar las librerías (Ver más arriba el punto "Liberías de python a utilizar")

### Paso 2 ###

El programa cuenta con dos archivos principales:

- El scraper.py ejecutamos la extracción de datos de la web y guardamos los datos en la base de datos Sqlite3.

- El scraper_model.py es el modelo, en donde utilizamos la librería peewee para utilizar un ORM para la conexión a la base de datos.

## Ejecución del programa ##

- El programa inicia ejecutando el archivo scraper.py
- Luego, el programa pregunta si desea crear la bbdd, esta solo se puede crear una sola vez.

- Luego si la base de datos está creada, el sistema le pregunta al usuario el número de índice que desea almacenar.

- El programa guarda el libro en la base de datos.