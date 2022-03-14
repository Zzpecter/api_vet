from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from vet_api_rest.models import AlmacenMedicamentos


class AlmacenMedicamentosResource(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.almacen_medicamentos = AlmacenMedicamentos()

    def get(self, id_almacen_medicamentos):
        self.almacen_medicamentos.id_almacen_medicamentos = id_almacen_medicamentos
        almacen_medicamentos = self.almacen_medicamentos.seleccionar()
        print(almacen_medicamentos.json)
        return almacen_medicamentos

    def put(self, id_almacen_medicamentos):
        self.almacen_medicamentos.id_almacen_medicamentos = id_almacen_medicamentos
        print(f'put @{__name__} endpoint, request: {request.json}')

        self.almacen_medicamentos.nombre_almacen = request.json['nombre_almacen']
        self.almacen_medicamentos.usuario_registro = request.json['usuario_registro']

        self.almacen_medicamentos.actualizar()
        return {"mensaje": "almacen_medicamentos actualizado correctamente"}

    def delete(self, id_almacen_medicamentos):
        self.almacen_medicamentos.id_almacen_medicamentos = id_almacen_medicamentos
        self.almacen_medicamentos.eliminar()

        return {"mensaje": "almacen_medicamentos eliminado correctamente"}


class AlmacenMedicamentosList(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.almacen_medicamentos = AlmacenMedicamentos()

    def get(self):
        return self.almacen_medicamentos.listar()

    def post(self):
        print(f'post @{__name__} endpoint, request: {request.json}')
        self.almacen_medicamentos.nombre_almacen = request.json['nombre_almacen']
        self.almacen_medicamentos.usuario_registro = request.json['usuario_registro']

        self.almacen_medicamentos.insertar()
        return {"mensaje": "almacen_medicamentos agregado correctamente"}, 201
