from flask import jsonify
from vet_api_rest.extensions import pwd_context, db


class Usuario():

    def __init__(self, id_entidad=None, id_nivel=None, login_usuario=None, password_usuario=None, usuario_registro=None,
                 fecha_registro=None, es_registro_activo=None):
        self.id_entidad = id_entidad
        self.id_nivel = id_nivel
        self.login_usuario = login_usuario
        if password_usuario:
            self.password_usuario = pwd_context.hash(password_usuario)
        else:
            self.password_usuario = password_usuario
        self.usuario_registro = usuario_registro
        self.fecha_registro = fecha_registro
        self.es_registro_activo = es_registro_activo

        self.connection = db.connect()
        self.cursor = self.connection.cursor()

    def __repr__(self):
        return f"<Usuario {self.login_usuario}>"

    def listar(self):
        sql_query = 'SELECT * FROM vi_usuario'
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        print(description[0] for description in self.cursor.description)
        r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in self.cursor.fetchall()]
        print(f'response from mySQL: {r}')
        return jsonify(r)

    def seleccionar(self):
        sql_query = f"SELECT * FROM vi_usuario WHERE id_entidad = {self.id_entidad}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in self.cursor.fetchall()][0]
        print(f'response from mySQL: {r}')
        return jsonify(r)

    def seleccionar_por_login(self):
        sql_query = f"SELECT * FROM vi_usuario WHERE login_usuario = '{self.login_usuario}'"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        print(description[0] for description in self.cursor.description)
        r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in self.cursor.fetchall()]
        print(f'response from mySQL: {r}')
        return r

    def insertar(self):
        sql_query = f"INSERT INTO usuario (id_entidad, id_nivel, login_usuario, password_usuario, usuario_registro) VALUES " \
                    f"({self.id_entidad}, {self.id_nivel}, '{self.login_usuario}', '{self.password_usuario}', '{self.usuario_registro}')"
        print(f'sending query to mySQL: {sql_query}')
        print(sql_query)
        self.cursor.execute(sql_query)
        self.connection.commit()

    def actualizar(self):
        sql_query = f"UPDATE usuario SET id_nivel = {self.id_nivel}, login_usuario = '{self.login_usuario}', " \
                    f"password_usuario = '{self.password_usuario}', usuario_registro = '{self.usuario_registro}' " \
                    f"WHERE id_entidad = {self.id_entidad}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        self.connection.commit()

    def eliminar(self):
        sql_query = f"UPDATE usuario SET es_registro_activo = 0 WHERE id_entidad = {self.id_entidad}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        self.connection.commit()

    def validar(self):
        pass
