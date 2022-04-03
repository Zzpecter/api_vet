from flask import jsonify
from vet_api_rest.extensions import db


class Venta():

    def __init__(self, id_venta=None, id_usuario=None, id_cliente=None, monto_total=None, fecha_hora=None,
                 usuario_registro=None, fecha_registro=None, es_registro_activo=None):
        self.id_venta = id_venta
        self.id_usuario = id_usuario
        self.id_cliente = id_cliente
        self.monto_total = monto_total
        self.fecha_hora = fecha_hora
        self.usuario_registro = usuario_registro
        self.fecha_registro = fecha_registro
        self.es_registro_activo = es_registro_activo

        self.connection = db.connect()
        self.cursor = self.connection.cursor()

    def listar(self):
        sql_query = 'SELECT * FROM vi_venta'
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)

        all = self.cursor.fetchall()
        if len(all) > 0:
            r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in all][0]
            print(f'response from mySQL: {r}')
            return jsonify(r)
        return jsonify({"message": "venta no encontrada"})

    def seleccionar(self):
        sql_query = f"SELECT * FROM vi_venta WHERE id_venta = {self.id_venta}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)

        all = self.cursor.fetchall()
        if len(all) > 0:
            r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in all][0]
            print(f'response from mySQL: {r}')
            return jsonify(r)
        return jsonify({"message": "venta no encontrada"})

    def insertar(self):
        sql_query = f"INSERT INTO venta (id_venta, id_usuario, id_cliente, monto_total, fecha_hora, usuario_registro)" \
                    f" VALUES ({self.id_venta}, {self.id_usuario}, {self.id_cliente}, {self.monto_total}, " \
                    f"'{self.fecha_hora}', '{self.usuario_registro}')"
        print(f'sending query to mySQL: {sql_query}')
        print(sql_query)
        self.cursor.execute(sql_query)
        self.connection.commit()

    def actualizar(self):
        sql_query = f"UPDATE venta SET id_usuario = {self.id_usuario}, id_cliente = {self.id_cliente}, " \
                    f"monto_total = {self.monto_total}, fecha_hora = '{self.fecha_hora}', usuario_registro = " \
                    f"'{self.usuario_registro}' WHERE id_venta = {self.id_venta}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        self.connection.commit()

    def eliminar(self):
        sql_query = f"UPDATE venta SET es_registro_activo = 0 WHERE id_venta = {self.id_venta}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        self.connection.commit()

