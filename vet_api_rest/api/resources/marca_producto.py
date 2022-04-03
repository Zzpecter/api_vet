from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from vet_api_rest.models import MarcaProducto


class MarcaProductoResource(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.marca_producto = MarcaProducto()

    def get(self, id_marca_producto):
        self.marca_producto.id_marca_producto = id_marca_producto
        marca_producto = self.marca_producto.seleccionar()
        print(marca_producto.json)
        return marca_producto

    def put(self, id_marca_producto):
        self.marca_producto.id_marca_producto = id_marca_producto
        print(f'put {__name__} endpoint; request: {request.json}')

        self.marca_producto.nombre_marca = request.json['nombre_marca']
        self.marca_producto.pais_fabricacion = request.json['pais_fabricacion']
        self.marca_producto.usuario_registro = request.json['usuario_registro']

        self.marca_producto.actualizar()
        return {"mensaje": "marca_producto actualizada correctamente"}

    def delete(self, id_marca_producto):
        self.marca_producto.id_marca_producto = id_marca_producto
        self.marca_producto.eliminar()

        return {"mensaje": "marca_producto eliminada correctamente"}


class MarcaProductoList(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.marca_producto = MarcaProducto()

    def get(self):
        return self.marca_producto.listar()

    def post(self):
        print(f'post {__name__} endpoint; request: {request.json}')
        self.marca_producto.nombre_marca = request.json['nombre_marca']
        self.marca_producto.pais_fabricacion = request.json['pais_fabricacion']
        self.marca_producto.usuario_registro = request.json['usuario_registro']

        self.marca_producto.insertar()
        return {"mensaje": "marca_producto agregada correctamente"}, 201
