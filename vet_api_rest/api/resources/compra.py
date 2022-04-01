from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from vet_api_rest.models import Compra


class CompraResource(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.compra = Compra()

    def get(self, id_compra):
        self.compra.id_compra = id_compra
        compra = self.compra.seleccionar()
        print(compra.json)
        return compra

    def put(self, id_compra):
        self.compra.id_compra = id_compra
        print(f'put {__name__} endpoint; request: {request.json}')

        self.compra.id_usuario = request.json['id_usuario']
        self.compra.id_proveedor = request.json['id_proveedor']
        self.compra.monto_total = request.json['monto_total']
        self.compra.fecha_hora = request.json['fecha_hora']
        self.compra.usuario_registro = request.json['usuario_registro']

        self.compra.actualizar()
        return {"mensaje": "compra actualizada correctamente"}

    def delete(self, id_compra):
        self.compra.id_compra = id_compra
        self.compra.eliminar()

        return {"mensaje": "compra eliminada correctamente"}


class CompraList(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.compra = Compra()

    def get(self):
        return self.compra.listar()

    def post(self):
        print(f'post {__name__} endpoint; request: {request.json}')
        self.compra.id_usuario = request.json['id_usuario']
        self.compra.id_proveedor = request.json['id_proveedor']
        self.compra.monto_total = request.json['monto_total']
        self.compra.fecha_hora = request.json['fecha_hora']
        self.compra.usuario_registro = request.json['usuario_registro']

        self.compra.insertar()
        return {"mensaje": "compra agregada correctamente"}, 201
