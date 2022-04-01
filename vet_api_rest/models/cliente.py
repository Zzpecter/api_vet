from flask import jsonify
from vet_api_rest.extensions import  db


class Cliente():

    def __init__(self, id_cliente=None, nombre_factura=None, nit_ci=None, nota=None, usuario_registro=None,
                 fecha_registro=None, es_registro_activo=None):
        self.id_cliente = id_cliente
        self.nombre_factura = nombre_factura
        self.nit_ci = nit_ci
        self.nota = nota
        self.usuario_registro = usuario_registro
        self.fecha_registro = fecha_registro
        self.es_registro_activo = es_registro_activo

        self.connection = db.connect()
        self.cursor = self.connection.cursor()

    def listar(self):
        sql_query = 'SELECT * FROM vi_cliente'
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)

        all = self.cursor.fetchall()
        if len(all) > 0:
            r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in all][0]
            print(f'response from mySQL: {r}')
            return jsonify(r)
        return jsonify({"message": "cliente no encontrado"})

    def seleccionar(self):
        sql_query = f"SELECT * FROM vi_cliente WHERE id_cliente = {self.id_cliente}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)

        all = self.cursor.fetchall()
        if len(all) > 0:
            r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in all][0]
            print(f'response from mySQL: {r}')
            return jsonify(r)
        return jsonify({"message": "cliente no encontrado"})

    def seleccionar_por_nit(self):
        sql_query = f"SELECT * FROM vi_cliente WHERE nit_ci = '{self.nit_ci}'"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)

        all = self.cursor.fetchall()
        if len(all) > 0:
            r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in all][0]
            print(f'response from mySQL: {r}')
            return jsonify(r)
        return jsonify({"message": "cliente no encontrado"})

    def insertar(self):
        sql_query = f"INSERT INTO cliente (id_cliente, nombre_factura, nit_ci, nota, usuario_registro) VALUES " \
                    f"({self.id_cliente}, '{self.nombre_factura}', '{self.nit_ci}', '{self.nota}', '{self.usuario_registro}')"
        print(f'sending query to mySQL: {sql_query}')
        print(sql_query)
        self.cursor.execute(sql_query)
        self.connection.commit()

    def actualizar(self):
        sql_query = f"UPDATE cliente SET nombre_factura = '{self.nombre_factura}', nit_ci = '{self.nit_ci}', " \
                    f"nota = '{self.nota}', usuario_registro = '{self.usuario_registro}' " \
                    f"WHERE id_cliente = {self.id_cliente}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        self.connection.commit()

    def eliminar(self):
        sql_query = f"UPDATE cliente SET es_registro_activo = 0 WHERE id_cliente = {self.id_cliente}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        self.connection.commit()

