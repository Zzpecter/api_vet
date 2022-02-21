"""Various helpers for auth. Mainly about tokens blocklisting

Heavily inspired by
https://github.com/vimalloc/flask-jwt-extended/blob/master/examples/blocklist_database.py
"""
from datetime import datetime
from flask_jwt_extended import decode_token
from abarrotes_api_rest.extensions import db
from abarrotes_api_rest.models.api_tokens import ApiTokens


def add_token_to_database(encoded_token, identity_claim):
    decoded_token = decode_token(encoded_token)

    db_token = ApiTokens(
        jti=decoded_token["jti"],
        tipo_token=decoded_token["type"],
        id_entidad = decoded_token[identity_claim],
        fecha_expiracion= datetime.fromtimestamp(decoded_token["exp"]),
        activo= False,
    )
    db_token.insertar()


def is_token_revoked(jwt_payload):
    token_finder = ApiTokens(jti=jwt_payload["jti"])
    token = token_finder.seleccionar_por_jti()
    print(f'token from dB: {token}')
    if token:
        return token[0]['activo']
    else:
        return False


def revocar_token(token_jti, user):
    # try:
    #     token = TokenBlocklist.query.filter_by(jti=token_jti, user_id=user).one()
    #     token.revoked = True
    #     db.session.commit()
    # except NoResultFound:
    #     raise Exception("Could not find the token {}".format(token_jti))
    pass
