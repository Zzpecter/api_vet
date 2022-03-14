from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from vet_api_rest.models import Citas


class CitasResource(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.citas = Citas()

    def get(self, id_cita):
        self.citas.id_cita = id_cita
        citas = self.citas.seleccionar()
        print(citas.json)
        return citas

    def put(self, id_cita):
        self.citas.id_cita = id_cita
        print(f'put @{__name__} endpoint, request: {request.json}')

        self.citas.id_mascota = request.json['id_mascota']
        self.citas.fecha_hora = request.json['fecha_hora']
        self.citas.motivo_cita = request.json['motivo_cita']
        self.citas.usuario_registro = request.json['usuario_registro']

        self.citas.actualizar()
        return {"mensaje": "citas actualizado correctamente"}

    def delete(self, id_cita):
        self.citas.id_cita = id_cita
        self.citas.eliminar()

        return {"mensaje": "citas eliminado correctamente"}


class CitasList(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.citas = Citas()

    def get(self):
        return self.citas.listar()

    def post(self):
        print(f'post @{__name__} endpoint, request: {request.json}')
        self.citas.id_mascota = request.json['id_mascota']
        self.citas.fecha_hora = request.json['fecha_hora']
        self.citas.motivo_cita = request.json['motivo_cita']
        self.citas.usuario_registro = request.json['usuario_registro']

        self.citas.insertar()
        return {"mensaje": "citas agregado correctamente"}, 201
