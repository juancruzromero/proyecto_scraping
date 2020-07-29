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
        db.connect()
        Libro.create(indice=ind, name=nam,price=pri)
        db.close()

    class Meta:
        database = db