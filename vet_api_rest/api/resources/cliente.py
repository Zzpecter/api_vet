from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from vet_api_rest.models import Cliente


class ClienteResource(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.cliente = Cliente()

    def get(self, id_cliente):
        self.cliente.id_cliente = id_cliente
        cliente = self.cliente.seleccionar()
        print(cliente.json)
        return cliente

    def put(self, id_cliente):
        self.cliente.id_cliente = id_cliente
        print(f'put {__name__} endpoint; request: {request.json}')

        self.cliente.nombre_factura = request.json['nombre_factura']
        self.cliente.nit_ci = request.json['nit_ci']
        self.cliente.nota = request.json['nota']
        self.cliente.usuario_registro = request.json['usuario_registro']

        self.cliente.actualizar()
        return {"mensaje": "cliente actualizado correctamente"}

    def delete(self, id_cliente):
        self.cliente.id_cliente = id_cliente
        self.cliente.eliminar()

        return {"mensaje": "cliente eliminado correctamente"}


class ClienteList(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.cliente = Cliente()

    def get(self):
        return self.cliente.listar()

    def post(self):
        print(f'post {__name__} endpoint; request: {request.json}')
        self.cliente.id_cliente = request.json['id_cliente']
        self.cliente.nombre_factura = request.json['nombre_factura']
        self.cliente.nit_ci = request.json['nit_ci']
        self.cliente.nota = request.json['nota']
        self.cliente.usuario_registro = request.json['usuario_registro']

        self.cliente.insertar()
        return {"mensaje": "cliente agregado correctamente"}, 201
