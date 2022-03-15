from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from vet_api_rest.models import Nivel


class NivelResource(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.nivel = Nivel()

    def get(self, id_nivel):
        self.nivel.id_nivel = id_nivel
        nivel = self.nivel.seleccionar()
        print(nivel.json)
        return nivel

    def put(self, id_nivel):
        self.nivel.id_nivel = id_nivel
        print(f'put {__name__} endpoint; request: {request.json}')

        self.nivel.nivel = request.json['nivel']
        self.nivel.descripcion = request.json['descripcion']
        self.nivel.usuario_registro = request.json['usuario_registro']

        self.nivel.actualizar()
        return {"mensaje": "nivel actualizado correctamente"}

    def delete(self, id_nivel):
        self.nivel.id_nivel = id_nivel
        self.nivel.eliminar()

        return {"mensaje": "nivel eliminado correctamente"}


class NivelList(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.nivel = Nivel()

    def get(self):
        return self.nivel.listar()

    def post(self):
        print(f'post {__name__} endpoint; request: {request.json}')
        self.nivel.nivel = request.json['nivel']
        self.nivel.descripcion = request.json['descripcion']
        self.nivel.usuario_registro = request.json['usuario_registro']

        self.nivel.insertar()
        return {"mensaje": "nivel agregado correctamente"}, 201
