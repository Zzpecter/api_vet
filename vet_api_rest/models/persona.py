from flask import jsonify
from vet_api_rest.extensions import db


class Persona:
    def __init__(self, id_persona=None, nombres=None, apellidos=None, apodo=None, usuario_registro=None,
                 fecha_registro=None, es_registro_activo=None):
        self.id_persona = id_persona
        self.apellidos = apellidos
        self.nombres = nombres
        self.apodo = apodo
        self.usuario_registro = usuario_registro
        self.fecha_registro = fecha_registro
        self.es_registro_activo = es_registro_activo

        self.connection = db.connect()
        self.cursor = self.connection.cursor()

    def listar(self):
        sql_query = 'SELECT * FROM vi_persona'
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        print(description[0] for description in self.cursor.description)
        r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in self.cursor.fetchall()]
        print(f'response from mySQL: {r}')
        return jsonify(r)

    def seleccionar(self):
        sql_query = f"SELECT * FROM vi_persona WHERE id_persona = {self.id_persona}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in self.cursor.fetchall()][0]
        print(f'response from mySQL: {r}')
        return jsonify(r)

    def insertar(self):
        sql_query = f"INSERT INTO persona (id_persona, nombres, apellidos, apodo, usuario_registro) VALUES " \
                    f"({self.id_persona}, '{self.nombres}', '{self.apellidos}', '{self.apodo}', '{self.usuario_registro}')"
        print(f'sending query to mySQL: {sql_query}')
        print(sql_query)
        self.cursor.execute(sql_query)
        self.connection.commit()

    def actualizar(self):
        sql_query = f"UPDATE persona SET nombres = '{self.nombres}', apellidos = '{self.apellidos}', " \
                    f"apodo = '{self.apodo}', usuario_registro = '{self.usuario_registro}' " \
                    f"WHERE id_persona = {self.id_persona}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        self.connection.commit()

    def eliminar(self):
        sql_query = f"UPDATE persona SET es_registro_activo = 0 WHERE id_persona = {self.id_persona}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        self.connection.commit()

