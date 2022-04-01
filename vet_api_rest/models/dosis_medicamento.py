from flask import jsonify
from vet_api_rest.extensions import db


class DosisMedicamento():

    def __init__(self, id_dosis_medicamento=None, id_medicamento=None, nombre_dosis=None, cantidad_dias_despues=None,
                 usuario_registro=None, fecha_registro=None, es_registro_activo=None):
        self.id_dosis_medicamento = id_dosis_medicamento
        self.id_medicamento = id_medicamento
        self.nombre_dosis = nombre_dosis
        self.cantidad_dias_despues = cantidad_dias_despues
        self.usuario_registro = usuario_registro
        self.fecha_registro = fecha_registro
        self.es_registro_activo = es_registro_activo

        self.connection = db.connect()
        self.cursor = self.connection.cursor()

    def listar(self):
        sql_query = 'SELECT * FROM vi_dosis_medicamento'
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)

        all = self.cursor.fetchall()
        if len(all) > 0:
            r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in all][0]
            print(f'response from mySQL: {r}')
            return jsonify(r)
        return jsonify({"message": "dosis_medicamento no encontrada"})

    def seleccionar(self):
        sql_query = f"SELECT * FROM vi_dosis_medicamento WHERE id_dosis_medicamento = {self.id_dosis_medicamento}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)

        all = self.cursor.fetchall()
        if len(all) > 0:
            r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in all][0]
            print(f'response from mySQL: {r}')
            return jsonify(r)
        return jsonify({"message": "dosis_medicamento no encontrada"})

    def insertar(self):
        sql_query = f"INSERT INTO dosis_medicamento (id_medicamento, nombre_dosis, cantidad_dias_despues, usuario_registro) VALUES " \
                    f"({self.id_medicamento}, '{self.nombre_dosis}', {self.cantidad_dias_despues},  '{self.usuario_registro}')"
        print(f'sending query to mySQL: {sql_query}')
        print(sql_query)
        self.cursor.execute(sql_query)
        self.connection.commit()

    def actualizar(self):
        sql_query = f"UPDATE dosis_medicamento SET id_medicamento = {self.id_medicamento}, nombre_dosis = '{self.nombre_dosis}', " \
                    f"cantidad_dias_despues = {self.cantidad_dias_despues}, usuario_registro = '{self.usuario_registro}' " \
                    f"WHERE id_dosis_medicamento = {self.id_dosis_medicamento}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        self.connection.commit()

    def eliminar(self):
        sql_query = f"UPDATE dosis_medicamento SET es_registro_activo = 0 WHERE id_dosis_medicamento = {self.id_dosis_medicamento}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        self.connection.commit()

