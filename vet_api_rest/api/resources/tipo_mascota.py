from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from vet_api_rest.models import TipoMascota


class TipoMascotaResource(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.tipo_mascota = TipoMascota()

    def get(self, id_tipo_mascota):
        self.tipo_mascota.id_tipo_mascota = id_tipo_mascota
        tipo_mascota = self.tipo_mascota.seleccionar()
        print(tipo_mascota.json)
        return tipo_mascota

    def put(self, id_tipo_mascota):
        self.tipo_mascota.id_tipo_mascota = id_tipo_mascota
        print(f'put {__name__} endpoint; request: {request.json}')

        self.tipo_mascota.nombre_tipo_mascota = request.json['nombre_tipo_mascota']
        self.tipo_mascota.usuario_registro = request.json['usuario_registro']

        self.tipo_mascota.actualizar()
        return {"mensaje": "tipo_mascota actualizada correctamente"}

    def delete(self, id_tipo_mascota):
        self.tipo_mascota.id_tipo_mascota = id_tipo_mascota
        self.tipo_mascota.eliminar()

        return {"mensaje": "tipo_mascota eliminada correctamente"}


class TipoMascotaList(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.tipo_mascota = TipoMascota()

    def get(self):
        return self.tipo_mascota.listar()

    def post(self):
        print(f'post {__name__} endpoint; request: {request.json}')
        self.tipo_mascota.nombre_tipo_mascota = request.json['nombre_tipo_mascota']
        self.tipo_mascota.usuario_registro = request.json['usuario_registro']

        self.tipo_mascota.insertar()
        return {"mensaje": "tipo_mascota agregada correctamente"}, 201
