from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from vet_api_rest.models import ProductoVenta


class ProductoVentaResource(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.producto_venta = ProductoVenta()

    def get(self, id_producto_venta):
        self.producto_venta.id_producto_venta = id_producto_venta
        producto_venta = self.producto_venta.seleccionar()
        print(producto_venta.json)
        return producto_venta

    def put(self, id_producto_venta):
        self.producto_venta.id_producto_venta = id_producto_venta
        print(f'put {__name__} endpoint; request: {request.json}')

        self.producto_venta.id_producto = request.json['id_producto']
        self.producto_venta.id_venta = request.json['id_venta']
        self.producto_venta.precio_unitario = request.json['precio_unitario']
        self.producto_venta.cantidad = request.json['cantidad']
        self.producto_venta.usuario_registro = request.json['usuario_registro']

        self.producto_venta.actualizar()
        return {"mensaje": "producto_venta actualizada correctamente"}

    def delete(self, id_producto_venta):
        self.producto_venta.id_producto_venta = id_producto_venta
        self.producto_venta.eliminar()

        return {"mensaje": "producto_venta eliminada correctamente"}


class ProductoVentaList(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.producto_venta = ProductoVenta()

    def get(self):
        return self.producto_venta.listar()

    def post(self):
        print(f'post {__name__} endpoint; request: {request.json}')
        self.producto_venta.id_producto = request.json['id_producto']
        self.producto_venta.id_venta = request.json['id_venta']
        self.producto_venta.precio_unitario = request.json['precio_unitario']
        self.producto_venta.cantidad = request.json['cantidad']
        self.producto_venta.usuario_registro = request.json['usuario_registro']

        self.producto_venta.insertar()
        return {"mensaje": "producto_venta agregada correctamente"}, 201
