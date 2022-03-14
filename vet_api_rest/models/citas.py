from flask import jsonify
from vet_api_rest.extensions import pwd_context, db


class Citas:

    def __init__(self, id_cita=None, id_mascota=None, fecha_hora=None, motivo_cita=None, usuario_registro=None,
                 fecha_registro=None, es_registro_activo=None):
        self.id_cita = id_cita
        self.id_mascota = id_mascota
        self.fecha_hora = fecha_hora
        self.motivo_cita = motivo_cita
        self.usuario_registro = usuario_registro
        self.fecha_registro = fecha_registro
        self.es_registro_activo = es_registro_activo

        self.connection = db.connect()
        self.cursor = self.connection.cursor()

    def listar(self):
        sql_query = 'SELECT * FROM vi_citas'
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        print(description[0] for description in self.cursor.description)
        r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in self.cursor.fetchall()]
        print(f'response from mySQL: {r}')
        return jsonify(r)

    def seleccionar(self):
        sql_query = f"SELECT * FROM vi_citas WHERE id_cita = {self.id_cita}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in self.cursor.fetchall()][0]
        print(f'response from mySQL: {r}')
        return jsonify(r)

    def insertar(self):
        sql_query = f"INSERT INTO citas (id_mascota, fecha_hora, motivo_cita, usuario_registro) VALUES " \
                    f"('{self.id_mascota}', '{self.fecha_hora}', '{self.motivo_cita}', '{self.usuario_registro}')"
        print(f'sending query to mySQL: {sql_query}')
        print(sql_query)
        self.cursor.execute(sql_query)
        self.connection.commit()

    def actualizar(self):
        sql_query = f"UPDATE citas SET id_mascota = '{self.id_mascota}', fecha_hora = '{self.fecha_hora}', " \
                    f"motivo_cita = '{self.motivo_cita}', usuario_registro = '{self.usuario_registro}' " \
                    f"WHERE id_cita = {self.id_cita}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        self.connection.commit()

    def eliminar(self):
        sql_query = f"UPDATE citas SET es_registro_activo = 0 " \
                    f"WHERE id_cita = {self.id_cita}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        self.connection.commit()

