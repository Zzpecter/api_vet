from flask import jsonify
from vet_api_rest.extensions import db


class TratamientosPendientes():

    def __init__(self, id_tratamiento_pendiente=None, id_mascota=None, id_medicamento=None, fecha_tratamiento=None, 
                 fecha_recordatorio=None, comentario=None, mensaje_enviado=None, usuario_registro=None,
                 fecha_registro=None, es_registro_activo=None):
        self.id_tratamiento_pendiente = id_tratamiento_pendiente
        self.id_mascota = id_mascota
        self.id_medicamento = id_medicamento
        self.fecha_tratamiento = fecha_tratamiento
        self.fecha_recordatorio = fecha_recordatorio
        self.comentario = comentario
        self.mensaje_enviado = mensaje_enviado
        self.usuario_registro = usuario_registro
        self.fecha_registro = fecha_registro
        self.es_registro_activo = es_registro_activo

        self.connection = db.connect()
        self.cursor = self.connection.cursor()

    def listar(self):
        sql_query = 'SELECT * FROM vi_tratamientos_pendientes'
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)

        all = self.cursor.fetchall()
        if len(all) > 0:
            r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in all][0]
            print(f'response from mySQL: {r}')
            return jsonify(r)
        return jsonify({"message": "producto no encontrado"})

    def seleccionar(self):
        sql_query = f"SELECT * FROM vi_tratamientos_pendientes WHERE id_tratamiento_pendiente = {self.id_tratamiento_pendiente}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)

        all = self.cursor.fetchall()
        if len(all) > 0:
            r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in all][0]
            print(f'response from mySQL: {r}')
            return jsonify(r)
        return jsonify({"message": "producto no encontrado"})

    def insertar(self):
        sql_query = f"INSERT INTO tratamientos_pendientes (id_mascota, id_medicamento, fecha_tratamiento, " \
                    f"fecha_recordatorio, comentario, mensaje_enviado, usuario_registro) VALUES {self.id_mascota}, " \
                    f"{self.id_medicamento}, '{self.fecha_tratamiento}', '{self.fecha_recordatorio}', " \
                    f"'{self.comentario}', '{self.mensaje_enviado}', '{self.usuario_registro}')"
        print(f'sending query to mySQL: {sql_query}')
        print(sql_query)
        self.cursor.execute(sql_query)
        self.connection.commit()

    def actualizar(self):
        sql_query = f"UPDATE tratamientos_pendientes SET id_mascota = {self.id_mascota}, id_medicamento = " \
                    f"{self.id_medicamento}, fecha_tratamiento = '{self.fecha_tratamiento}', fecha_recordatorio = " \
                    f"'{self.fecha_recordatorio}', comentario = '{self.comentario}', mensaje_enviado = " \
                    f"'{self.mensaje_enviado}' usuario_registro = '{self.usuario_registro}' " \
                    f"WHERE id_tratamiento_pendiente = {self.id_tratamiento_pendiente}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        self.connection.commit()

    def eliminar(self):
        sql_query = f"UPDATE tratamientos_pendientes SET es_registro_activo = 0 WHERE id_tratamiento_pendiente = {self.id_tratamiento_pendiente}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        self.connection.commit()

