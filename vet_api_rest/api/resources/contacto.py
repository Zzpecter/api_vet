from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from vet_api_rest.models import Contacto


class ContactoResource(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.contacto = Contacto()

    def get(self, id_contacto):
        self.contacto.id_contacto = id_contacto
        contacto = self.contacto.seleccionar()
        print(contacto.json)
        return contacto

    def put(self, id_contacto):
        self.contacto.id_contacto = id_contacto
        print(f'put {__name__} endpoint; request: {request.json}')

        self.contacto.id_entidad = request.json['id_entidad']
        self.contacto.id_tipo_contacto = request.json['id_tipo_contacto']
        self.contacto.datos_contacto = request.json['datos_contacto']
        self.contacto.usuario_registro = request.json['usuario_registro']

        self.contacto.actualizar()
        return {"mensaje": "contacto actualizada correctamente"}

    def delete(self, id_contacto):
        self.contacto.id_contacto = id_contacto
        self.contacto.eliminar()

        return {"mensaje": "contacto eliminada correctamente"}


class ContactoList(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.contacto = Contacto()

    def get(self):
        return self.contacto.listar()

    def post(self):
        print(f'post {__name__} endpoint; request: {request.json}')
        self.contacto.id_entidad = request.json['id_entidad']
        self.contacto.id_tipo_contacto = request.json['id_tipo_contacto']
        self.contacto.datos_contacto = request.json['datos_contacto']
        self.contacto.usuario_registro = request.json['usuario_registro']

        self.contacto.insertar()
        return {"mensaje": "contacto agregada correctamente"}, 201
