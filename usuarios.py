from conexion import Conexion

class Usuarios(Conexion):

    def __init__(self):
        self.conectar('localhost', 27017, 'bot', 'usuarios')

    def agregar_usuario(self, nombre, telefono, estado):
        dato = {
            'nombre': nombre,
            'telefono': telefono,
            'estado': estado
        }

        id = self.guardar(dato)
