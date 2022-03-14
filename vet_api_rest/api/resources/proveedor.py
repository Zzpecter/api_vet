from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from vet_api_rest.models import Proveedor


class ProveedorResource(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.proveedor = Proveedor()

    def get(self, id_proveedor):
        self.proveedor.id_proveedor = id_proveedor
        proveedor = self.proveedor.seleccionar()
        print(proveedor.json)
        return proveedor

    def put(self, id_proveedor):
        self.proveedor.id_proveedor = id_proveedor
        print(f'put {__name__} endpoint; request: {request.json}')

        self.proveedor.razon_social = request.json['razon_social']
        self.proveedor.nit_ci = request.json['nit_ci']
        self.proveedor.usuario_registro = request.json['usuario_registro']

        self.proveedor.actualizar()
        return {"mensaje": "proveedor actualizado correctamente"}

    def delete(self, id_proveedor):
        self.proveedor.id_proveedor = id_proveedor
        self.proveedor.eliminar()

        return {"mensaje": "proveedor eliminado correctamente"}


class ProveedorList(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.proveedor = Proveedor()

    def get(self):
        return self.proveedor.listar()

    def post(self):
        print(f'post {__name__} endpoint; request: {request.json}')
        self.proveedor.id_proveedor = request.json['id_proveedor']
        self.proveedor.razon_social = request.json['razon_social']
        self.proveedor.nit_ci = request.json['nit_ci']
        self.proveedor.usuario_registro = request.json['usuario_registro']

        self.proveedor.insertar()
        return {"mensaje": "proveedor agregado correctamente"}, 201
