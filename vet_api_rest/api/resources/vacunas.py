from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from vet_api_rest.models import Vacunas


class VacunaResource(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.vacuna = Vacunas()

    def get(self, id_vacuna):
        self.vacuna.id_vacuna = id_vacuna
        vacuna = self.vacuna.seleccionar()
        print(vacuna.json)
        return vacuna

    def put(self, id_vacuna):
        self.vacuna.id_vacuna = id_vacuna
        print(f'put {__name__} endpoint; request: {request.json}')

        self.vacuna.id_mascota = request.json['id_mascota']
        self.vacuna.id_medicamento = request.json['id_medicamento']
        self.vacuna.fecha_vacuna = request.json['fecha_vacuna']
        self.vacuna.usuario_registro = request.json['usuario_registro']

        self.vacuna.actualizar()
        return {"mensaje": "vacuna actualizada correctamente"}

    def delete(self, id_vacuna):
        self.vacuna.id_vacuna = id_vacuna
        self.vacuna.eliminar()

        return {"mensaje": "vacuna eliminada correctamente"}


class VacunaList(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.vacuna = Vacunas()

    def get(self):
        return self.vacuna.listar()

    def post(self):
        print(f'post {__name__} endpoint; request: {request.json}')
        self.vacuna.id_mascota = request.json['id_mascota']
        self.vacuna.id_medicamento = request.json['id_medicamento']
        self.vacuna.fecha_vacuna = request.json['fecha_vacuna']
        self.vacuna.usuario_registro = request.json['usuario_registro']

        self.vacuna.insertar()
        return {"mensaje": "vacuna agregada correctamente"}, 201
