from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from vet_api_rest.models import UnidadContenido


class UnidadContenidoResource(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.unidad_contenido = UnidadContenido()

    def get(self, id_unidad_contenido):
        self.unidad_contenido.id_unidad_contenido = id_unidad_contenido
        unidad_contenido = self.unidad_contenido.seleccionar()
        print(unidad_contenido.json)
        return unidad_contenido

    def put(self, id_unidad_contenido):
        self.unidad_contenido.id_unidad_contenido = id_unidad_contenido
        print(f'put {__name__} endpoint; request: {request.json}')

        self.unidad_contenido.nombre_unidad = request.json['nombre_unidad_contenido']
        self.unidad_contenido.usuario_registro = request.json['usuario_registro']

        self.unidad_contenido.actualizar()
        return {"mensaje": "unidad_contenido actualizada correctamente"}

    def delete(self, id_unidad_contenido):
        self.unidad_contenido.id_unidad_contenido = id_unidad_contenido
        self.unidad_contenido.eliminar()

        return {"mensaje": "unidad_contenido eliminada correctamente"}


class UnidadContenidoList(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.unidad_contenido = UnidadContenido()

    def get(self):
        return self.unidad_contenido.listar()

    def post(self):
        print(f'post {__name__} endpoint; request: {request.json}')
        self.unidad_contenido.nombre_unidad = request.json['nombre_unidad_contenido']
        self.unidad_contenido.usuario_registro = request.json['usuario_registro']

        self.unidad_contenido.insertar()
        return {"mensaje": "unidad_contenido agregada correctamente"}, 201
