from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from vet_api_rest.models import Mascota


class MascotaResource(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.mascota = Mascota()

    def get(self, id_mascota):
        self.mascota.id_mascota = id_mascota
        mascota = self.mascota.seleccionar()
        print(mascota.json)
        return mascota

    def put(self, id_mascota):
        self.mascota.id_mascota = id_mascota
        print(f'put {__name__} endpoint; request: {request.json}')

        self.mascota.id_tipo_mascota = request.json['id_tipo_mascota']
        self.mascota.id_cliente = request.json['id_cliente']
        self.mascota.nombre_mascota = request.json['nombre_mascota']
        self.mascota.color = request.json['color']
        self.mascota.sexo_mascota = request.json['sexo_mascota']
        self.mascota.es_reproductor = request.json['es_reproductor']
        self.mascota.rasgos = request.json['rasgos']
        self.mascota.ref_foto = request.json['ref_foto']
        self.mascota.usuario_registro = request.json['usuario_registro']

        self.mascota.actualizar()
        return {"mensaje": "mascota actualizada correctamente"}

    def delete(self, id_mascota):
        self.mascota.id_mascota = id_mascota
        self.mascota.eliminar()

        return {"mensaje": "mascota eliminada correctamente"}


class MascotaList(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.mascota = Mascota()

    def get(self):
        return self.mascota.listar()

    def post(self):
        print(f'post {__name__} endpoint; request: {request.json}')
        self.mascota.id_tipo_mascota = request.json['id_tipo_mascota']
        self.mascota.id_cliente = request.json['id_cliente']
        self.mascota.nombre_mascota = request.json['nombre_mascota']
        self.mascota.color = request.json['color']
        self.mascota.sexo_mascota = request.json['sexo_mascota']
        self.mascota.es_reproductor = request.json['es_reproductor']
        self.mascota.rasgos = request.json['rasgos']
        self.mascota.ref_foto = request.json['ref_foto']
        self.mascota.usuario_registro = request.json['usuario_registro']

        self.mascota.insertar()
        return {"mensaje": "mascota agregada correctamente"}, 201
