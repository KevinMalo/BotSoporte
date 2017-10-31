from conexion import Conexion
import csv

class Datos(Conexion):
    
    def __init__(self):
        
        self.conectar('localhost', 27017, 'bot', 'datos')

    def guardar_csv(self):
            
        with open('Preguntas_Frecuentes_Software_P_blico_-_FAQ.csv', newline='') as csvfile:

            leer = csv.reader(csvfile, delimiter=';', quotechar='|')

            for i, row in enumerate(leer):
                
                if i != 0:
                    
                    self.guardar({'Orden':row[0], 
                                'Categoria':row[1], 
                                'Pregunta':row[2], 
                                'Respuesta':row[3],
                                'Categoria_en':row[4], 
                                'Pregunta_en':row[5], 
                                'Respuesta_en':row[6]})
                
                print(row)

#datos = Datos()
#datos.guardar_csv()


