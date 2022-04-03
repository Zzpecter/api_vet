from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from vet_api_rest.models import TratamientosPendientes


class TratamientosPendientesResource(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.tratamientos_pendientes = TratamientosPendientes()

    def get(self, id_tratamientos_pendientes):
        self.tratamientos_pendientes.id_tratamientos_pendientes = id_tratamientos_pendientes
        tratamientos_pendientes = self.tratamientos_pendientes.seleccionar()
        print(tratamientos_pendientes.json)
        return tratamientos_pendientes

    def put(self, id_tratamientos_pendientes):
        self.tratamientos_pendientes.id_tratamientos_pendientes = id_tratamientos_pendientes
        print(f'put {__name__} endpoint; request: {request.json}')

        self.tratamientos_pendientes.id_mascota = request.json['id_mascota']
        self.tratamientos_pendientes.id_medicamento = request.json['id_medicamento']
        self.tratamientos_pendientes.fecha_tratamiento = request.json['fecha_tratamiento']
        self.tratamientos_pendientes.fecha_recordatorio = request.json['fecha_recordatorio']
        self.tratamientos_pendientes.comentario = request.json['comentario']
        self.tratamientos_pendientes.mensaje_enviado = request.json['mensaje_enviado']
        self.tratamientos_pendientes.usuario_registro = request.json['usuario_registro']

        self.tratamientos_pendientes.actualizar()
        return {"mensaje": "tratamientos_pendientes actualizada correctamente"}

    def delete(self, id_tratamientos_pendientes):
        self.tratamientos_pendientes.id_tratamientos_pendientes = id_tratamientos_pendientes
        self.tratamientos_pendientes.eliminar()

        return {"mensaje": "tratamientos_pendientes eliminada correctamente"}


class TratamientosPendientesList(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.tratamientos_pendientes = TratamientosPendientes()

    def get(self):
        return self.tratamientos_pendientes.listar()

    def post(self):
        print(f'post {__name__} endpoint; request: {request.json}')
        self.tratamientos_pendientes.id_mascota = request.json['id_mascota']
        self.tratamientos_pendientes.id_medicamento = request.json['id_medicamento']
        self.tratamientos_pendientes.fecha_tratamiento = request.json['fecha_tratamiento']
        self.tratamientos_pendientes.fecha_recordatorio = request.json['fecha_recordatorio']
        self.tratamientos_pendientes.comentario = request.json['comentario']
        self.tratamientos_pendientes.mensaje_enviado = request.json['mensaje_enviado']
        self.tratamientos_pendientes.usuario_registro = request.json['usuario_registro']

        self.tratamientos_pendientes.insertar()
        return {"mensaje": "tratamientos_pendientes agregada correctamente"}, 201
