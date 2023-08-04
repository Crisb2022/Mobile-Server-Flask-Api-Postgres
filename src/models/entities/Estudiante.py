# Entidad que vamos a enviar a a la bd

# Llamada al metodo de la DateFormat.py
from utils.DateFormat import DateFormat


class Estudiante():
    # Declaracion del constructor "Deben ser los datos de la db"
    def __init__(self, id_estudiante, nombres=None, 
                 apellidos=None, cedula=None, correo=None, usuario=None, 
                 password=None, image=None, nacimiento=None) -> None:
        self.id_estudiante = id_estudiante
        self.nombres = nombres
        self.apellidos = apellidos
        self.cedula = cedula
        self.correo = correo
        self.usuario = usuario
        self.password = password
        self.image = image
        self.nacimiento = nacimiento

    # Transformacion a JSON
    def to_JSON(self):
        return {
            'id_estudiante':  self.id_estudiante,
            'nombres': self.nombres,
            'apellidos': self.apellidos,
            'cedula': self.cedula,
            'correo': self.correo,
            'usuario': self.usuario,
            'password': self.password,
            'image': self.image,
            'nacimiento': DateFormat.convert_date(self.nacimiento),
        }
