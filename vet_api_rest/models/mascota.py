from flask import jsonify
from vet_api_rest.extensions import db


class Mascota():

    def __init__(self, id_mascota=None, id_tipo_mascota=None, id_cliente=None, nombre_mascota=None, color=None,
                 sexo_mascota=None, es_reproductor=None, rasgos=None, ref_foto=None,
                 usuario_registro=None, fecha_registro=None, es_registro_activo=None):
        self.id_mascota = id_mascota
        self.id_tipo_mascota = id_tipo_mascota
        self.id_cliente = id_cliente
        self.nombre_mascota = nombre_mascota
        self.color = color
        self.sexo_mascota = sexo_mascota
        self.es_reproductor = es_reproductor
        self.rasgos = rasgos
        self.ref_foto = ref_foto
        self.usuario_registro = usuario_registro
        self.fecha_registro = fecha_registro
        self.es_registro_activo = es_registro_activo

        self.connection = db.connect()
        self.cursor = self.connection.cursor()

    def listar(self):
        sql_query = 'SELECT * FROM vi_mascota'
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)

        all = self.cursor.fetchall()
        if len(all) > 0:
            r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in all][0]
            print(f'response from mySQL: {r}')
            return jsonify(r)
        return jsonify({"message": "mascota no encontrada"})

    def seleccionar(self):
        sql_query = f"SELECT * FROM vi_mascota WHERE id_mascota = {self.id_mascota}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)

        all = self.cursor.fetchall()
        if len(all) > 0:
            r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in all][0]
            print(f'response from mySQL: {r}')
            return jsonify(r)
        return jsonify({"message": "mascota no encontrada"})

    def insertar(self):
        sql_query = f"INSERT INTO mascota (id_tipo_mascota, id_cliente, nombre_mascota, color, sexo_mascota, " \
                    f"es_reproductor, rasgos, ref_foto, usuario_registro) VALUES " \
                    f"({self.id_tipo_mascota}, {self.id_cliente}, '{self.nombre_mascota}', '{self.color}', '{self.sexo_mascota}', " \
                    f"'{self.es_reproductor}', '{self.rasgos}', '{self.ref_foto}', '{self.usuario_registro}')"
        print(f'sending query to mySQL: {sql_query}')
        print(sql_query)
        self.cursor.execute(sql_query)
        self.connection.commit()

    def actualizar(self):
        sql_query = f"UPDATE mascota SET id_tipo_mascota = {self.id_tipo_mascota}, id_cliente = {self.id_cliente}, " \
                    f"nombre_mascota = '{self.nombre_mascota}', color = '{self.color}', sexo_mascota = '{self.sexo_mascota}', " \
                    f"es_reproductor = '{self.es_reproductor}', rasgos = '{self.rasgos}', ref_foto = '{self.ref_foto}', " \
                    f"usuario_registro = '{self.usuario_registro}' WHERE id_mascota = {self.id_mascota}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        self.connection.commit()

    def eliminar(self):
        sql_query = f"UPDATE mascota SET es_registro_activo = 0 WHERE id_mascota = {self.id_mascota}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        self.connection.commit()

