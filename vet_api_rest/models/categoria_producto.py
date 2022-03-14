from flask import jsonify
from vet_api_rest.extensions import pwd_context, db


class CategoriaProducto:

    def __init__(self, id_categoria_producto=None, nombre_categoria=None, usuario_registro=None, fecha_registro=None,
                 es_registro_activo=None):
        self.id_categoria_producto = id_categoria_producto
        self.nombre_categoria = nombre_categoria
        self.usuario_registro = usuario_registro
        self.fecha_registro = fecha_registro
        self.es_registro_activo = es_registro_activo

        self.connection = db.connect()
        self.cursor = self.connection.cursor()

    def listar(self):
        sql_query = 'SELECT * FROM vi_categoria_producto'
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        print(description[0] for description in self.cursor.description)
        r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in self.cursor.fetchall()]
        print(f'response from mySQL: {r}')
        return jsonify(r)

    def seleccionar(self):
        sql_query = f"SELECT * FROM vi_categoria_producto WHERE id_categoria_producto = {self.id_categoria_producto}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in self.cursor.fetchall()][0]
        print(f'response from mySQL: {r}')
        return jsonify(r)

    def insertar(self):
        sql_query = f"INSERT INTO categoria_producto (nombre_categoria, usuario_registro) VALUES " \
                    f"('{self.nombre_categoria}', '{self.usuario_registro}')"
        print(f'sending query to mySQL: {sql_query}')
        print(sql_query)
        self.cursor.execute(sql_query)
        self.connection.commit()

    def actualizar(self):
        sql_query = f"UPDATE categoria_producto SET nombre_categoria = '{self.nombre_categoria}', " \
                    f"usuario_registro = '{self.usuario_registro}' " \
                    f"WHERE id_categoria_producto = {self.id_categoria_producto}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        self.connection.commit()

    def eliminar(self):
        sql_query = f"UPDATE categoria_producto SET es_registro_activo = 0 " \
                    f"WHERE id_categoria_producto = {self.id_categoria_producto}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        self.connection.commit()

