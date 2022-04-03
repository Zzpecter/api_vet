from flask import jsonify
from vet_api_rest.extensions import db


class Medicamentos():

    def __init__(self, id_medicamento=None, id_categoria_medicamento=None, id_unidad_contenido=None, id_marca_medicamento=None, contenido_total=None,
                 nombre_medicamento=None, codigo_medicamento=None, precio_compra=None, precio_venta=None,
                 usuario_registro=None, fecha_registro=None, es_registro_activo=None):
        self.id_medicamento = id_medicamento
        self.id_categoria_medicamento = id_categoria_medicamento
        self.id_unidad_contenido = id_unidad_contenido
        self.id_marca_medicamento = id_marca_medicamento
        self.contenido_total = contenido_total
        self.nombre_medicamento = nombre_medicamento
        self.codigo_medicamento = codigo_medicamento
        self.precio_compra = precio_compra
        self.precio_venta = precio_venta
        self.usuario_registro = usuario_registro
        self.fecha_registro = fecha_registro
        self.es_registro_activo = es_registro_activo

        self.connection = db.connect()
        self.cursor = self.connection.cursor()

    def listar(self):
        sql_query = 'SELECT * FROM vi_medicamentos'
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)

        all = self.cursor.fetchall()
        if len(all) > 0:
            r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in all][0]
            print(f'response from mySQL: {r}')
            return jsonify(r)
        return jsonify({"message": "medicamento no encontrado"})

    def seleccionar(self):
        sql_query = f"SELECT * FROM vi_medicamentos WHERE id_medicamento = {self.id_medicamento}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)

        all = self.cursor.fetchall()
        if len(all) > 0:
            r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in all][0]
            print(f'response from mySQL: {r}')
            return jsonify(r)
        return jsonify({"message": "medicamento no encontrado"})

    def insertar(self):
        sql_query = f"INSERT INTO medicamentos (id_categoria_medicamento, id_unidad_contenido, id_marca_medicamento, contenido_total, " \
                    f"nombre_medicamento, codigo_medicamento, precio_compra, precio_venta, usuario_registro) VALUES " \
                    f"({self.id_categoria_medicamento}, {self.id_unidad_contenido}, {self.id_marca_medicamento}, {self.contenido_total}, " \
                    f"'{self.nombre_medicamento}', '{self.codigo_medicamento}', {self.precio_compra}, {self.precio_venta}, " \
                    f"'{self.usuario_registro}')"
        print(f'sending query to mySQL: {sql_query}')
        print(sql_query)
        self.cursor.execute(sql_query)
        self.connection.commit()

    def actualizar(self):
        sql_query = f"UPDATE medicamentos SET id_categoria_medicamento = {self.id_categoria_medicamento}, id_unidad_contenido = {self.id_unidad_contenido}, " \
                    f"id_marca_medicamento = {self.id_marca_medicamento}, contenido_total = {self.contenido_total}, nombre_medicamento = '{self.nombre_medicamento}', " \
                    f"codigo_medicamento = '{self.codigo_medicamento}', precio_compra = {self.precio_compra}, " \
                    f"precio_venta = {self.precio_compra}, usuario_registro = '{self.usuario_registro}' " \
                    f"WHERE id_medicamento = {self.id_medicamento}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        self.connection.commit()

    def eliminar(self):
        sql_query = f"UPDATE medicamentos SET es_registro_activo = 0 WHERE id_medicamento = {self.id_medicamento}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        self.connection.commit()

