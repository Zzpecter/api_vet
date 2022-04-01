from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from vet_api_rest.models import DosisMedicamento


class DosisMedicamentoResource(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.dosis_medicamento = DosisMedicamento()

    def get(self, id_dosis_medicamento):
        self.dosis_medicamento.id_dosis_medicamento = id_dosis_medicamento
        dosis_medicamento = self.dosis_medicamento.seleccionar()
        print(dosis_medicamento.json)
        return dosis_medicamento

    def put(self, id_dosis_medicamento):
        self.dosis_medicamento.id_dosis_medicamento = id_dosis_medicamento
        print(f'put {__name__} endpoint; request: {request.json}')

        self.dosis_medicamento.id_medicamento = request.json['id_medicamento']
        self.dosis_medicamento.nombre_dosis = request.json['nombre_dosis']
        self.dosis_medicamento.cantidad_dias_despues = request.json['cantidad_dias_despues']
        self.dosis_medicamento.usuario_registro = request.json['usuario_registro']

        self.dosis_medicamento.actualizar()
        return {"mensaje": "dosis_medicamento actualizada correctamente"}

    def delete(self, id_dosis_medicamento):
        self.dosis_medicamento.id_dosis_medicamento = id_dosis_medicamento
        self.dosis_medicamento.eliminar()

        return {"mensaje": "dosis_medicamento eliminada correctamente"}


class DosisMedicamentoList(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.dosis_medicamento = DosisMedicamento()

    def get(self):
        return self.dosis_medicamento.listar()

    def post(self):
        print(f'post {__name__} endpoint; request: {request.json}')
        self.dosis_medicamento.id_medicamento = request.json['id_medicamento']
        self.dosis_medicamento.nombre_dosis = request.json['nombre_dosis']
        self.dosis_medicamento.cantidad_dias_despues = request.json['cantidad_dias_despues']
        self.dosis_medicamento.usuario_registro = request.json['usuario_registro']

        self.dosis_medicamento.insertar()
        return {"mensaje": "dosis_medicamento agregada correctamente"}, 201
