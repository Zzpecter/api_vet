from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from vet_api_rest.models import ServicioVenta


class ServicioVentaResource(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.servicio_venta = ServicioVenta()

    def get(self, id_servicio_venta):
        self.servicio_venta.id_servicio_venta = id_servicio_venta
        servicio_venta = self.servicio_venta.seleccionar()
        print(servicio_venta.json)
        return servicio_venta

    def put(self, id_servicio_venta):
        self.servicio_venta.id_servicio_venta = id_servicio_venta
        print(f'put {__name__} endpoint; request: {request.json}')

        self.servicio_venta.id_servicio = request.json['id_servicio']
        self.servicio_venta.id_venta = request.json['id_venta']
        self.servicio_venta.precio_unitario = request.json['precio_unitario']
        self.servicio_venta.cantidad = request.json['cantidad']
        self.servicio_venta.usuario_registro = request.json['usuario_registro']

        self.servicio_venta.actualizar()
        return {"mensaje": "servicio_venta actualizada correctamente"}

    def delete(self, id_servicio_venta):
        self.servicio_venta.id_servicio_venta = id_servicio_venta
        self.servicio_venta.eliminar()

        return {"mensaje": "servicio_venta eliminada correctamente"}


class ServicioVentaList(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.servicio_venta = ServicioVenta()

    def get(self):
        return self.servicio_venta.listar()

    def post(self):
        print(f'post {__name__} endpoint; request: {request.json}')
        self.servicio_venta.id_servicio = request.json['id_servicio']
        self.servicio_venta.id_venta = request.json['id_venta']
        self.servicio_venta.precio_unitario = request.json['precio_unitario']
        self.servicio_venta.cantidad = request.json['cantidad']
        self.servicio_venta.usuario_registro = request.json['usuario_registro']

        self.servicio_venta.insertar()
        return {"mensaje": "servicio_venta agregada correctamente"}, 201
