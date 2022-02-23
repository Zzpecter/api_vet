from flask import Blueprint, current_app, jsonify
from flask_restful import Api
from vet_api_rest.api.resources import UserResource, UserList


blueprint = Blueprint("api", __name__, url_prefix="/api/v1")
api = Api(blueprint)


api.add_resource(UserResource, "/users/<int:id_entidad>", endpoint="user_by_id")
api.add_resource(UserList, "/users", endpoint="users")

