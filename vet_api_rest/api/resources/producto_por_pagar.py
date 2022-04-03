from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from vet_api_rest.models import ProductoPorPagar


class ProductoPorPagarResource(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.producto_por_pagar = ProductoPorPagar()

    def get(self, id_producto_por_pagar):
        self.producto_por_pagar.id_producto_por_pagar = id_producto_por_pagar
        producto_por_pagar = self.producto_por_pagar.seleccionar()
        print(producto_por_pagar.json)
        return producto_por_pagar

    def put(self, id_producto_por_pagar):
        self.producto_por_pagar.id_producto_por_pagar = id_producto_por_pagar
        print(f'put {__name__} endpoint; request: {request.json}')

        self.producto_por_pagar.id_producto = request.json['id_producto']
        self.producto_por_pagar.id_cliente = request.json['id_cliente']
        self.producto_por_pagar.cantidad = request.json['cantidad']
        self.producto_por_pagar.usuario_registro = request.json['usuario_registro']

        self.producto_por_pagar.actualizar()
        return {"mensaje": "producto_por_pagar actualizada correctamente"}

    def delete(self, id_producto_por_pagar):
        self.producto_por_pagar.id_producto_por_pagar = id_producto_por_pagar
        self.producto_por_pagar.eliminar()

        return {"mensaje": "producto_por_pagar eliminada correctamente"}


class ProductoPorPagarList(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.producto_por_pagar = ProductoPorPagar()

    def get(self):
        return self.producto_por_pagar.listar()

    def post(self):
        print(f'post {__name__} endpoint; request: {request.json}')
        self.producto_por_pagar.id_producto = request.json['id_producto']
        self.producto_por_pagar.id_cliente = request.json['id_cliente']
        self.producto_por_pagar.cantidad = request.json['cantidad']
        self.producto_por_pagar.usuario_registro = request.json['usuario_registro']

        self.producto_por_pagar.insertar()
        return {"mensaje": "producto_por_pagar agregada correctamente"}, 201
