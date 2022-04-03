from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from vet_api_rest.models import MarcaMedicamento


class MarcaMedicamentoResource(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.marca_medicamento = MarcaMedicamento()

    def get(self, id_marca_medicamento):
        self.marca_medicamento.id_marca_medicamento = id_marca_medicamento
        marca_medicamento = self.marca_medicamento.seleccionar()
        print(marca_medicamento.json)
        return marca_medicamento

    def put(self, id_marca_medicamento):
        self.marca_medicamento.id_marca_medicamento = id_marca_medicamento
        print(f'put {__name__} endpoint; request: {request.json}')

        self.marca_medicamento.nombre_marca = request.json['nombre_marca']
        self.marca_medicamento.pais_fabricacion = request.json['pais_fabricacion']
        self.marca_medicamento.usuario_registro = request.json['usuario_registro']

        self.marca_medicamento.actualizar()
        return {"mensaje": "marca_medicamento actualizada correctamente"}

    def delete(self, id_marca_medicamento):
        self.marca_medicamento.id_marca_medicamento = id_marca_medicamento
        self.marca_medicamento.eliminar()

        return {"mensaje": "marca_medicamento eliminada correctamente"}


class MarcaMedicamentoList(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.marca_medicamento = MarcaMedicamento()

    def get(self):
        return self.marca_medicamento.listar()

    def post(self):
        print(f'post {__name__} endpoint; request: {request.json}')
        self.marca_medicamento.nombre_marca = request.json['nombre_marca']
        self.marca_medicamento.pais_fabricacion = request.json['pais_fabricacion']
        self.marca_medicamento.usuario_registro = request.json['usuario_registro']

        self.marca_medicamento.insertar()
        return {"mensaje": "marca_medicamento agregada correctamente"}, 201
