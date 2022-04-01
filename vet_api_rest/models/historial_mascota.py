from flask import jsonify
from vet_api_rest.extensions import db


class HistorialMascota():

    def __init__(self, id_historial_mascota=None, id_mascota=None, peso_actual_gr=None, temperatura_c=None,
                 descripcion_cliente=None, diagnostico=None, conclusiones=None, fecha=None,
                 usuario_registro=None, fecha_registro=None, es_registro_activo=None):
        self.id_historial_mascota = id_historial_mascota
        self.id_mascota = id_mascota
        self.peso_actual_gr = peso_actual_gr
        self.temperatura_c = temperatura_c
        self.descripcion_cliente = descripcion_cliente
        self.diagnostico = diagnostico
        self.conclusiones = conclusiones
        self.fecha = fecha
        self.usuario_registro = usuario_registro
        self.fecha_registro = fecha_registro
        self.es_registro_activo = es_registro_activo

        self.connection = db.connect()
        self.cursor = self.connection.cursor()

    def listar(self):
        sql_query = 'SELECT * FROM vi_historial_mascota'
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)

        all = self.cursor.fetchall()
        if len(all) > 0:
            r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in all][0]
            print(f'response from mySQL: {r}')
            return jsonify(r)
        return jsonify({"message": "historial_mascota no encontrada"})

    def seleccionar(self):
        sql_query = f"SELECT * FROM vi_historial_mascota WHERE id_historial_mascota = {self.id_historial_mascota}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)

        all = self.cursor.fetchall()
        if len(all) > 0:
            r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in all][0]
            print(f'response from mySQL: {r}')
            return jsonify(r)
        return jsonify({"message": "historial_mascota no encontrada"})

    def insertar(self):
        sql_query = f"INSERT INTO historial_mascota (id_mascota, peso_actual_gr, temperatura_c, descripcion_cliente, " \
                    f"diagnostico, conclusiones, fecha, usuario_registro) VALUES " \
                    f"({self.id_mascota}, {self.peso_actual_gr}, {self.temperatura_c}, '{self.descripcion_cliente}', " \
                    f"'{self.diagnostico}', '{self.conclusiones}', '{self.fecha}', '{self.usuario_registro}')"
        print(f'sending query to mySQL: {sql_query}')
        print(sql_query)
        self.cursor.execute(sql_query)
        self.connection.commit()

    def actualizar(self):
        sql_query = f"UPDATE historial_mascota SET id_mascota = {self.id_mascota}, peso_actual_gr = {self.peso_actual_gr}, " \
                    f"temperatura_c = {self.temperatura_c}, descripcion_cliente = '{self.descripcion_cliente}', " \
                    f"diagnostico = '{self.diagnostico}', conclusiones = '{self.conclusiones}', fecha = '{self.fecha}', " \
                    f"usuario_registro = '{self.usuario_registro}' WHERE id_historial_mascota = {self.id_historial_mascota}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        self.connection.commit()

    def eliminar(self):
        sql_query = f"UPDATE historial_mascota SET es_registro_activo = 0 WHERE id_historial_mascota = {self.id_historial_mascota}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        self.connection.commit()

