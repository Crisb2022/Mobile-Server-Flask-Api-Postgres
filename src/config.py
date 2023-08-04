# Libreria para la conexion con las variables de entorno
from decouple import config

# Llamamos a la Secret Key
class Config:
    SECRET_KEY = config('SECRET_KEY')

# Refrescar el servidor en cada cambio
class DevelopmentConfig(Config):
    DEBUG = True

# diccionario para regresar la llave de Development
config = {
    'development': DevelopmentConfig
}
