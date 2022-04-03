from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from vet_api_rest.models import Raza


class RazaResource(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.raza = Raza()

    def get(self, id_raza):
        self.raza.id_raza = id_raza
        raza = self.raza.seleccionar()
        print(raza.json)
        return raza

    def put(self, id_raza):
        self.raza.id_raza = id_raza
        print(f'put {__name__} endpoint; request: {request.json}')

        self.raza.id_tipo_mascota = request.json['id_tipo_mascota']
        self.raza.nombre_raza = request.json['nombre_raza']
        self.raza.usuario_registro = request.json['usuario_registro']

        self.raza.actualizar()
        return {"mensaje": "raza actualizada correctamente"}

    def delete(self, id_raza):
        self.raza.id_raza = id_raza
        self.raza.eliminar()

        return {"mensaje": "raza eliminada correctamente"}


class RazaList(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.raza = Raza()

    def get(self):
        return self.raza.listar()

    def post(self):
        print(f'post {__name__} endpoint; request: {request.json}')
        self.raza.id_tipo_mascota = request.json['id_tipo_mascota']
        self.raza.nombre_raza = request.json['nombre_raza']
        self.raza.usuario_registro = request.json['usuario_registro']

        self.raza.insertar()
        return {"mensaje": "raza agregada correctamente"}, 201
