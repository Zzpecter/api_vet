from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from vet_api_rest.models import TipoContacto


class TipoContactoResource(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.tipo_contacto = TipoContacto()

    def get(self, id_tipo_contacto):
        self.tipo_contacto.id_tipo_contacto = id_tipo_contacto
        tipo_contacto = self.tipo_contacto.seleccionar()
        print(tipo_contacto.json)
        return tipo_contacto

    def put(self, id_tipo_contacto):
        self.tipo_contacto.id_tipo_contacto = id_tipo_contacto
        print(f'put {__name__} endpoint; request: {request.json}')

        self.tipo_contacto.nombre_tipo_contacto = request.json['nombre_tipo_contacto']
        self.tipo_contacto.usuario_registro = request.json['usuario_registro']

        self.tipo_contacto.actualizar()
        return {"mensaje": "tipo_contacto actualizada correctamente"}

    def delete(self, id_tipo_contacto):
        self.tipo_contacto.id_tipo_contacto = id_tipo_contacto
        self.tipo_contacto.eliminar()

        return {"mensaje": "tipo_contacto eliminada correctamente"}


class TipoContactoList(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.tipo_contacto = TipoContacto()

    def get(self):
        return self.tipo_contacto.listar()

    def post(self):
        print(f'post {__name__} endpoint; request: {request.json}')
        self.tipo_contacto.nombre_tipo_contacto = request.json['nombre_tipo_contacto']
        self.tipo_contacto.usuario_registro = request.json['usuario_registro']

        self.tipo_contacto.insertar()
        return {"mensaje": "tipo_contacto agregada correctamente"}, 201
