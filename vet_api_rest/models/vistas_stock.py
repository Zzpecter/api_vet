from flask import jsonify
from vet_api_rest.extensions import db


class VistasStock:

    def __init__(self):
        self.connection = db.connect()
        self.cursor = self.connection.cursor()

    def mascota_completo_listar(self):
        sql_query = 'SELECT * FROM vi_mascota_completo'
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)

        all = self.cursor.fetchall()
        if len(all) > 0:
            r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in all][0]
            print(f'response from mySQL: {r}')
            return jsonify(r)
        return jsonify({"message": "mascota no encontrada"})

    def mascota_completo_seleccionar(self, column, value):
        sql_query = f"SELECT * FROM vi_mascota_completo WHERE {column} = {value}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)

        all = self.cursor.fetchall()
        if len(all) > 0:
            r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in all][0]
            print(f'response from mySQL: {r}')
            return jsonify(r)
        return jsonify({"message": "mascota no encontrada"})