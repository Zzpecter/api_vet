from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from vet_api_rest.models import AlmacenPetshop


class AlmacenPetshopResource(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.almacen_petshop = AlmacenPetshop()

    def get(self, id_almacen_petshop):
        self.almacen_petshop.id_almacen_petshop = id_almacen_petshop
        almacen_petshop = self.almacen_petshop.seleccionar()
        print(almacen_petshop.json)
        return almacen_petshop

    def put(self, id_almacen_petshop):
        self.almacen_petshop.id_almacen_petshop = id_almacen_petshop
        print(f'put @{__name__} endpoint, request: {request.json}')

        self.almacen_petshop.nombre_almacen = request.json['nombre_almacen']
        self.almacen_petshop.usuario_registro = request.json['usuario_registro']

        self.almacen_petshop.actualizar()
        return {"mensaje": "almacen_petshop actualizado correctamente"}

    def delete(self, id_almacen_petshop):
        self.almacen_petshop.id_almacen_petshop = id_almacen_petshop
        self.almacen_petshop.eliminar()

        return {"mensaje": "almacen_petshop eliminado correctamente"}


class AlmacenPetshopList(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.almacen_petshop = AlmacenPetshop()

    def get(self):
        return self.almacen_petshop.listar()

    def post(self):
        print(f'post @{__name__} endpoint, request: {request.json}')
        self.almacen_petshop.nombre_almacen = request.json['nombre_almacen']
        self.almacen_petshop.usuario_registro = request.json['usuario_registro']

        self.almacen_petshop.insertar()
        return {"mensaje": "almacen_petshop agregado correctamente"}, 201
