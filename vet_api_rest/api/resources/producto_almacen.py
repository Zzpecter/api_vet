from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from vet_api_rest.models import ProductoAlmacen


class ProductoAlmacenResource(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.producto_almacen = ProductoAlmacen()

    def get(self, id_producto_almacen):
        self.producto_almacen.id_producto_almacen = id_producto_almacen
        producto_almacen = self.producto_almacen.seleccionar()
        print(producto_almacen.json)
        return producto_almacen

    def put(self, id_producto_almacen):
        self.producto_almacen.id_producto_almacen = id_producto_almacen
        print(f'put {__name__} endpoint; request: {request.json}')

        self.producto_almacen.id_producto = request.json['id_producto']
        self.producto_almacen.id_almacen = request.json['id_almacen']
        self.producto_almacen.stock_actual = request.json['stock_actual']
        self.producto_almacen.usuario_registro = request.json['usuario_registro']

        self.producto_almacen.actualizar()
        return {"mensaje": "producto_almacen actualizada correctamente"}

    def delete(self, id_producto_almacen):
        self.producto_almacen.id_producto_almacen = id_producto_almacen
        self.producto_almacen.eliminar()

        return {"mensaje": "producto_almacen eliminada correctamente"}


class ProductoAlmacenList(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.producto_almacen = ProductoAlmacen()

    def get(self):
        return self.producto_almacen.listar()

    def post(self):
        print(f'post {__name__} endpoint; request: {request.json}')
        self.producto_almacen.id_producto = request.json['id_producto']
        self.producto_almacen.id_almacen = request.json['id_almacen']
        self.producto_almacen.stock_actual = request.json['stock_actual']
        self.producto_almacen.usuario_registro = request.json['usuario_registro']

        self.producto_almacen.insertar()
        return {"mensaje": "producto_almacen agregada correctamente"}, 201
