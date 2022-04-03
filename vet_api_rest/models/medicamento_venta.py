from flask import jsonify
from vet_api_rest.extensions import db


class MedicamentoVenta():

    def __init__(self, id_medicamento_venta=None, id_medicamento=None, id_venta=None, precio_unitario=None, cantidad=None,
                 usuario_registro=None, fecha_registro=None, es_registro_activo=None):
        self.id_medicamento_venta = id_medicamento_venta
        self.id_medicamento = id_medicamento
        self.id_venta = id_venta
        self.precio_unitario = precio_unitario
        self.cantidad = cantidad
        self.usuario_registro = usuario_registro
        self.fecha_registro = fecha_registro
        self.es_registro_activo = es_registro_activo

        self.connection = db.connect()
        self.cursor = self.connection.cursor()

    def listar(self):
        sql_query = 'SELECT * FROM vi_medicamento_venta'
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)

        all = self.cursor.fetchall()
        if len(all) > 0:
            r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in all][0]
            print(f'response from mySQL: {r}')
            return jsonify(r)
        return jsonify({"message": "medicamento_venta no encontrada"})

    def seleccionar(self):
        sql_query = f"SELECT * FROM vi_medicamento_venta WHERE id_medicamento_venta = {self.id_medicamento_venta}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)

        all = self.cursor.fetchall()
        if len(all) > 0:
            r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in all][0]
            print(f'response from mySQL: {r}')
            return jsonify(r)
        return jsonify({"message": "medicamento_venta no encontrada"})

    def insertar(self):
        sql_query = f"INSERT INTO medicamento_venta (id_medicamento, id_venta, precio_unitario, cantidad, usuario_registro) VALUES " \
                    f"({self.id_medicamento}, {self.id_venta}, '{self.precio_unitario}', {self.cantidad}, '{self.usuario_registro}')"
        print(f'sending query to mySQL: {sql_query}')
        print(sql_query)
        self.cursor.execute(sql_query)
        self.connection.commit()

    def actualizar(self):
        sql_query = f"UPDATE medicamento_venta SET id_medicamento = {self.id_medicamento}, id_venta = {self.id_venta}, " \
                    f"precio_unitario = '{self.precio_unitario}', cantidad = {self.cantidad}, usuario_registro = '{self.usuario_registro}' " \
                    f"WHERE id_medicamento_venta = {self.id_medicamento_venta}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        self.connection.commit()

    def eliminar(self):
        sql_query = f"UPDATE medicamento_venta SET es_registro_activo = 0 WHERE id_medicamento_venta = {self.id_medicamento_venta}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        self.connection.commit()

