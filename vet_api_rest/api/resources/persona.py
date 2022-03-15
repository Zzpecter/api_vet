from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from vet_api_rest.models import Persona


class PersonaResource(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.persona = Persona()

    def get(self, id_persona):
        self.persona.id_persona = id_persona
        persona = self.persona.seleccionar()
        print(persona.json)
        return persona

    def put(self, id_persona):
        self.persona.id_persona = id_persona
        print(f'put {__name__} endpoint; request: {request.json}')

        self.persona.nombres = request.json['nombres']
        self.persona.apellidos = request.json['apellidos']
        self.persona.apodo = request.json['apodo']
        self.persona.usuario_registro = request.json['usuario_registro']

        self.persona.actualizar()
        return {"mensaje": "persona actualizado correctamente"}

    def delete(self, id_persona):
        self.persona.id_persona = id_persona
        self.persona.eliminar()

        return {"mensaje": "persona eliminado correctamente"}


class PersonaList(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.persona = Persona()

    def get(self):
        return self.persona.listar()

    def post(self):
        print(f'post {__name__} endpoint; request: {request.json}')
        self.persona.id_persona = request.json['id_persona']
        self.persona.nombres = request.json['nombres']
        self.persona.apellidos = request.json['apellidos']
        self.persona.apodo = request.json['apodo']
        self.persona.usuario_registro = request.json['usuario_registro']

        self.persona.insertar()
        return {"mensaje": "persona agregado correctamente"}, 201
