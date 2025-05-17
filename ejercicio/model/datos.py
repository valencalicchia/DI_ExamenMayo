import mysql.connector
from model.models import PoblacionModel, ActividadModel, EstudianteModel
from model.config import DBConfig

class BaseDAO:
    def __init__(self):
        config = DBConfig.get_config()

        db = config.get("db")
        user = config.get("user")
        psw = config.get("psw")
        port = config.get("port")
        host = config.get("host")

        if not all([db, user, psw, port, host]):
            raise ValueError("Faltan datos de conexión a la BD.")

        self.conn = mysql.connector.connect(
            user=user, password=psw, port=port, host=host, database=db
        )
        self.cursor = self.conn.cursor(dictionary=True)

    def execute_query(self, query, params=None, fetch_one=False):
        self.cursor.execute(query, params or ())
        if query.strip().upper().startswith("SELECT"):
            return self.cursor.fetchone() if fetch_one else self.cursor.fetchall()
        else:
            self.conn.commit()
            return self.cursor.lastrowid

    def close(self):
        self.cursor.close()
        self.conn.close()
        

class PoblacionesDAO(BaseDAO):
    def get(self, poblacion_id):
        query = "SELECT * FROM poblaciones WHERE id_poblacion = %s"
        row = self.execute_query(query, (poblacion_id,), fetch_one=True)
        if row:
            return PoblacionModel(row['id_poblacion'], row['nombre'])
        return None
    
    def get_all(self):
        query = "SELECT * FROM poblaciones"
        rows = self.execute_query(query)
        return [PoblacionModel(row['id_poblacion'], row['nombre']) for row in rows]

class ActividadesDAO(BaseDAO):
    def get(self, actividad_id):
        query = "SELECT * FROM actividades WHERE id_actividad = %s"
        row = self.execute_query(query, (actividad_id,), fetch_one=True)
        if row:
            return ActividadModel(row['id_actividad'], row['nombre'])
        return None
    
    def get_all(self):
        query = "SELECT * FROM actividades"
        rows = self.execute_query(query)
        return [ActividadModel(row['id_actividad'], row['nombre']) for row in rows]

class EstudiantesDAO(BaseDAO):
    def get(self, estudiante_id):
        query = "SELECT * FROM estudiantes WHERE id_estudiante = %s"
        row = self.execute_query(query, (estudiante_id,), fetch_one=True)
        if row:
            return EstudianteModel(
                row['id_estudiante'], row['nombre'], row['apellidos'], row['dni'],
                row['fecha_nacimiento'], row['id_poblacion'], row['distancia_centro'],
                row['modalidad'], row['usuario'], row['tutor'], row['telefono_tutor'],
                row['fecha_registro']
            )
        return None
    
    def get_all(self):
        query = "SELECT * FROM estudiantes"
        rows = self.execute_query(query)
        return [
            EstudianteModel(
                row['id_estudiante'], row['nombre'], row['apellidos'], row['dni'],
                row['fecha_nacimiento'], row['id_poblacion'], row['distancia_centro'],
                row['modalidad'], row['usuario'], row['tutor'], row['telefono_tutor'],
                row['fecha_registro']
            ) for row in rows
        ]

    def create(self, estudiante: EstudianteModel):
        query = """
        INSERT INTO estudiantes 
        (nombre, apellidos, dni, fecha_nacimiento, id_poblacion, distancia_centro, 
         modalidad, usuario, tutor, telefono_tutor)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        estudiante_id = self.execute_query(query, (
            estudiante.nombre, estudiante.apellidos, estudiante.dni, estudiante.fecha_nacimiento,
            estudiante.id_poblacion, estudiante.distancia_centro, estudiante.modalidad,
            estudiante.usuario, estudiante.tutor, estudiante.telefono_tutor
        ))
        return self.get(estudiante_id)

    def update(self, estudiante: EstudianteModel):
        query = """
        UPDATE estudiantes 
        SET nombre = %s, apellidos = %s, dni = %s, fecha_nacimiento = %s, 
            id_poblacion = %s, distancia_centro = %s, modalidad = %s, 
            usuario = %s, tutor = %s, telefono_tutor = %s
        WHERE id_estudiante = %s
        """
        self.execute_query(query, (
            estudiante.nombre, estudiante.apellidos, estudiante.dni, estudiante.fecha_nacimiento,
            estudiante.id_poblacion, estudiante.distancia_centro, estudiante.modalidad,
            estudiante.usuario, estudiante.tutor, estudiante.telefono_tutor, estudiante.id_estudiante
        ))
        return self.get(estudiante.id_estudiante)

    def delete(self, estudiante_id):
        query = "DELETE FROM estudiantes WHERE id_estudiante = %s"
        self.execute_query(query, (estudiante_id,))

    def check_dni_exists(self, dni, estudiante_id=None):
        query = "SELECT * FROM estudiantes WHERE dni = %s"
        params = (dni,)
        if estudiante_id:
            query += " AND id_estudiante != %s"
            params = (dni, estudiante_id)
        row = self.execute_query(query, params, fetch_one=True)
        return row is not None

class EstudianteActividadesDAO(BaseDAO):
    def get_by_estudiante(self, estudiante_id):
        query = """
        SELECT ea.*, a.nombre as actividad_nombre 
        FROM estudiante_actividades ea
        JOIN actividades a ON ea.id_actividad = a.id_actividad
        WHERE ea.id_estudiante = %s
        """
        rows = self.execute_query(query, (estudiante_id,))
        return [
            {
                'id_estudiante_actividad': row['id_estudiante_actividad'],
                'id_estudiante': row['id_estudiante'],
                'id_actividad': row['id_actividad'],
                'actividad_nombre': row['actividad_nombre']
            } for row in rows
        ]

    def add_actividad(self, estudiante_id, actividad_id):
        query = """
        INSERT INTO estudiante_actividades (id_estudiante, id_actividad)
        VALUES (%s, %s)
        """
        self.execute_query(query, (estudiante_id, actividad_id))

    def remove_actividad(self, estudiante_actividad_id):
        query = "DELETE FROM estudiante_actividades WHERE id_estudiante_actividad = %s"
        self.execute_query(query, (estudiante_actividad_id,))

    def remove_all_actividades(self, estudiante_id):
        query = "DELETE FROM estudiante_actividades WHERE id_estudiante = %s"
        self.execute_query(query, (estudiante_id,))


class UsuariosDAO(BaseDAO):
    def check_credentials(self, usuario, contrasenia):
        query = "SELECT * FROM usuarios WHERE usuario = %s AND contrasenia = %s"
        row = self.execute_query(query, (usuario, contrasenia), fetch_one=True)
        return row is not None  # Devuelve True si existe el usuario con la contraseña correcta, False si no
