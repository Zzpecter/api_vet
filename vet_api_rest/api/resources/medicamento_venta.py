from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from vet_api_rest.models import MedicamentoVenta


class MedicamentoVentaResource(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.medicamento_venta = MedicamentoVenta()

    def get(self, id_medicamento_venta):
        self.medicamento_venta.id_medicamento_venta = id_medicamento_venta
        medicamento_venta = self.medicamento_venta.seleccionar()
        print(medicamento_venta.json)
        return medicamento_venta

    def put(self, id_medicamento_venta):
        self.medicamento_venta.id_medicamento_venta = id_medicamento_venta
        print(f'put {__name__} endpoint; request: {request.json}')

        self.medicamento_venta.id_medicamento = request.json['id_medicamento']
        self.medicamento_venta.id_venta = request.json['id_venta']
        self.medicamento_venta.precio_unitario = request.json['precio_unitario']
        self.medicamento_venta.cantidad = request.json['cantidad']
        self.medicamento_venta.usuario_registro = request.json['usuario_registro']

        self.medicamento_venta.actualizar()
        return {"mensaje": "medicamento_venta actualizada correctamente"}

    def delete(self, id_medicamento_venta):
        self.medicamento_venta.id_medicamento_venta = id_medicamento_venta
        self.medicamento_venta.eliminar()

        return {"mensaje": "medicamento_venta eliminada correctamente"}


class MedicamentoVentaList(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.medicamento_venta = MedicamentoVenta()

    def get(self):
        return self.medicamento_venta.listar()

    def post(self):
        print(f'post {__name__} endpoint; request: {request.json}')
        self.medicamento_venta.id_medicamento = request.json['id_medicamento']
        self.medicamento_venta.id_venta = request.json['id_venta']
        self.medicamento_venta.precio_unitario = request.json['precio_unitario']
        self.medicamento_venta.cantidad = request.json['cantidad']
        self.medicamento_venta.usuario_registro = request.json['usuario_registro']

        self.medicamento_venta.insertar()
        return {"mensaje": "medicamento_venta agregada correctamente"}, 201
