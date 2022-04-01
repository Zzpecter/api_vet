from flask import jsonify
from vet_api_rest.extensions import db


class Compra():

    def __init__(self, id_compra=None, id_usuario=None, id_proveedor=None, monto_total=None, fecha_hora=None,
                 usuario_registro=None, fecha_registro=None, es_registro_activo=None):
        self.id_compra = id_compra
        self.id_usuario = id_usuario
        self.id_proveedor = id_proveedor
        self.monto_total = monto_total
        self.fecha_hora = fecha_hora
        self.usuario_registro = usuario_registro
        self.fecha_registro = fecha_registro
        self.es_registro_activo = es_registro_activo

        self.connection = db.connect()
        self.cursor = self.connection.cursor()

    def listar(self):
        sql_query = 'SELECT * FROM vi_compra'
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)

        all = self.cursor.fetchall()
        if len(all) > 0:
            r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in all][0]
            print(f'response from mySQL: {r}')
            return jsonify(r)
        return jsonify({"message": "compra no encontrada"})

    def seleccionar(self):
        sql_query = f"SELECT * FROM vi_compra WHERE id_compra = {self.id_compra}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)

        all = self.cursor.fetchall()
        if len(all) > 0:
            r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in all][0]
            print(f'response from mySQL: {r}')
            return jsonify(r)
        return jsonify({"message": "compra no encontrada"})

    def insertar(self):
        sql_query = f"INSERT INTO compra (id_compra, id_usuario, id_proveedor, monto_total, fecha_hora, usuario_registro) VALUES " \
                    f"({self.id_compra}, {self.id_usuario}, {self.id_proveedor}, {self.monto_total}, '{self.fecha_hora}', '{self.usuario_registro}')"
        print(f'sending query to mySQL: {sql_query}')
        print(sql_query)
        self.cursor.execute(sql_query)
        self.connection.commit()

    def actualizar(self):
        sql_query = f"UPDATE compra SET id_usuario = {self.id_usuario}, id_proveedor = {self.id_proveedor}, " \
                    f"monto_total = {self.monto_total}, fecha_hora = '{self.fecha_hora}', usuario_registro = '{self.usuario_registro}' " \
                    f"WHERE id_compra = {self.id_compra}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        self.connection.commit()

    def eliminar(self):
        sql_query = f"UPDATE compra SET es_registro_activo = 0 WHERE id_compra = {self.id_compra}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        self.connection.commit()

