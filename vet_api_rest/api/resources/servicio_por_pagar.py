from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from vet_api_rest.models import ServicioPorPagar


class ServicioPorPagarResource(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.servicio_por_pagar = ServicioPorPagar()

    def get(self, id_servicio_por_pagar):
        self.servicio_por_pagar.id_servicio_por_pagar = id_servicio_por_pagar
        servicio_por_pagar = self.servicio_por_pagar.seleccionar()
        print(servicio_por_pagar.json)
        return servicio_por_pagar

    def put(self, id_servicio_por_pagar):
        self.servicio_por_pagar.id_servicio_por_pagar = id_servicio_por_pagar
        print(f'put {__name__} endpoint; request: {request.json}')

        self.servicio_por_pagar.id_servicio = request.json['id_servicio']
        self.servicio_por_pagar.id_cliente = request.json['id_cliente']
        self.servicio_por_pagar.cantidad = request.json['cantidad']
        self.servicio_por_pagar.usuario_registro = request.json['usuario_registro']

        self.servicio_por_pagar.actualizar()
        return {"mensaje": "servicio_por_pagar actualizada correctamente"}

    def delete(self, id_servicio_por_pagar):
        self.servicio_por_pagar.id_servicio_por_pagar = id_servicio_por_pagar
        self.servicio_por_pagar.eliminar()

        return {"mensaje": "servicio_por_pagar eliminada correctamente"}


class ServicioPorPagarList(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.servicio_por_pagar = ServicioPorPagar()

    def get(self):
        return self.servicio_por_pagar.listar()

    def post(self):
        print(f'post {__name__} endpoint; request: {request.json}')
        self.servicio_por_pagar.id_servicio = request.json['id_servicio']
        self.servicio_por_pagar.id_cliente = request.json['id_cliente']
        self.servicio_por_pagar.cantidad = request.json['cantidad']
        self.servicio_por_pagar.usuario_registro = request.json['usuario_registro']

        self.servicio_por_pagar.insertar()
        return {"mensaje": "servicio_por_pagar agregada correctamente"}, 201
