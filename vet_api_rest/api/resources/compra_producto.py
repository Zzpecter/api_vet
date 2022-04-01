from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from vet_api_rest.models import CompraProducto


class CompraProductoResource(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.compra_producto = CompraProducto()

    def get(self, id_compra_producto):
        self.compra_producto.id_compra_producto = id_compra_producto
        compra_producto = self.compra_producto.seleccionar()
        print(compra_producto.json)
        return compra_producto

    def put(self, id_compra_producto):
        self.compra_producto.id_compra_producto = id_compra_producto
        print(f'put {__name__} endpoint; request: {request.json}')

        self.compra_producto.id_compra = request.json['id_compra']
        self.compra_producto.id_producto = request.json['id_producto']
        self.compra_producto.precio_unitario = request.json['precio_unitario']
        self.compra_producto.cantidad = request.json['cantidad']
        self.compra_producto.usuario_registro = request.json['usuario_registro']

        self.compra_producto.actualizar()
        return {"mensaje": "compra_producto actualizada correctamente"}

    def delete(self, id_compra_producto):
        self.compra_producto.id_compra_producto = id_compra_producto
        self.compra_producto.eliminar()

        return {"mensaje": "compra_producto eliminada correctamente"}


class CompraProductoList(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.compra_producto = CompraProducto()

    def get(self):
        return self.compra_producto.listar()

    def post(self):
        print(f'post {__name__} endpoint; request: {request.json}')
        self.compra_producto.id_compra = request.json['id_compra']
        self.compra_producto.id_producto = request.json['id_producto']
        self.compra_producto.precio_unitario = request.json['precio_unitario']
        self.compra_producto.cantidad = request.json['cantidad']
        self.compra_producto.usuario_registro = request.json['usuario_registro']

        self.compra_producto.insertar()
        return {"mensaje": "compra_producto agregada correctamente"}, 201
