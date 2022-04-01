from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from vet_api_rest.models import CompraMedicamento


class CompraMedicamentoResource(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.compra_medicamento = CompraMedicamento()

    def get(self, id_compra_medicamento):
        self.compra_medicamento.id_compra_medicamento = id_compra_medicamento
        compra_medicamento = self.compra_medicamento.seleccionar()
        print(compra_medicamento.json)
        return compra_medicamento

    def put(self, id_compra_medicamento):
        self.compra_medicamento.id_compra_medicamento = id_compra_medicamento
        print(f'put {__name__} endpoint; request: {request.json}')

        self.compra_medicamento.id_usuario = request.json['id_usuario']
        self.compra_medicamento.id_proveedor = request.json['id_proveedor']
        self.compra_medicamento.monto_total = request.json['monto_total']
        self.compra_medicamento.fecha_hora = request.json['fecha_hora']
        self.compra_medicamento.usuario_registro = request.json['usuario_registro']

        self.compra_medicamento.actualizar()
        return {"mensaje": "compra_medicamento actualizada correctamente"}

    def delete(self, id_compra_medicamento):
        self.compra_medicamento.id_compra_medicamento = id_compra_medicamento
        self.compra_medicamento.eliminar()

        return {"mensaje": "compra_medicamento eliminada correctamente"}


class CompraMedicamentoList(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.compra_medicamento = CompraMedicamento()

    def get(self):
        return self.compra_medicamento.listar()

    def post(self):
        print(f'post {__name__} endpoint; request: {request.json}')
        self.compra_medicamento.id_usuario = request.json['id_usuario']
        self.compra_medicamento.id_proveedor = request.json['id_proveedor']
        self.compra_medicamento.monto_total = request.json['monto_total']
        self.compra_medicamento.fecha_hora = request.json['fecha_hora']
        self.compra_medicamento.usuario_registro = request.json['usuario_registro']

        self.compra_medicamento.insertar()
        return {"mensaje": "compra_medicamento agregada correctamente"}, 201
