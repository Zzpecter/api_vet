from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from vet_api_rest.models import CategoriaMedicamento


class CategoriaMedicamentoResource(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.categoria_medicamento = CategoriaMedicamento()

    def get(self, id_categoria_medicamento):
        self.categoria_medicamento.id_categoria_medicamento = id_categoria_medicamento
        categoria_medicamento = self.categoria_medicamento.seleccionar()
        print(categoria_medicamento.json)
        return categoria_medicamento

    def put(self, id_categoria_medicamento):
        self.categoria_medicamento.id_categoria_medicamento = id_categoria_medicamento
        print(f'put @{__name__} endpoint, request: {request.json}')

        self.categoria_medicamento.nombre_categoria_medicamento = request.json['nombre_categoria_medicamento']
        self.categoria_medicamento.usuario_registro = request.json['usuario_registro']

        self.categoria_medicamento.actualizar()
        return {"mensaje": "categoria_medicamento actualizado correctamente"}

    def delete(self, id_categoria_medicamento):
        self.categoria_medicamento.id_categoria_medicamento = id_categoria_medicamento
        self.categoria_medicamento.eliminar()

        return {"mensaje": "categoria_medicamento eliminado correctamente"}


class CategoriaMedicamentoList(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.categoria_medicamento = CategoriaMedicamento()

    def get(self):
        return self.categoria_medicamento.listar()

    def post(self):
        print(f'post @{__name__} endpoint, request: {request.json}')
        self.categoria_medicamento.nombre_categoria_medicamento = request.json['nombre_categoria_medicamento']
        self.categoria_medicamento.usuario_registro = request.json['usuario_registro']

        self.categoria_medicamento.insertar()
        return {"mensaje": "categoria_medicamento agregado correctamente"}, 201
