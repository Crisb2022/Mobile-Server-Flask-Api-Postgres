import psycopg2                         # Conexion con la bd
from psycopg2 import DatabaseError      # Captura de los errores
from decouple import config             # variables de configuracion

# Obtenemos la conexion con postgres a traves de .env
def get_connection():
    try:
        return psycopg2.connect(
            host=config('PGSQL_HOST'),
            user=config('PGSQL_USER'),
            password=config('PGSQL_PASSWORD'),
            database=config('PGSQL_DATABASE')
        )
    except DatabaseError as ex:
        raise ex   