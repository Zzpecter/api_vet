from flask import request, jsonify, Blueprint, current_app as app
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    get_jwt_identity,
    get_jwt,
)

from vet_api_rest.models import Usuario
from vet_api_rest.extensions import pwd_context, jwt
from vet_api_rest.auth.helpers import revocar_token, is_token_revoked, add_token_to_database


blueprint = Blueprint("auth", __name__, url_prefix="/auth")


@blueprint.route("/login", methods=["POST"])
def login():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    login_usuario = request.json.get("login_usuario", None)
    password_usuario = request.json.get("password_usuario", None)
    if not login_usuario or not password_usuario:
        return jsonify({"msg": "Missing username or password"}), 400

    usuario = Usuario(login_usuario=login_usuario)
    user = usuario.seleccionar_por_login()[0]
    print(user)
    print(password_usuario)
    print(user['password_usuario'])
    if user is None or not pwd_context.verify(password_usuario, user['password_usuario']):
        return jsonify({"msg": "Bad credentials"}), 400

    access_token = create_access_token(identity=user['id_usuario'])
    refresh_token = create_refresh_token(identity=user['id_usuario'])
    add_token_to_database(access_token, app.config["JWT_IDENTITY_CLAIM"])
    add_token_to_database(refresh_token, app.config["JWT_IDENTITY_CLAIM"])

    ret = {"access_token": access_token, "refresh_token": refresh_token}
    return jsonify(ret), 200


@blueprint.route("/refresh", methods=["POST"])
@jwt_required(refresh=True)
def refresh():
    """Get an access token from a refresh token

    ---
    post:
      tags:
        - auth
      summary: Get an access token
      description: Get an access token by using a refresh token in the `Authorization` header
      responses:
        200:
          content:
            application/json:
              schema:
                type: object
                properties:
                  access_token:
                    type: string
                    example: myaccesstoken
        400:
          description: bad request
        401:
          description: unauthorized
    """
    current_user = get_jwt_identity()
    access_token = create_access_token(identity=current_user)
    ret = {"access_token": access_token}
    add_token_to_database(access_token, app.config["JWT_IDENTITY_CLAIM"])
    return jsonify(ret), 200


@blueprint.route("/revoke_access", methods=["DELETE"])
@jwt_required()
def revoke_access_token():
    """Revoke an access token

    ---
    delete:
      tags:
        - auth
      summary: Revoke an access token
      description: Revoke an access token
      responses:
        200:
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                    example: token revoked
        400:
          description: bad request
        401:
          description: unauthorized
    """
    jti = get_jwt()["jti"]
    user_identity = get_jwt_identity()
    revocar_token(jti, user_identity)
    return jsonify({"message": "token revoked"}), 200


@blueprint.route("/revoke_refresh", methods=["DELETE"])
@jwt_required(refresh=True)
def revoke_refresh_token():
    """Revoke a refresh token, used mainly for logout

    ---
    delete:
      tags:
        - auth
      summary: Revoke a refresh token
      description: Revoke a refresh token, used mainly for logout
      responses:
        200:
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                    example: token revoked
        400:
          description: bad request
        401:
          description: unauthorized
    """
    jti = get_jwt()["jti"]
    user_identity = get_jwt_identity()
    revocar_token(jti, user_identity)
    return jsonify({"message": "token revoked"}), 200


@jwt.user_lookup_loader
def user_loader_callback(jwt_headers, jwt_payload):
    identity = jwt_payload["sub"]
    print(f'jwt.user_lookup_loader . identity: {identity}')
    usuario = Usuario(id_entidad=identity)
    return usuario.seleccionar()


@jwt.token_in_blocklist_loader
def check_if_token_revoked(jwt_headers, jwt_payload):
    return is_token_revoked(jwt_payload)

