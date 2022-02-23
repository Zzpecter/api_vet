from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from vet_api_rest.models import Usuario


class UserResource(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.usuario = Usuario()

    def get(self, id_entidad):
        self.usuario.id_entidad = id_entidad
        usuario = self.usuario.seleccionar()
        print(usuario.json)
        return usuario

    def put(self, id_entidad):
        self.usuario.id_entidad = id_entidad
        print(f'put user endpoint; request: {request.json}')

        self.usuario.id_nivel = request.json['id_nivel']
        self.usuario.login_usuario = request.json['login_usuario']
        self.usuario.password_usuario = request.json['password_usuario']
        self.usuario.usuario_registro = request.json['usuario_registro']

        self.usuario.actualizar()
        return {"mensaje": "usuario actualizado correctamente"}

    def delete(self, id_entidad):
        self.usuario.id_entidad = id_entidad
        self.usuario.eliminar()

        return {"mensaje": "usuario eliminado correctamente"}


class UserList(Resource):
    """Creation and get_all
    """

    method_decorators = [jwt_required()]

    def __init__(self):
        self.usuario = Usuario()

    def get(self):
        return self.usuario.listar()

    def post(self):
        print(f'post user endpoint; request: {request.json}')
        self.usuario.id_entidad = request.json['id_entidad']
        self.usuario.id_nivel = request.json['id_nivel']
        self.usuario.login_usuario = request.json['login_usuario']
        self.usuario.password_usuario = request.json['password_usuario']
        self.usuario.usuario_registro = request.json['usuario_registro']

        self.usuario.insertar()
        return {"mensaje": "usuario agregado correctamente"}, 201
