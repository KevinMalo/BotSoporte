from conexion import Conexion
from datos import Datos


class Categorias(Conexion):

    def __init__(self):
        self.conectar('localhost', 27017, 'bot', 'categorias')


    def agregar_categrias(self):

        datos_categorias = Datos()

        consultar = datos_categorias.consultar({})

        for resultado in consultar:
            #print (resultado)
            self.guardar({"categoria": resultado['Categoria'], "Idioma":"es"})      
            self.guardar({"categoria": resultado['Categoria_en'], "Idioma":"en"})
            
categoria = Categorias()
categoria.agregar_categrias()