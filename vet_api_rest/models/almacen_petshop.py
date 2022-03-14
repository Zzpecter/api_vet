from flask import jsonify
from vet_api_rest.extensions import pwd_context, db


class AlmacenPetshop:

    def __init__(self, id_almacen_petshop=None, nombre_almacen=None, usuario_registro=None, fecha_registro=None,
                 es_registro_activo=None):
        self.id_almacen_petshop = id_almacen_petshop
        self.nombre_almacen = nombre_almacen
        self.usuario_registro = usuario_registro
        self.fecha_registro = fecha_registro
        self.es_registro_activo = es_registro_activo

        self.connection = db.connect()
        self.cursor = self.connection.cursor()

    def listar(self):
        sql_query = 'SELECT * FROM vi_almacen_petshop'
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        print(description[0] for description in self.cursor.description)
        r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in self.cursor.fetchall()]
        print(f'response from mySQL: {r}')
        return jsonify(r)

    def seleccionar(self):
        sql_query = f"SELECT * FROM vi_almacen_petshop WHERE id_almacen_petshop = {self.id_almacen_petshop}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in self.cursor.fetchall()][0]
        print(f'response from mySQL: {r}')
        return jsonify(r)

    def insertar(self):
        sql_query = f"INSERT INTO almacen_petshop (nombre_almacen, usuario_registro) VALUES " \
                    f"('{self.nombre_almacen}', '{self.usuario_registro}')"
        print(f'sending query to mySQL: {sql_query}')
        print(sql_query)
        self.cursor.execute(sql_query)
        self.connection.commit()

    def actualizar(self):
        sql_query = f"UPDATE almacen_petshop SET nombre_almacen = '{self.nombre_almacen}', " \
                    f"usuario_registro = '{self.usuario_registro}' " \
                    f"WHERE id_almacen_petshop = {self.id_almacen_petshop}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        self.connection.commit()

    def eliminar(self):
        sql_query = f"UPDATE almacen_petshop SET es_registro_activo = 0 " \
                    f"WHERE id_almacen_petshop = {self.id_almacen_petshop}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        self.connection.commit()

