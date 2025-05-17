from PySide6.QtWidgets import QWidget, QMessageBox, QDialog
from PySide6.QtCore import QDate
from view.alta_alumnos_ui import Ui_alumnos
from util.message_box import MessageBox
import re
from datetime import datetime
import re
from model.datos import EstudiantesDAO, PoblacionesDAO, ActividadesDAO, EstudianteActividadesDAO
from model.models import EstudianteModel

class EstudianteController(QDialog):
    """
    Controlador para la ventana de gestión de estudiantes, que permite la creación,
    modificación y visualización de estudiantes.
    """
    def __init__(self, estudiante_id=None):
        """
        Constructor de la clase EstudianteController.

        Parámetros:
        estudiante_id (int): ID del estudiante a editar. Si es None, se crea un nuevo estudiante.
        """
        try:
            super().__init__()
            self.ui = Ui_alumnos()
            self.ui.setupUi(self)
            
            self.init_daos()
            self.config_events()
            self.b_es_menor = True
            
            if estudiante_id:  # Modificación de estudiante existente
                self.estudiante_id = estudiante_id
                self.estudiante = self.dao_estudiantes.get(self.estudiante_id)
                self.es_nuevo = False
                self.en_edicion = False
            else:  # Nuevo estudiante
                self.estudiante_id = None
                self.estudiante = None
                self.es_nuevo = True
                self.en_edicion = True
                self.ui.VcBtnCancelar.setVisible(False)
            
            self.cambiar_modo()
            self.init_ui()

        except Exception as e:
            MessageBox(f"Error al cargar el formulario: {str(e)}", "error").show()

    def init_daos(self):
        """Inicializa los DAOs necesarios"""
        self.dao_estudiantes = EstudiantesDAO()
        self.dao_poblaciones = PoblacionesDAO()
        self.dao_actividades = ActividadesDAO()
        self.dao_estudiante_actividades = EstudianteActividadesDAO()

    def config_events(self):
        """Configura los eventos de los botones"""
        self.ui.vcBtnGuardar.clicked.connect(self.accion_btn_guardar)
        self.ui.VcBtnCancelar.clicked.connect(self.close)
        self.ui.VcBtnCancelar.clicked.connect(self.accion_btn_eliminar)
        self.ui.vcDateEdit.dateChanged.connect(self.fecha_changed)

    def cargar_poblaciones(self):
        """Carga las poblaciones en el combobox"""
        self.ui.vccboboxPobl.clear()
        poblaciones = self.dao_poblaciones.get_all()
        for poblacion in poblaciones:
            self.ui.vccboboxPobl.addItem(poblacion.nombre, poblacion.id_poblacion)

    def cargar_actividades(self):
        """Carga las actividades disponibles"""
        actividades = self.dao_actividades.get_all()
        # Asigna las actividades a los checkboxes correspondientes
        for actividad in actividades:
            if actividad.nombre == "Danza":
                self.ui.vcChkBoDanza.setText(actividad.nombre)
            elif actividad.nombre == "Ajedrez":
                self.ui.vcChkboxAjedrez.setText(actividad.nombre)
            elif actividad.nombre == "Fútbol":
                self.ui.vcChkBoxFtbol.setText(actividad.nombre)

    def fecha_changed(self):
        """Maneja el cambio de fecha de nacimiento"""
        fecha = self.ui.vcDateEdit.date().toPython()
        self.b_es_menor = self.es_menor_de_edad(fecha)
        
        # Mostrar/ocultar campos de tutor según sea menor
        self.ui.vcLblTlf.setVisible(self.b_es_menor)
        self.ui.vcTxtTlf.setVisible(self.b_es_menor)
        self.ui.vcTxtTutor.setVisible(self.b_es_menor)
        self.ui.vcLblTutor.setVisible(self.b_es_menor)

    def es_menor_de_edad(self, fecha_nacimiento):
        """Determina si el estudiante es menor de edad"""
        hoy = datetime.now()
        edad = hoy.year - fecha_nacimiento.year
        if (hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day):
            edad -= 1
        return edad < 18

    def cambiar_modo(self):
        """Cambia entre modo edición y visualización"""
        if not self.en_edicion:  # Modo visualización
            self.ui.vcBtnGuardar.setText("Editar")
            self.ui.VcBtnCancelar.setText("Eliminar")
        else:  # Modo edición
            self.ui.vcBtnGuardar.setText("Guardar")
            self.ui.VcBtnCancelar.setText("Cancelar")

        # Habilitar/deshabilitar campos según el modo
        self.ui.vcTxtNombre.setEnabled(self.en_edicion)
        self.ui.vcTxtApell.setEnabled(self.en_edicion)
        self.ui.vcTxtDni.setEnabled(self.en_edicion)
        self.ui.vcDateEdit.setEnabled(self.en_edicion)
        self.ui.vccboboxPobl.setEnabled(self.en_edicion)
        self.ui.vcspinBoxDist.setEnabled(self.en_edicion)
        self.ui.vcRdBtnPrese.setEnabled(self.en_edicion)
        self.ui.vcRdBtnDist.setEnabled(self.en_edicion)
        self.ui.vcChkBoDanza.setEnabled(self.en_edicion)
        self.ui.vcChkboxAjedrez.setEnabled(self.en_edicion)
        self.ui.vcChkBoxFtbol.setEnabled(self.en_edicion)
        self.ui.vcTxtTutor.setEnabled(self.en_edicion)
        self.ui.vcTxtTlf.setEnabled(self.en_edicion)

    def init_ui(self):
        """Inicializa la interfaz con los datos del estudiante"""
        self.set_fecha()
        self.cargar_poblaciones()
        self.cargar_actividades()
        self.ui.vcRdBtnDist.setChecked(True)
        
        if not self.es_nuevo:
            self.cargar_datos_estudiante()

    def set_fecha(self):
        """Configura el widget de fecha"""
        fecha_hoy = QDate.currentDate()
        self.ui.vcDateEdit.setDate(fecha_hoy)
        self.ui.vcDateEdit.setMaximumDate(fecha_hoy)
        self.ui.vcDateEdit.setCalendarPopup(True)
        self.ui.vcDateEdit.setDisplayFormat("yyyy-MM-dd")

    def cargar_datos_estudiante(self):
        """Carga los datos del estudiante en la interfaz"""
        if self.estudiante:
            self.ui.vcTxtNombre.setText(self.estudiante.nombre)
            self.ui.vcTxtApell.setText(self.estudiante.apellidos)
            self.ui.vcTxtDni.setText(self.estudiante.dni)
            
            fecha_nac = QDate.fromString(str(self.estudiante.fecha_nacimiento), "yyyy-MM-dd")
            self.ui.vcDateEdit.setDate(fecha_nac)
            
            self.ui.vccboboxPobl.setCurrentText(self.dao_poblaciones.get(self.estudiante.id_poblacion).nombre)
            self.ui.vcspinBoxDist.setValue(float(self.estudiante.distancia_centro))
            
            if self.estudiante.modalidad == 'Presencial':
                self.ui.vcRdBtnPrese.setChecked(True)
            else:
                self.ui.vcRdBtnDist.setChecked(True)
            
            if self.estudiante.tutor:
                self.ui.vcTxtTutor.setText(self.estudiante.tutor)
                self.ui.vcTxtTlf.setText(self.estudiante.telefono_tutor)
            
            # Cargar actividades del estudiante
            actividades_estudiante = self.dao_estudiante_actividades.get_by_estudiante(self.estudiante.id_estudiante)
            for actividad in actividades_estudiante:
                if actividad['actividad_nombre'] == "Danza":
                    self.ui.vcChkBoDanza.setChecked(True)
                elif actividad['actividad_nombre'] == "Ajedrez":
                    self.ui.vcChkboxAjedrez.setChecked(True)
                elif actividad['actividad_nombre'] == "Fútbol":
                    self.ui.vcChkBoxFtbol.setChecked(True)

    def accion_btn_guardar(self):
        """Maneja la acción del botón guardar/editar"""
        if self.en_edicion:
            if self.validar_datos():
                self.guardar_estudiante()
                self.en_edicion = False
                self.cambiar_modo()
        else:
            self.en_edicion = True
            self.cambiar_modo()

    def accion_btn_eliminar(self):
        """Maneja la acción del botón eliminar/cancelar"""
        if self.en_edicion:
            self.en_edicion = False
            self.cambiar_modo()
            self.cargar_datos_estudiante()
        else:
            self.eliminar_estudiante()

    def validar_datos(self):
        """Valida los datos del formulario"""
        nombre = self.ui.vcTxtNombre.text().strip()
        apellidos = self.ui.vcTxtApell.text().strip()
        dni = self.ui.vcTxtDni.text().strip()
        tutor = self.ui.vcTxtTutor.text().strip()
        telefono = self.ui.vcTxtTlf.text().strip()

        if not (nombre and apellidos and dni):
            MessageBox("Por favor, complete todos los campos requeridos.", "warning").show()
            return False
        
        if self.b_es_menor and not (tutor and telefono):
            MessageBox("Por favor, complete todos los datos del tutor.", "warning").show()
            return False

        if not self.validar_dni(dni):
            MessageBox("NIF no válido", "warning").show()
            return False
            
        return True

    def validar_dni(self, nif):
        """Valida el formato del DNI/NIE/NIF"""
        # nif = nif.upper().strip()
        
        # # Validación DNI
        # if re.match(r'^\d{8}[A-Z]$', nif):
        #     dni = nif[:8]
        #     letra = nif[-1]
        #     letras_validas = "TRWAGMYFPDXBNJZSQVHLCKE"
        #     return letra == letras_validas[int(dni) % 23]
        
        # # Validación NIE
        # elif re.match(r'^[XYZ]\d{7}[A-Z]$', nif):
        #     letra_inicial = nif[0]
        #     if letra_inicial == 'X':
        #         dni = '0' + nif[1:8]
        #     elif letra_inicial == 'Y':
        #         dni = '1' + nif[1:8]
        #     else:  # 'Z'
        #         dni = '2' + nif[1:8]
        #     letra = nif[-1]
        #     letras_validas = "TRWAGMYFPDXBNJZSQVHLCKE"
        #     return letra == letras_validas[int(dni) % 23]
        
        # # Validación NIF
        # elif re.match(r'^\d{8}[A-HJ-NP-TV-Z]$', nif):
        #     return True
        
        # return False
        return True 

    def crear_usuario(self, nombre, apellidos):
        """Genera un nombre de usuario automático"""
        partes = apellidos.strip().split()
        apellido = partes[0]
        usuario = nombre[0].lower() + apellido.lower()
        return usuario.replace(" ", "")

    def guardar_estudiante(self):
        """Guarda o actualiza el estudiante en la base de datos"""
        nombre = self.ui.vcTxtNombre.text().strip()
        apellidos = self.ui.vcTxtApell.text().strip()
        dni = self.ui.vcTxtDni.text().strip()
        tutor = self.ui.vcTxtTutor.text().strip() if self.b_es_menor else None
        telefono = self.ui.vcTxtTlf.text().strip() if self.b_es_menor else None
        distancia = self.ui.vcspinBoxDist.value()
        poblacion_id = self.ui.vccboboxPobl.currentData()
        modalidad = 'Presencial' if self.ui.vcRdBtnPrese.isChecked() else 'A Distancia'
        fecha_nac = self.ui.vcDateEdit.date().toPython()
        usuario = self.crear_usuario(nombre, apellidos)

        # Obtener actividades seleccionadas
        actividades_seleccionadas = []
        if self.ui.vcChkBoDanza.isChecked():
            actividades_seleccionadas.append("Danza")
        if self.ui.vcChkboxAjedrez.isChecked():
            actividades_seleccionadas.append("Ajedrez")
        if self.ui.vcChkBoxFtbol.isChecked():
            actividades_seleccionadas.append("Fútbol")

        estudiante = EstudianteModel(
            id_estudiante=self.estudiante_id if not self.es_nuevo else None,
            nombre=nombre,
            apellidos=apellidos,
            dni=dni,
            fecha_nacimiento=fecha_nac,
            id_poblacion=poblacion_id,
            distancia_centro=distancia,
            modalidad=modalidad,
            usuario=usuario,
            tutor=tutor,
            telefono_tutor=telefono
        )

        try:
            if self.es_nuevo:
                nuevo_id = self.dao_estudiantes.create(estudiante).id_estudiante
                self.estudiante_id = nuevo_id
                self.es_nuevo = False
                self.ui.VcBtnCancelar.setVisible(True)
            else:
                self.dao_estudiantes.update(estudiante)
            
            # Gestionar actividades
            self.dao_estudiante_actividades.remove_all_actividades(self.estudiante_id)
            actividades = self.dao_actividades.get_all()
            for actividad in actividades_seleccionadas:
                act_id = next(a.id_actividad for a in actividades if a.nombre == actividad)
                self.dao_estudiante_actividades.add_actividad(self.estudiante_id, act_id)
            MessageBox("Estudiante guardado correctamente").show()

        except Exception as e:
            MessageBox(f"No se pudo guardar el estudiante: {str(e)}", "error").show()
            

    def eliminar_estudiante(self):
        """Elimina el estudiante de la base de datos"""
        respuesta = MessageBox("¿Desea eliminar este estudiante? Esto eliminará también toda la información relacionada", "question", buttons=("Yes", "No")).show()

        if respuesta == "Yes":
            # Elimina las reservas y al cliente
            self.dao_estudiante_actividades.remove_all_actividades(self.estudiante_id)
            self.dao_estudiantes.delete(self.estudiante_id)
            respuesta = MessageBox("Estudiante eliminado").show() # Muestra mensaje de éxito
            if respuesta:
                self.accept()  # Cierra la ventana de cliente
                self.close()   

    def clear_form(self):
        """Limpia el formulario"""
        self.ui.vcTxtNombre.clear()
        self.ui.vcTxtApell.clear()
        self.ui.vcTxtDni.clear()
        self.ui.vcTxtTutor.clear()
        self.ui.vcTxtTlf.clear()
        self.set_fecha()
        self.ui.vcspinBoxDist.setValue(0)
        self.ui.vccboboxPobl.setCurrentIndex(0)
        self.ui.vcRdBtnPrese.setChecked(True)
        self.ui.vcRdBtnDist.setChecked(False)
        self.ui.vcChkBoDanza.setChecked(False)
        self.ui.vcChkboxAjedrez.setChecked(False)
        self.ui.vcChkBoxFtbol.setChecked(False)