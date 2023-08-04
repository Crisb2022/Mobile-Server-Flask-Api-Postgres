from flask import Flask
# importamos el diccionario creado en config.py
from config import config
# CORS
from flask_cors import CORS
# Routes
from routes import Estudiante

app=Flask(__name__)

# CORS: Acceso a la app por puerto establecido
CORS(app, resources={"*":{"origins":"http://192.168.100.240:5000"}})

# Manejo de errores cuando no se encuentra la pagina
def page_not_found(error):
    return "<h1>Pagina no encontrada</h1>", 404

if __name__=='__main__':
    # llamada al diccionario de config
    app.config.from_object(config['development'])
    # Registro de la ruta raiz
    app.register_blueprint(Estudiante.main, url_prefix='/api/estudiantes')
    
    app.register_error_handler(404, page_not_found)
    app.run()