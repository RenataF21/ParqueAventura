from app.config.mysqlconnection import connectToMySQL
from datetime import datetime
DATABASE = 'examen2'

class Visita:
    def __init__(self, data):
        self.id_visitas = data['id']
        self.id_usuario = data['id_usuario']
        self.id_parque = data['id_parque']
        self.fecha_visita = data['fecha_visita']
        self.rating = data['rating']
        self.acciones = data['acciones']
        self.usuario_id = data['usuario_id']
        self.parque_id = data['parque_id']
        # Para joins con la tabla usuarios

    @classmethod
    def get_all(cls):
        query = """
            SELECT v.*, p.nombre as parque 
            FROM visitas v
            JOIN parques p ON v.id_parque = p.id_parque
            ORDER BY v.fecha_de_visitas;
        """
        results = connectToMySQL(DATABASE).query_db(query)
        visitas = []
        if results:
            for row in results:
                visitas.append(cls(row))
        return visitas

    @classmethod
    def nueva(cls, data):
        query = """
            INSERT INTO visitas (parque, usuario, fecha_de_visitas, rating, acciones, id_parque, id_usuario)
            VALUES (%(parque)s, (%(usuario)s,  %(fecha_de_visitas)s, %(rating)s, %(acciones)s, %(id_parque)s, %(id_usuario)s);
        """
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def editar(cls, data):
        query = """
            UPDATE visitas 
            SET parque = %(parque)s,
                usuario = %(usuario)%,
                fecha_de_visitas = %(fecha_de_visitas)s,
                rating = %(rating)s,
                acciones = %(acciones)s
            WHERE id_visita = %(id_visita)s;
        """
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def obtener_por_id(cls, id_visita):
        query = """
            SELECT v.*, p.nombre as parque 
            FROM visitas v
            JOIN parques p ON v.id_parque = p.id_parque
            WHERE v.id_visitas = %(id_visita)s;
        """
        data = {'id_visita': id_visita}
        results = connectToMySQL(DATABASE).query_db(query, data)
        return cls(results[0]) if results else None

    @classmethod
    def eliminar(cls, id_visita):
        query1 = "DELETE FROM parques_visitas WHERE id_visitas = %(id_visitas)s;"
        query2 = "DELETE FROM visitas WHERE id_visitas = %(id_visitas)s;"
        data = {'id_visita': id_visita}
        connectToMySQL(DATABASE).query_db(query1, data)
        connectToMySQL(DATABASE).query_db(query2, data)
        return True

    @classmethod
    def obtener_por_parques(cls, id_parque):
        query = """
            SELECT v.*, p.nombre as parque 
            FROM visitas v
            JOIN parques p ON v.id_parque = p.id_parque
            WHERE v.id_parque = %(id_parque)s
            ORDER BY v.fecha_de_visitas;
        """
        data = {'id_parque': id_parque}
        results = connectToMySQL(DATABASE).query_db(query, data)
        visitas = []
        if results:
            for row in results:
                visitas.append(cls(row))
        return visitas

    # Método para validar los datos de la visita
    @staticmethod
    def validar_visita(data):
        errores = []
        
        # Validar que los campos no estén vacíos
        if not data['parque']:
            errores.append("El parque es obligatorio")
        
        if not data['fecha_de_visita']:
            errores.append("La fecha de visita es obligatoria")
            
        if not data['desarrollo']:
            errores.append("El desarrollo es obligatorio")

        # Validar fechas
        fecha_visita = datetime.strptime(data['fecha_de_visita'], '%Y-%m-%dT%H:%M')
        if fecha_visita <= datetime.now():
            errores.append("La fecha de visita debe ser una fecha futura")
            
        return errores