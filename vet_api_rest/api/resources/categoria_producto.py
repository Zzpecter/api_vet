from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from vet_api_rest.models import CategoriaProducto


class CategoriaProductoResource(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.categoria_producto = CategoriaProducto()

    def get(self, id_categoria_producto):
        self.categoria_producto.id_categoria_producto = id_categoria_producto
        categoria_producto = self.categoria_producto.seleccionar()
        print(categoria_producto.json)
        return categoria_producto

    def put(self, id_categoria_producto):
        self.categoria_producto.id_categoria_producto = id_categoria_producto
        print(f'put @{__name__} endpoint, request: {request.json}')

        self.categoria_producto.nombre_categoria = request.json['nombre_categoria']
        self.categoria_producto.usuario_registro = request.json['usuario_registro']

        self.categoria_producto.actualizar()
        return {"mensaje": "categoria_producto actualizado correctamente"}

    def delete(self, id_categoria_producto):
        self.categoria_producto.id_categoria_producto = id_categoria_producto
        self.categoria_producto.eliminar()

        return {"mensaje": "categoria_producto eliminado correctamente"}


class CategoriaProductoList(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.categoria_producto = CategoriaProducto()

    def get(self):
        return self.categoria_producto.listar()

    def post(self):
        print(f'post @{__name__} endpoint, request: {request.json}')
        self.categoria_producto.nombre_categoria = request.json['nombre_categoria']
        self.categoria_producto.usuario_registro = request.json['usuario_registro']

        self.categoria_producto.insertar()
        return {"mensaje": "categoria_producto agregado correctamente"}, 201
