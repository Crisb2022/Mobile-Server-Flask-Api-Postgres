# Traemos el modelo de la bd
from db.db import get_connection
from .entities.Estudiante import Estudiante


class EstudianteModel():

    @classmethod
    def createEstudiante(self, estudiante):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO public.estudiantes(
	                                id_estudiante, nombres, apellidos, cedula, correo, usuario, password, image, nacimiento)
	                                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)""", (estudiante.id_estudiante, estudiante.nombres, estudiante.apellidos, estudiante.cedula, estudiante.correo, estudiante.usuario, estudiante.password, estudiante.image, estudiante.nacimiento))
                affected_row = cursor.rowcount
                connection.commit()
            connection.close
            return affected_row
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_estudiantesOne(self, usuario):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                # Corregir el error de la imagen
                cursor.execute(
                    "SELECT id_estudiante, nombres, apellidos, cedula, correo, usuario, password, image, nacimiento FROM estudiantes WHERE usuario =%s", (usuario,))
                row = cursor.fetchone()
                estudiante = None
                if row != None:
                    estudiante = Estudiante(
                        row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
                    estudiante = estudiante.to_JSON()
                connection.close
                return estudiante
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def login_estudiante(self, usuario, password):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                # Corregir el error de la imagen
                cursor.execute(
                    "SELECT id_estudiante, nombres, apellidos, cedula, correo, usuario, password, image, nacimiento FROM estudiantes WHERE usuario =%s AND password =%s", (usuario, password))
                row = cursor.fetchone()
                isLogin = False
                if row != None:
                    isLogin = True
                connection.close
                return isLogin
        except Exception as ex:
            raise Exception(ex)
