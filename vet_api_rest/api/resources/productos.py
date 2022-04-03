from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from vet_api_rest.models import Productos


class ProductoResource(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.producto = Productos()

    def get(self, id_producto):
        self.producto.id_producto = id_producto
        producto = self.producto.seleccionar()
        print(producto.json)
        return producto

    def put(self, id_producto):
        self.producto.id_producto = id_producto
        print(f'put {__name__} endpoint; request: {request.json}')

        self.producto.id_categoria_producto = request.json['id_categoria_producto']
        self.producto.nombre_producto = request.json['nombre_producto']
        self.producto.codigo_producto = request.json['codigo_producto']
        self.producto.precio_compra = request.json['precio_compra']
        self.producto.precio_venta = request.json['precio_venta']
        self.producto.usuario_registro = request.json['usuario_registro']

        self.producto.actualizar()
        return {"mensaje": "producto actualizada correctamente"}

    def delete(self, id_producto):
        self.producto.id_producto = id_producto
        self.producto.eliminar()

        return {"mensaje": "producto eliminada correctamente"}


class ProductoList(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.producto = Productos()

    def get(self):
        return self.producto.listar()

    def post(self):
        print(f'post {__name__} endpoint; request: {request.json}')
        self.producto.id_categoria_producto = request.json['id_categoria_producto']
        self.producto.nombre_producto = request.json['nombre_producto']
        self.producto.codigo_producto = request.json['codigo_producto']
        self.producto.precio_compra = request.json['precio_compra']
        self.producto.precio_venta = request.json['precio_venta']
        self.producto.usuario_registro = request.json['usuario_registro']

        self.producto.insertar()
        return {"mensaje": "producto agregada correctamente"}, 201
