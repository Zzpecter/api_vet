from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from vet_api_rest.models import Entidad


class EntidadResource(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.entidad = Entidad()

    def delete(self, id_entidad):
        self.entidad.id_entidad = id_entidad
        self.entidad.eliminar()

        return {"mensaje": "entidad eliminado correctamente"}


class EntidadList(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.entidad = Entidad()

    def post(self):
        print(f'post {__name__} endpoint; request: {request.json}')
        self.entidad.id_entidad = request.json['id_entidad']

        self.entidad.insertar()
        return {"mensaje": "entidad agregado correctamente"}, 201
