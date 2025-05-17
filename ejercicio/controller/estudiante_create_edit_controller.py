from PySide6.QtWidgets import QWidget, QMessageBox
from PySide6.QtCore import QDate
from view.ui_alta_alumnos import Ui_alumnos
import re
from datetime import datetime


class EstudianteController(QWidget):
    """
    Clase encargada de manejar la interfaz de inscripción de estudiantes.
    Proporciona validación de datos y confirma el registro exitoso.
    """

    def __init__(self):
        super().__init__()
        self.ui = Ui_alumnos()
        self.ui.setupUi(self)
        self.config_events()

    def config_events(self):
        """
        Asocia los botones con sus respectivas funciones.
        """

        self.ui.vcRdBtnDist.setChecked(True)

        self.ui.vccboboxPobl.addItem('Guadalajara')
        self.ui.vccboboxPobl.addItem('Marchamalo')
        self.ui.vccboboxPobl.addItem('Yunquera')
        self.ui.vccboboxPobl.addItem('Horche')
        self.ui.vccboboxPobl.addItem('Torija')

        self.ui.vcBtnGuardar.clicked.connect(self.safe_student)
        self.ui.VcBtnCancelar.clicked.connect(self.clear_form)
        self.b_es_menor = True

        self.ui.vcDateEdit.dateChanged.connect(self.fecha_changed)

        self.set_fecha()

    def fecha_changed(self):
        """
        Maneja el cambio de fecha de nacimiento
        """
        self.b_es_menor = self.es_menor_de_edad(self.ui.vcDateEdit.date().toPython())  # Obtiene el tipo de reserva seleccionado
        self.ui.vcLblTlf.setVisible(self.b_es_menor)  
        self.ui.vcTxtTlf.setVisible(self.b_es_menor)  # Desmarca el checkbox por defecto

        self.ui.vcTxtTutor.setVisible(self.b_es_menor)  # Muestra u oculta el spinbox de jornadas si es Congreso
        self.ui.vcLblTutor.setVisible(self.b_es_menor)  # Restablece el valor por defecto a 0


    def set_fecha(self):
        """
        Establece la fecha en el calendario de la UI. Si es edición, establece la fecha de la reserva.
        """

        fecha_hoy = QDate.currentDate()  # Si es nueva reserva, establece la fecha de hoy

        self.ui.vcDateEdit.setDate(fecha_hoy)  # Establece la fecha en el calendario
        self.ui.vcDateEdit.setMaximumDate(fecha_hoy)  # Asegura que la fecha mínima sea hoy
        self.ui.vcDateEdit.setCalendarPopup(True)  # Habilita el popup del calendario
        self.ui.vcDateEdit.setDisplayFormat("yyyy-MM-dd")  # Formato de visualización de la fecha


    def safe_student(self):
        """
        Recolecta y valida los datos del estudiante antes de almacenarlos.
        """        
        nombre = self.ui.vcTxtNombre.text().strip()
        apellidos = self.ui.vcTxtApell.text().strip()
        dni = self.ui.vcTxtDni.text().strip()
        tutor = self.ui.vcTxtTutor.text().strip()
        tlftutor = self.ui.vcTxtTlf.text().strip()
        dis = self.ui.vcspinBoxDist.value()
        poblacion = self.ui.vccboboxPobl.currentText()

        b_prese = self.ui.vcRdBtnPrese.isChecked()
        fecha = self.ui.vcDateEdit.date().toPython()

        actividades = {
            "Danza": self.ui.vcChkBoDanza.isChecked(),
            "Ajedrez": self.ui.vcChkboxAjedrez.isChecked(),
            "Fútbol": self.ui.vcChkBoxFtbol.isChecked()
        }
        seleccionados = [act for act, activo in actividades.items() if activo]

        if not self.check_data(nombre, apellidos, dni, tutor, tlftutor):
            return

        self.crear_usuario(nombre, apellidos)

        self.show_data(nombre, apellidos, dni, fecha, b_prese, poblacion, dis, seleccionados, tutor, tlftutor)

    def check_data(self, nombre, apellido, identificacion, tutor, tlftutor):
        """
        Revisa que no falte información antes de continuar.
        """
        if not (nombre and apellido and identificacion):
            QMessageBox.warning(self, "Error", "Por favor, complete todos los campos requeridos.")
            return False
        
        if self.b_es_menor and not (tutor and tlftutor):
            QMessageBox.warning(self, "Error", "Por favor, complete todos los datos del tutor.")
            return False

        if not (self.validar_dni_nie_nif(self.ui.vcTxtDni.text().strip())):
            QMessageBox.warning(self, "Error", "NIF no válido")
            return False
        return True
    


    def show_data(self, nombre, apellido, identificacion, fecha, b_persencial, poblacion, dis_centro, seleccionados, tutor, tlftutor):
        """
        Muestra un mensaje con la información ingresada.
        """
        mensaje = (
            f"Estudiante: {nombre} {apellido}\n"
            f"NIF: {identificacion}\n"
            f"Usuario: {self.usuario}\n"
            f"Fecha de nacimiento: {fecha}\n"
            f"Población: {poblacion}\n"
            f"Distacia hasta el centro: {dis_centro}\n"
            f"Modalidad: {'A Distancia' if b_persencial else 'Presencial'}\n"
            f"Extraescolaes: {', '.join(seleccionados) if seleccionados else 'Ninguna'}"
        )

          # Si el estudiante es menor de edad, añadir los datos del tutor
        if self.b_es_menor:
            mensaje += (
                f"\n\nTutor: {tutor}\n"
                f"Teléfono del tutor: {tlftutor}"
            )


        QMessageBox.information(self, "Registro Exitoso", mensaje)

    def crear_usuario(self, nombre, apellidos):
        """
        Crear el usuario para el alumno
        """
        # Dividir el apellido por espacios
        partes = apellidos.strip().split()
        
        # Tomar el primer apellido
        apellido = partes[0]
        
        # Crear el nombre de usuario: inicial del nombre + primer apellido
        usuario = nombre[0].lower() + apellido.lower()
        
        # Eliminar posibles espacios extra
        self.usuario = usuario.replace(" ", "")

    def validar_dni_nie_nif(self, nif):

        """
        Comprueba la validez del dni
        """
        nif = nif.upper().strip()  

        # Comprobación de formato para DNI (8 dígitos + letra)
        if re.match(r'^\d{8}[A-Z]$', nif):
            dni = nif[:8]
            letra = nif[-1]
            letras_validas = "TRWAGMYFPDXBNJZSQVHLCKE"  # Letras posibles para el DNI
            letra_correcta = letras_validas[int(dni) % 23]
            if letra == letra_correcta:
                return True
            else:
                return False

        # Comprobación de formato para NIE (Letra + 7 dígitos + letra)
        elif re.match(r'^[XYZ]\d{7}[A-Z]$', nif):
            letra_inicial = nif[0]
            if letra_inicial == 'X':
                dni = '0' + nif[1:8]
            elif letra_inicial == 'Y':
                dni = '1' + nif[1:8]
            else:  # 'Z'
                dni = '2' + nif[1:8]
            
            letra = nif[-1]
            letras_validas = "TRWAGMYFPDXBNJZSQVHLCKE"  # Letras posibles para el DNI
            letra_correcta = letras_validas[int(dni) % 23]
            if letra == letra_correcta:
                return True
            else:
                return False

        # Comprobación de formato para NIF (personas jurídicas, 8 dígitos + letra)
        elif re.match(r'^\d{8}[A-HJ-NP-TV-Z]$', nif):
            # Las letras permitidas para personas jurídicas van de A a H y de J a N, etc.
            return True
        
        return False

    def es_menor_de_edad(self, fecha_nacimiento):
        # La fecha de nacimiento ya es un objeto datetime, así que no es necesario convertirla
        fecha_actual = datetime.now()
        
        # Calculamos la diferencia de años
        edad = fecha_actual.year - fecha_nacimiento.year
        
        # Ajustamos si la persona aún no ha cumplido años este año
        if (fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day):
            edad -= 1
        
        # Comprobamos si tiene 18 años o más
        return edad < 18

    def clear_form(self):
        """
        Vacía los campos de entrada para una nueva inscripción.
        """
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
        self.ui.vcChkBoxFtbol.setChecked(False)
        self.ui.vcChkboxAjedrez.setChecked(False)
