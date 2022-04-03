from flask import jsonify
from vet_api_rest.extensions import db


class ServicioPorPagar:

    def __init__(self, id_servicio_por_pagar=None, id_servicio=None, id_cliente=None, cantidad=None,
                 usuario_registro=None, fecha_registro=None, es_registro_activo=None):
        self.id_servicio_por_pagar = id_servicio_por_pagar
        self.id_servicio = id_servicio
        self.id_cliente = id_cliente
        self.cantidad = cantidad
        self.usuario_registro = usuario_registro
        self.fecha_registro = fecha_registro
        self.es_registro_activo = es_registro_activo

        self.connection = db.connect()
        self.cursor = self.connection.cursor()

    def listar(self):
        sql_query = 'SELECT * FROM vi_servicio_por_pagar'
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)

        all = self.cursor.fetchall()
        if len(all) > 0:
            r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in all][0]
            print(f'response from mySQL: {r}')
            return jsonify(r)
        return jsonify({"message": "servicio_por_pagar no encontrada"})

    def seleccionar(self):
        sql_query = f"SELECT * FROM vi_servicio_por_pagar WHERE id_servicio_por_pagar = {self.id_servicio_por_pagar}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)

        all = self.cursor.fetchall()
        if len(all) > 0:
            r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in all][0]
            print(f'response from mySQL: {r}')
            return jsonify(r)
        return jsonify({"message": "servicio_por_pagar no encontrada"})

    def insertar(self):
        sql_query = f"INSERT INTO servicio_por_pagar (id_servicio, id_cliente, cantidad, usuario_registro) VALUES " \
                    f"({self.id_servicio}, {self.id_cliente}, {self.cantidad}, '{self.usuario_registro}')"
        print(f'sending query to mySQL: {sql_query}')
        print(sql_query)
        self.cursor.execute(sql_query)
        self.connection.commit()

    def actualizar(self):
        sql_query = f"UPDATE servicio_por_pagars SET id_servicio = {self.id_servicio}, id_cliente = {self.id_cliente}, " \
                    f"cantidad = {self.cantidad}, usuario_registro = '{self.usuario_registro}' " \
                    f"WHERE id_servicio_por_pagar = {self.id_servicio_por_pagar}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        self.connection.commit()

    def eliminar(self):
        sql_query = f"UPDATE servicio_por_pagars SET es_registro_activo = 0 WHERE id_servicio_por_pagar = {self.id_servicio_por_pagar}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        self.connection.commit()
