from datetime import datetime

class EstudianteModel:
    def __init__(self, id_estudiante, nombre, apellidos, dni, fecha_nacimiento, id_poblacion, 
                 distancia_centro, modalidad, usuario, tutor=None, telefono_tutor=None, fecha_registro=None):
        self.id_estudiante = id_estudiante
        self.nombre = nombre
        self.apellidos = apellidos
        self.dni = dni
        self.fecha_nacimiento = fecha_nacimiento
        self.id_poblacion = id_poblacion
        self.distancia_centro = distancia_centro
        self.modalidad = modalidad
        self.usuario = usuario
        self.tutor = tutor
        self.telefono_tutor = telefono_tutor
        self.fecha_registro = fecha_registro
        
    @property
    def es_menor(self):
        hoy = datetime.now()
        edad = hoy.year - self.fecha_nacimiento.year
        if (hoy.month, hoy.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day):
            edad -= 1
        return edad < 18

class PoblacionModel:
    def __init__(self, id_poblacion, nombre):
        self.id_poblacion = id_poblacion
        self.nombre = nombre

class ActividadModel:
    def __init__(self, id_actividad, nombre):
        self.id_actividad = id_actividad
        self.nombre = nombre

class EstudianteActividadModel:
    def __init__(self, id_estudiante_actividad, id_estudiante, id_actividad):
        self.id_estudiante_actividad = id_estudiante_actividad
        self.id_estudiante = id_estudiante
        self.id_actividad = id_actividad

