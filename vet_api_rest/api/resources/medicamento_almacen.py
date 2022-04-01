from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from vet_api_rest.models import MedicamentoAlmacen


class MedicamentoAlmacenResource(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.medicamento_almacen = MedicamentoAlmacen()

    def get(self, id_medicamento_almacen):
        self.medicamento_almacen.id_medicamento_almacen = id_medicamento_almacen
        medicamento_almacen = self.medicamento_almacen.seleccionar()
        print(medicamento_almacen.json)
        return medicamento_almacen

    def put(self, id_medicamento_almacen):
        self.medicamento_almacen.id_medicamento_almacen = id_medicamento_almacen
        print(f'put {__name__} endpoint; request: {request.json}')

        self.medicamento_almacen.id_medicamento = request.json['id_medicamento']
        self.medicamento_almacen.id_almacen = request.json['id_almacen']
        self.medicamento_almacen.stock_actual = request.json['stock_actual']
        self.medicamento_almacen.usuario_registro = request.json['usuario_registro']

        self.medicamento_almacen.actualizar()
        return {"mensaje": "medicamento_almacen actualizada correctamente"}

    def delete(self, id_medicamento_almacen):
        self.medicamento_almacen.id_medicamento_almacen = id_medicamento_almacen
        self.medicamento_almacen.eliminar()

        return {"mensaje": "medicamento_almacen eliminada correctamente"}


class MedicamentoAlmacenList(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.medicamento_almacen = MedicamentoAlmacen()

    def get(self):
        return self.medicamento_almacen.listar()

    def post(self):
        print(f'post {__name__} endpoint; request: {request.json}')
        self.medicamento_almacen.id_medicamento = request.json['id_medicamento']
        self.medicamento_almacen.id_almacen = request.json['id_almacen']
        self.medicamento_almacen.stock_actual = request.json['stock_actual']
        self.medicamento_almacen.usuario_registro = request.json['usuario_registro']

        self.medicamento_almacen.insertar()
        return {"mensaje": "medicamento_almacen agregada correctamente"}, 201
