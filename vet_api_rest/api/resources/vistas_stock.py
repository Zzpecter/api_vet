from flask_restful import Resource
from flask_jwt_extended import jwt_required
from vet_api_rest.models import VistasStock


class MascotaCompletoResource(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.vista = VistasStock()

    def get(self, column, value):
        vista = self.vista.mascota_completo_seleccionar(column, value)
        print(vista.json)
        return vista


class MascotaCompletoList(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.vista = VistasStock()

    def get(self):
        return self.vista.mascota_completo_listar()
