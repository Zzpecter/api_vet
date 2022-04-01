from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from vet_api_rest.models import HistorialMascota


class HistorialMascotaResource(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.historial_mascota = HistorialMascota()

    def get(self, id_historial_mascota):
        self.historial_mascota.id_historial_mascota = id_historial_mascota
        historial_mascota = self.historial_mascota.seleccionar()
        print(historial_mascota.json)
        return historial_mascota

    def put(self, id_historial_mascota):
        self.historial_mascota.id_historial_mascota = id_historial_mascota
        print(f'put {__name__} endpoint; request: {request.json}')

        self.historial_mascota.id_mascota = request.json['id_mascota']
        self.historial_mascota.peso_actual_gr = request.json['peso_actual_gr']
        self.historial_mascota.temperatura_c = request.json['temperatura_c']
        self.historial_mascota.descripcion_cliente = request.json['descripcion_cliente']
        self.historial_mascota.diagnostico = request.json['diagnostico']
        self.historial_mascota.conclusiones = request.json['conclusiones']
        self.historial_mascota.fecha = request.json['fecha']
        self.historial_mascota.usuario_registro = request.json['usuario_registro']

        self.historial_mascota.actualizar()
        return {"mensaje": "historial_mascota actualizada correctamente"}

    def delete(self, id_historial_mascota):
        self.historial_mascota.id_historial_mascota = id_historial_mascota
        self.historial_mascota.eliminar()

        return {"mensaje": "historial_mascota eliminada correctamente"}


class HistorialMascotaList(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.historial_mascota = HistorialMascota()

    def get(self):
        return self.historial_mascota.listar()

    def post(self):
        print(f'post {__name__} endpoint; request: {request.json}')
        self.historial_mascota.id_mascota = request.json['id_mascota']
        self.historial_mascota.peso_actual_gr = request.json['peso_actual_gr']
        self.historial_mascota.temperatura_c = request.json['temperatura_c']
        self.historial_mascota.descripcion_cliente = request.json['descripcion_cliente']
        self.historial_mascota.diagnostico = request.json['diagnostico']
        self.historial_mascota.conclusiones = request.json['conclusiones']
        self.historial_mascota.fecha = request.json['fecha']
        self.historial_mascota.usuario_registro = request.json['usuario_registro']

        self.historial_mascota.insertar()
        return {"mensaje": "historial_mascota agregada correctamente"}, 201
