from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from vet_api_rest.models import Medicamentos


class MedicamentoResource(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.medicamento = Medicamentos()

    def get(self, id_medicamento):
        self.medicamento.id_medicamento = id_medicamento
        medicamento = self.medicamento.seleccionar()
        print(medicamento.json)
        return medicamento

    def put(self, id_medicamento):
        self.medicamento.id_medicamento = id_medicamento
        print(f'put {__name__} endpoint; request: {request.json}')

        self.medicamento.id_categoria_medicamento = request.json['id_medicamento']
        self.medicamento.id_unidad_contenido = request.json['id_unidad_contenido']
        self.medicamento.contenido_total = request.json['contenido_total']
        self.medicamento.nombre_medicamento = request.json['nombre_medicamento']
        self.medicamento.codigo_medicamento = request.json['codigo_medicamento']
        self.medicamento.precio_compra = request.json['precio_compra']
        self.medicamento.precio_venta = request.json['precio_venta']
        self.medicamento.usuario_registro = request.json['usuario_registro']

        self.medicamento.actualizar()
        return {"mensaje": "medicamento actualizada correctamente"}

    def delete(self, id_medicamento):
        self.medicamento.id_medicamento = id_medicamento
        self.medicamento.eliminar()

        return {"mensaje": "medicamento eliminada correctamente"}


class MedicamentoList(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.medicamento = Medicamentos()

    def get(self):
        return self.medicamento.listar()

    def post(self):
        print(f'post {__name__} endpoint; request: {request.json}')
        self.medicamento.id_categoria_medicamento = request.json['id_medicamento']
        self.medicamento.id_unidad_contenido = request.json['id_unidad_contenido']
        self.medicamento.contenido_total = request.json['contenido_total']
        self.medicamento.nombre_medicamento = request.json['nombre_medicamento']
        self.medicamento.codigo_medicamento = request.json['codigo_medicamento']
        self.medicamento.precio_compra = request.json['precio_compra']
        self.medicamento.precio_venta = request.json['precio_venta']
        self.medicamento.usuario_registro = request.json['usuario_registro']

        self.medicamento.insertar()
        return {"mensaje": "medicamento agregada correctamente"}, 201
