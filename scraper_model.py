""" Archivo en donde realizamos el modelo y la conexión a la BBDD"""
from peewee import *
import datetime

# En este caso, trabajaremos con Sqlite.
# Más info de peewee en http://docs.peewee-orm.com/en/latest/.
db = SqliteDatabase("data.db")

class Libro(Model):
    indice = IntegerField()
    name = TextField()
    #Por el momento, precio es de tipo string.
    price = TextField()
    timestamp = DateTimeField(default=datetime.datetime.now)

    def ingresar_dato(self, ind,nam, pri):
        '''
            Método para ingresar datos.
        '''
        db.connect()
        Libro.create(indice=ind, name=nam,price=pri)
        db.close()

    def crear_db(self):
        '''
        Método para crear la base de datos.
        '''
        db.connect()
        db.create_tables([Libro],safe=True)
        db.close()


    class Meta:
        database = db