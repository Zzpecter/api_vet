from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from vet_api_rest.models import Servicios


class ServicioResource(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.servicio = Servicios()

    def get(self, id_servicio):
        self.servicio.id_servicio = id_servicio
        servicio = self.servicio.seleccionar()
        print(servicio.json)
        return servicio

    def put(self, id_servicio):
        self.servicio.id_servicio = id_servicio
        print(f'put {__name__} endpoint; request: {request.json}')

        self.servicio.nombre_servicio = request.json['nombre_servicio']
        self.servicio.costo = request.json['costo']
        self.servicio.usuario_registro = request.json['usuario_registro']

        self.servicio.actualizar()
        return {"mensaje": "servicio actualizada correctamente"}

    def delete(self, id_servicio):
        self.servicio.id_servicio = id_servicio
        self.servicio.eliminar()

        return {"mensaje": "servicio eliminada correctamente"}


class ServicioList(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.servicio = Servicios()

    def get(self):
        return self.servicio.listar()

    def post(self):
        print(f'post {__name__} endpoint; request: {request.json}')
        self.servicio.nombre_servicio = request.json['nombre_servicio']
        self.servicio.costo = request.json['costo']
        self.servicio.usuario_registro = request.json['usuario_registro']

        self.servicio.insertar()
        return {"mensaje": "servicio agregada correctamente"}, 201
