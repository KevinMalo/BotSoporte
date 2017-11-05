from conexion import Conexion
from datos import Datos


class Preguntas(Conexion):

    def __init__(self):
        self.conectar('localhost', 27017, 'bot', 'preguntas')


    def agregar_preguntas(self):

        datos_preguntas = Datos()

        consultar = datos_preguntas.consultar({})

        for resultado in consultar:
            #print (resultado)
            self.guardar({"Pregunta": resultado['Pregunta'], "Respuesta": resultado['Respuesta'], "Categoria": resultado['Categoria']})       
            self.guardar({"Pregunta_en": resultado['Pregunta_en'], "Respuesta_en": resultado['Respuesta_en'], "Categoria_en": resultado['Categoria_en']})
        
#preguntas = Preguntas()
#preguntas.agregar_preguntas()