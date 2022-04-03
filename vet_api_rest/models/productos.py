from flask import jsonify
from vet_api_rest.extensions import db


class Productos():

    def __init__(self, id_producto=None, id_categoria_producto=None, id_marca_producto=None, nombre_producto=None,
                 codigo_producto=None, precio_compra=None, precio_venta=None, usuario_registro=None,
                 fecha_registro=None, es_registro_activo=None):
        self.id_producto = id_producto
        self.id_categoria_producto = id_categoria_producto
        self.id_marca_producto = id_marca_producto
        self.nombre_producto = nombre_producto
        self.codigo_producto = codigo_producto
        self.precio_compra = precio_compra
        self.precio_venta = precio_venta
        self.usuario_registro = usuario_registro
        self.fecha_registro = fecha_registro
        self.es_registro_activo = es_registro_activo

        self.connection = db.connect()
        self.cursor = self.connection.cursor()

    def listar(self):
        sql_query = 'SELECT * FROM vi_productos'
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)

        all = self.cursor.fetchall()
        if len(all) > 0:
            r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in all][0]
            print(f'response from mySQL: {r}')
            return jsonify(r)
        return jsonify({"message": "producto no encontrado"})

    def seleccionar(self):
        sql_query = f"SELECT * FROM vi_productos WHERE id_producto = {self.id_producto}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)

        all = self.cursor.fetchall()
        if len(all) > 0:
            r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in all][0]
            print(f'response from mySQL: {r}')
            return jsonify(r)
        return jsonify({"message": "producto no encontrado"})

    def insertar(self):
        sql_query = f"INSERT INTO productos (id_categoria_producto, id_marca_producto, nombre_producto, codigo_producto, " \
                    f"nombre_productos, codigo_productos, precio_compra, precio_venta, usuario_registro) VALUES " \
                    f"({self.id_categoria_producto}, {self.id_marca_producto}, '{self.nombre_producto}', '{self.codigo_producto}', " \
                    f"{self.precio_compra}, {self.precio_venta}, '{self.usuario_registro}')"
        print(f'sending query to mySQL: {sql_query}')
        print(sql_query)
        self.cursor.execute(sql_query)
        self.connection.commit()

    def actualizar(self):
        sql_query = f"UPDATE productos SET id_categoria_producto = {self.id_categoria_producto}, id_marca_producto = {self.id_marca_producto}, " \
                    f"nombre_producto = {self.nombre_producto}, codigo_producto = {self.codigo_producto}, " \
                    f"precio_compra = {self.precio_compra}, precio_venta = {self.precio_compra}, " \
                    f"usuario_registro = '{self.usuario_registro}' WHERE id_producto = {self.id_producto}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        self.connection.commit()

    def eliminar(self):
        sql_query = f"UPDATE productos SET es_registro_activo = 0 WHERE id_producto = {self.id_producto}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        self.connection.commit()

