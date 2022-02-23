from flask import jsonify
from vet_api_rest.extensions import pwd_context, db

class ApiTokens:

    def __init__(self, id_api_tokens=None, id_entidad=None, jti=None, tipo_token=None, fecha_expiracion=None,
                 activo=True):
        self.id_api_tokens = id_api_tokens
        self.id_entidad = id_entidad
        self.jti = jti
        self.tipo_token = tipo_token
        self.fecha_expiracion = fecha_expiracion
        self.activo = int(activo)

        self.connection = db.connect()
        self.cursor = self.connection.cursor()

    # def listar(self):
    #     sql_query = 'SELECT * FROM vi_usuario'
    #     print(f'sending query to mySQL: {sql_query}')
    #     self.cursor.execute(sql_query)
    #     print(description[0] for description in self.cursor.description)
    #     r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in self.cursor.fetchall()]
    #     print(r)
    #     return jsonify(r)
    #
    # def seleccionar(self):
    #     sql_query = f"SELECT * FROM vi_usuario WHERE id_entidad = {self.id_entidad}"
    #     print(f'sending query to mySQL: {sql_query}')
    #     self.cursor.execute(sql_query)
    #     print(description[0] for description in self.cursor.description)
    #     r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in self.cursor.fetchall()]
    #     print(r)
    #     return jsonify(r)
    #
    def seleccionar_por_jti(self):
        sql_query = f"SELECT * FROM api_tokens WHERE jti = '{self.jti}'"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        print(description[0] for description in self.cursor.description)
        r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in self.cursor.fetchall()]
        print(r)
        return r

    def insertar(self):
        sql_query = f"INSERT INTO api_tokens (id_usuario, jti, tipo_token, fecha_expiracion, activo) VALUES " \
                    f"({self.id_entidad}, '{self.jti}', '{self.tipo_token}', '{self.fecha_expiracion}', {self.activo})"
        print(f'sending query to mySQL: {sql_query}')
        print(sql_query)
        self.cursor.execute(sql_query)
        self.connection.commit()

    # def actualizar(self):
    #     sql_query = f"UPDATE usuario SET login_usuario = '{self.login_usuario}', " \
    #                 f"password_usuario = '{self.password_usuario}', usuario_registro = '{self.usuario_registro}' " \
    #                 f"WHERE id_entidad = {self.id_entidad}"
    #     print(f'sending query to mySQL: {sql_query}')
    #     self.cursor.execute(sql_query)
    #     self.connection.commit()
    #
    # def eliminar(self):
    #     sql_query = f"UPDATE usuario SET es_registro_activo = 0 WHERE id_entidad = {self.id_entidad}"
    #     print(f'sending query to mySQL: {sql_query}')
    #     self.cursor.execute(sql_query)
    #     self.connection.commit()
    #
    # def validar(self):
    #     pass
