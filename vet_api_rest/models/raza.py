from flask import jsonify
from vet_api_rest.extensions import db


class Raza:

    def __init__(self, id_raza=None, id_tipo_mascota=None, nombre_raza=None, usuario_registro=None,
                 fecha_registro=None, es_registro_activo=None):
        self.id_raza = id_raza
        self.id_tipo_mascota = id_tipo_mascota
        self.nombre_raza = nombre_raza
        self.usuario_registro = usuario_registro
        self.fecha_registro = fecha_registro
        self.es_registro_activo = es_registro_activo

        self.connection = db.connect()
        self.cursor = self.connection.cursor()

    def listar(self):
        sql_query = 'SELECT * FROM vi_raza'
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)

        all = self.cursor.fetchall()
        if len(all) > 0:
            r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in all][0]
            print(f'response from mySQL: {r}')
            return jsonify(r)
        return jsonify({"message": "raza no encontrada"})

    def seleccionar(self):
        sql_query = f"SELECT * FROM vi_raza WHERE id_raza = {self.id_raza}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)

        all = self.cursor.fetchall()
        if len(all) > 0:
            r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in all][0]
            print(f'response from mySQL: {r}')
            return jsonify(r)
        return jsonify({"message": "raza no encontrada"})

    def insertar(self):
        sql_query = f"INSERT INTO raza (id_tipo_mascota, nombre_raza, usuario_registro) VALUES " \
                    f"({self.id_tipo_mascota}, '{self.nombre_raza}', '{self.usuario_registro}')"
        print(f'sending query to mySQL: {sql_query}')
        print(sql_query)
        self.cursor.execute(sql_query)
        self.connection.commit()

    def actualizar(self):
        sql_query = f"UPDATE razas SET id_tipo_mascota = {self.id_tipo_mascota}, nombre_raza = {self.nombre_raza}, " \
                    f"usuario_registro = '{self.usuario_registro}' WHERE id_raza = {self.id_raza}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        self.connection.commit()

    def eliminar(self):
        sql_query = f"UPDATE razas SET es_registro_activo = 0 WHERE id_raza = {self.id_raza}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        self.connection.commit()

