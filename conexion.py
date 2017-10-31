import pymongo
from pymongo import MongoClient
# Uso para conexiones remotas
# from urllib.parse import quote_plus

class Conexion:

    db = ''

    client = ''

    coleccion = ''

    def conectar(self, host, puerto, base_datos, coleccion):
        # Uso para conexiones remotas (agregar el parametro clave y usuario)
        #uri = "mongodb://%s:%s@%s:%i/%s?authMechanism=SCRAM-SHA-1" % (usuario, clave, host, puerto, base_datos)
        self.client = MongoClient(host, puerto)
        self.db = self.client[base_datos]
        self.coleccion = self.db[coleccion]

    # CREATE
    def guardar(self, dato):
        id = self.coleccion.insert_one(dato).inserted_id
        print(id)
        return id

    # UPDATE
    def editar(self, dato = {}, new_date = {}):
        up = self.coleccion.update( dato, {'$set':new_date} )
        #Ejemplo: db.estelar.update({_id:3}, {tipo:"planeta enano"})

    # READ
    def consultar(self, filtro = {}):
        
        mi_consulta = self.coleccion.find(filtro)
        return mi_consulta
        
            
    # DELETE
    def eliminar(self, dato):
        delete = self.coleccion.delete_one(dato)