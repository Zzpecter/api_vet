from vet_api_rest.extensions import db


class Entidad:

    def __init__(self, id_entidad=None):
        self.id_entidad = id_entidad
        self.connection = db.connect()
        self.cursor = self.connection.cursor()

    def insertar(self):
        sql_query = f"INSERT INTO entidad (id_entidad) VALUES " \
                    f"({self.id_entidad})"
        print(f'sending query to mySQL: {sql_query}')
        print(sql_query)
        self.cursor.execute(sql_query)
        self.connection.commit()

    def eliminar(self):
        sql_query = f"UPDATE entidad SET es_registro_activo = 0 WHERE id_entidad = {self.id_entidad}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        self.connection.commit()

