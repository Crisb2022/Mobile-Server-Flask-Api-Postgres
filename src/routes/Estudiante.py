from flask import Blueprint, jsonify, request
import uuid
# Entities
from models.entities.Estudiante import Estudiante
# importar Modelos
from models.EstudianteModel import EstudianteModel

main=Blueprint('estudiante_blueprint', '__name__')


@main.route('/<usuario>')
def get_estudiantes(usuario):
    try:
        estudiante =  EstudianteModel.get_estudiantesOne(usuario)
        print (estudiante)
        if estudiante != None:
            return jsonify(estudiante)
        else: 
            return jsonify({}), 400
    except Exception as ex:
        return jsonify({
            'message': str(ex)
        }), 500

# ruta de estudiantes
@main.route('/add', methods=['POST'])
def add_estudiante():
    try:
        nombres = request.json['nombres']
        apellidos = request.json['apellidos']
        cedula = request.json['cedula']
        correo = request.json['correo']
        usuario = request.json['usuario']
        password = request.json['password']
        image = request.json['image']
        nacimiento = request.json['nacimiento']
        id_estudiante = uuid.uuid4()
        estudiante = Estudiante(str(id_estudiante), nombres, apellidos, cedula, correo, usuario, password, image, nacimiento)
        # llamamos al modelo 
        affected_row = EstudianteModel.createEstudiante(estudiante)
        if affected_row == 1:
            return jsonify(estudiante.id_estudiante)
        else:
            return jsonify({
                'message' : 'Error al insertar'
            }), 500
    except Exception as ex:
        return jsonify({
            'message': str(ex)
        }), 500
    
@main.route('/login/<usuario>/<password>')
def login_estudiantes(usuario, password):
    try:
        estudiante =  EstudianteModel.login_estudiante(usuario, password)
        print ('------',estudiante)
        if estudiante:
            return jsonify({
                "message": "Esta logeado"
            })
        else: 
            return jsonify({
                "message" : "come pipi"
            }), 400
    except Exception as ex:
        return jsonify({
            'message': str(ex)
        }), 500