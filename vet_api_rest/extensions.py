"""Extensions registry

All extensions here are used as singletons and
initialized in application factory
"""
from flaskext.mysql import MySQL
from passlib.context import CryptContext
from flask_jwt_extended import JWTManager


db = MySQL()
jwt = JWTManager()
pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")
