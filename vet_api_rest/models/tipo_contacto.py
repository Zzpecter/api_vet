from flask import jsonify
from vet_api_rest.extensions import db


class TipoContacto():

    def __init__(self, id_tipo_contacto=None, nombre_tipo_contacto=None, usuario_registro=None,
                 fecha_registro=None, es_registro_activo=None):
        self.id_tipo_contacto = id_tipo_contacto
        self.nombre_tipo_contacto = nombre_tipo_contacto
        self.usuario_registro = usuario_registro
        self.fecha_registro = fecha_registro
        self.es_registro_activo = es_registro_activo

        self.connection = db.connect()
        self.cursor = self.connection.cursor()

    def listar(self):
        sql_query = 'SELECT * FROM vi_tipo_contacto'
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)

        all = self.cursor.fetchall()
        if len(all) > 0:
            r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in all][0]
            print(f'response from mySQL: {r}')
            return jsonify(r)
        return jsonify({"message": "producto no encontrado"})

    def seleccionar(self):
        sql_query = f"SELECT * FROM vi_tipo_contacto WHERE id_tipo_contacto = {self.id_tipo_contacto}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)

        all = self.cursor.fetchall()
        if len(all) > 0:
            r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in all][0]
            print(f'response from mySQL: {r}')
            return jsonify(r)
        return jsonify({"message": "producto no encontrado"})

    def insertar(self):
        sql_query = f"INSERT INTO tipo_contacto (nombre_tipo_contacto, usuario_registro) VALUES " \
                    f"('{self.nombre_tipo_contacto}',  '{self.usuario_registro}')"
        print(f'sending query to mySQL: {sql_query}')
        print(sql_query)
        self.cursor.execute(sql_query)
        self.connection.commit()

    def actualizar(self):
        sql_query = f"UPDATE tipo_contacto SET nombre_tipo_contacto = '{self.nombre_tipo_contacto}', " \
                    f"usuario_registro = '{self.usuario_registro}' WHERE id_tipo_contacto = {self.id_tipo_contacto}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        self.connection.commit()

    def eliminar(self):
        sql_query = f"UPDATE tipo_contacto SET es_registro_activo = 0 WHERE id_tipo_contacto = {self.id_tipo_contacto}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        self.connection.commit()

