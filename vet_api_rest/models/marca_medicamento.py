from flask import jsonify
from vet_api_rest.extensions import db


class MarcaMedicamento():

    def __init__(self, id_marca_medicamento=None, nombre_marca=None, pais_fabricacion=None, usuario_registro=None, 
                 fecha_registro=None, es_registro_activo=None):
        self.id_marca_medicamento = id_marca_medicamento
        self.nombre_marca = nombre_marca
        self.pais_fabricacion = pais_fabricacion
        self.usuario_registro = usuario_registro
        self.fecha_registro = fecha_registro
        self.es_registro_activo = es_registro_activo

        self.connection = db.connect()
        self.cursor = self.connection.cursor()

    def listar(self):
        sql_query = 'SELECT * FROM vi_marca_medicamento'
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)

        all = self.cursor.fetchall()
        if len(all) > 0:
            r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in all][0]
            print(f'response from mySQL: {r}')
            return jsonify(r)
        return jsonify({"message": "marca_medicamento no encontrada"})

    def seleccionar(self):
        sql_query = f"SELECT * FROM vi_marca_medicamento WHERE id_marca_medicamento = {self.id_marca_medicamento}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)

        all = self.cursor.fetchall()
        if len(all) > 0:
            r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in all][0]
            print(f'response from mySQL: {r}')
            return jsonify(r)
        return jsonify({"message": "marca_medicamento no encontrada"})

    def insertar(self):
        sql_query = f"INSERT INTO marca_medicamento (nombre_marca, pais_fabricacion,  usuario_registro) VALUES " \
                    f"('{self.nombre_marca}', '{self.pais_fabricacion}', '{self.usuario_registro}')"
        print(f'sending query to mySQL: {sql_query}')
        print(sql_query)
        self.cursor.execute(sql_query)
        self.connection.commit()

    def actualizar(self):
        sql_query = f"UPDATE marca_medicamento SET nombre_marca = '{self.nombre_marca}', pais_fabricacion = " \
                    f"'{self.pais_fabricacion}', usuario_registro = '{self.usuario_registro}' " \
                    f"WHERE id_marca_medicamento = {self.id_marca_medicamento}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        self.connection.commit()

    def eliminar(self):
        sql_query = f"UPDATE marca_medicamento SET es_registro_activo = 0 WHERE id_marca_medicamento = {self.id_marca_medicamento}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        self.connection.commit()

