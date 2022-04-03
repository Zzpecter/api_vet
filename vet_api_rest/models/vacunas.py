from flask import jsonify
from vet_api_rest.extensions import db


class Vacunas:

    def __init__(self, id_vacuna=None, id_mascota=None, id_medicamento=None, fecha_vacuna=None, usuario_registro=None,
                 fecha_registro=None, es_registro_activo=None):
        self.id_vacuna = id_vacuna
        self.id_mascota = id_mascota
        self.id_medicamento = id_medicamento
        self.fecha_vacuna = fecha_vacuna
        self.usuario_registro = usuario_registro
        self.fecha_registro = fecha_registro
        self.es_registro_activo = es_registro_activo

        self.connection = db.connect()
        self.cursor = self.connection.cursor()

    def listar(self):
        sql_query = 'SELECT * FROM vi_vacunas'
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)

        all = self.cursor.fetchall()
        if len(all) > 0:
            r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in all][0]
            print(f'response from mySQL: {r}')
            return jsonify(r)
        return jsonify({"message": "vacunas no encontrada"})

    def seleccionar(self):
        sql_query = f"SELECT * FROM vi_vacunas WHERE id_vacuna = {self.id_vacuna}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)

        all = self.cursor.fetchall()
        if len(all) > 0:
            r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in all][0]
            print(f'response from mySQL: {r}')
            return jsonify(r)
        return jsonify({"message": "vacunas no encontrada"})

    def insertar(self):
        sql_query = f"INSERT INTO vacunas (id_mascota, id_medicamento, fecha_vacuna, usuario_registro) VALUES " \
                    f"({self.id_mascota}, {self.id_medicamento}, '{self.fecha_vacuna}', '{self.usuario_registro}')"
        print(f'sending query to mySQL: {sql_query}')
        print(sql_query)
        self.cursor.execute(sql_query)
        self.connection.commit()

    def actualizar(self):
        sql_query = f"UPDATE vacunas SET id_mascota = {self.id_mascota}, id_medicamento = {self.id_medicamento}, " \
                    f"fecha_vacuna = {self.fecha_vacuna}, usuario_registro = '{self.usuario_registro}' " \
                    f"WHERE id_vacuna = {self.id_vacuna}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        self.connection.commit()

    def eliminar(self):
        sql_query = f"UPDATE vacunas SET es_registro_activo = 0 WHERE id_vacuna = {self.id_vacuna}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        self.connection.commit()

