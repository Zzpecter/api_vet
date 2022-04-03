from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from vet_api_rest.models import Venta


class VentaResource(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.venta = Venta()

    def get(self, id_venta):
        self.venta.id_venta = id_venta
        venta = self.venta.seleccionar()
        print(venta.json)
        return venta

    def put(self, id_venta):
        self.venta.id_venta = id_venta
        print(f'put {__name__} endpoint; request: {request.json}')

        self.venta.id_usuario = request.json['id_usuario']
        self.venta.id_cliente = request.json['id_cliente']
        self.venta.monto_total = request.json['monto_total']
        self.venta.fecha_hora = request.json['fecha_hora']
        self.venta.usuario_registro = request.json['usuario_registro']

        self.venta.actualizar()
        return {"mensaje": "venta actualizada correctamente"}

    def delete(self, id_venta):
        self.venta.id_venta = id_venta
        self.venta.eliminar()

        return {"mensaje": "venta eliminada correctamente"}


class VentaList(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.venta = Venta()

    def get(self):
        return self.venta.listar()

    def post(self):
        print(f'post {__name__} endpoint; request: {request.json}')
        self.venta.id_usuario = request.json['id_usuario']
        self.venta.id_cliente = request.json['id_cliente']
        self.venta.monto_total = request.json['monto_total']
        self.venta.fecha_hora = request.json['fecha_hora']
        self.venta.usuario_registro = request.json['usuario_registro']

        self.venta.insertar()
        return {"mensaje": "venta agregada correctamente"}, 201
