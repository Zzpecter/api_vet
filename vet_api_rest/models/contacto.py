from flask import jsonify
from vet_api_rest.extensions import db


class Contacto():

    def __init__(self, id_contacto=None, id_entidad=None, id_tipo_contacto=None, datos_contacto=None,
                 usuario_registro=None, fecha_registro=None, es_registro_activo=None):
        self.id_contacto = id_contacto
        self.id_entidad = id_entidad
        self.id_tipo_contacto = id_tipo_contacto
        self.datos_contacto = datos_contacto
        self.usuario_registro = usuario_registro
        self.fecha_registro = fecha_registro
        self.es_registro_activo = es_registro_activo

        self.connection = db.connect()
        self.cursor = self.connection.cursor()

    def listar(self):
        sql_query = 'SELECT * FROM vi_contacto'
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)

        all = self.cursor.fetchall()
        if len(all) > 0:
            r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in all][0]
            print(f'response from mySQL: {r}')
            return jsonify(r)
        return jsonify({"message": "contacto no encontrada"})

    def seleccionar(self):
        sql_query = f"SELECT * FROM vi_contacto WHERE id_contacto = {self.id_contacto}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)

        all = self.cursor.fetchall()
        if len(all) > 0:
            r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in all][0]
            print(f'response from mySQL: {r}')
            return jsonify(r)
        return jsonify({"message": "contacto no encontrada"})

    def insertar(self):
        sql_query = f"INSERT INTO contacto (id_entidad, id_tipo_contacto, datos_contacto, usuario_registro) VALUES " \
                    f"({self.id_entidad}, {self.id_tipo_contacto}, '{self.datos_contacto}',  '{self.usuario_registro}')"
        print(f'sending query to mySQL: {sql_query}')
        print(sql_query)
        self.cursor.execute(sql_query)
        self.connection.commit()

    def actualizar(self):
        sql_query = f"UPDATE contacto SET id_entidad = {self.id_entidad}, id_tipo_contacto = {self.id_tipo_contacto}, " \
                    f"datos_contacto = '{self.datos_contacto}', usuario_registro = '{self.usuario_registro}' " \
                    f"WHERE id_contacto = {self.id_contacto}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        self.connection.commit()

    def eliminar(self):
        sql_query = f"UPDATE contacto SET es_registro_activo = 0 WHERE id_contacto = {self.id_contacto}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        self.connection.commit()

