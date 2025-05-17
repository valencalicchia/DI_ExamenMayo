from PySide6.QtWidgets import QAbstractItemView, QDialog, QHeaderView
from PySide6.QtGui import QStandardItem, QStandardItemModel
from PySide6.QtCore import QModelIndex

from view.clientes_ui import Ui_Estudiantes
from model.datos import EstudiantesDAO, PoblacionesDAO
from controller.estudiante_create_edit_controller import EstudianteController
from util.message_box import MessageBox

class EstudiantesController(QDialog):
    """
    Controlador de la interfaz para gestionar estudiantes. Esta clase se encarga de manejar la interacción con la
    UI, los eventos, y la lógica asociada a la gestión de estudiantes.
    """
    
    def __init__(self):
        """
        Constructor de la clase, inicializa la interfaz de usuario y configura los eventos necesarios.
        """
        super().__init__()  # Llama al constructor de la clase base QDialog
        self.ui = Ui_Estudiantes()  # Instancia la UI de los estudiantes
        self.ui.setupUi(self)  # Configura la interfaz de usuario
        self.init_ui()  # Llama al método para inicializar la UI y los eventos

    def init_ui(self):
        """
        Método para configurar la interfaz de usuario y los eventos.
        """
        try:
            self.config_events()  # Configura los eventos de la UI
            self.config_table()  # Configura la tabla de estudiantes
            # self.load_poblaciones()  # Carga las poblaciones en el combobox
        except Exception as e:
            # En caso de error, se muestra un mensaje de error con la descripción
            MessageBox("Error al configurar la UI", "error", str(e)).show()

    def config_events(self):
        """
        Configura los eventos de la interfaz de usuario, como los clics en los botones.
        """
        # Conecta los botones a sus respectivas funciones
        self.ui.vcGridEstudiantes.clicked.connect(self.click_estudiante)  # Evento de clic en la tabla de estudiantes
        self.ui.vcbtnModificar.clicked.connect(lambda: self.open_modal(False))  # Evento de clic en "Modificar"
        self.ui.vcbtnNuevo.clicked.connect(lambda: self.open_modal(True))  # Evento de clic en "Nuevo"
        # self.ui.vcbtnEliminar.clicked.connect(self.eliminar_estudiante)  # Evento de clic en "Eliminar"
        # self.ui.vcbtnBuscar.clicked.connect(self.buscar_estudiantes)  # Evento de clic en "Buscar"
        # self.ui.vccboPoblacion.currentIndexChanged.connect(self.filtrar_por_poblacion)  # Evento de cambio en población

    def load_poblaciones(self):
        """
        Carga las poblaciones en el combobox de filtrado.
        """
        dao_poblaciones = PoblacionesDAO()
        poblaciones = dao_poblaciones.get_all()
        
        self.ui.cboPoblacion.clear()
        self.ui.cboPoblacion.addItem("Todas las poblaciones", 0)
        
        for poblacion in poblaciones:
            self.ui.cboPoblacion.addItem(poblacion.nombre, poblacion.id_poblacion)

    def config_table(self, estudiantes=None):
        """
        Configura la tabla que muestra los estudiantes.
        
        :param estudiantes: Lista opcional de estudiantes a mostrar. Si es None, carga todos los estudiantes.
        """
        self.dao_estudiante = EstudiantesDAO()  # Crea la instancia de acceso a los datos de los estudiantes
        self.estudiante_seleccionado = None  # Inicializa el estudiante seleccionado
        
        headers = ["Nombre", "Apellidos", "DNI", "Población", "Modalidad", "Usuario", "Id"]  # Encabezados

        # Obtiene la lista de estudiantes desde la base de datos si no se proporciona
        if estudiantes is None:
            estudiantes = self.dao_estudiante.get_all()

        # Crea un modelo de tabla con el número de filas y columnas correspondientes
        self.model = QStandardItemModel(len(estudiantes), len(headers))
        self.model.setHorizontalHeaderLabels(headers)  # Configura los encabezados de las columnas

        # Rellena la tabla con los datos de los estudiantes
        for row, estudiante in enumerate(estudiantes):
            poblacion_dao = PoblacionesDAO()
            poblacion = poblacion_dao.get(estudiante.id_poblacion)
            
            self.model.setItem(row, 0, QStandardItem(estudiante.nombre))  # Columna "Nombre"
            self.model.setItem(row, 1, QStandardItem(estudiante.apellidos))  # Columna "Apellidos"
            self.model.setItem(row, 2, QStandardItem(estudiante.dni))  # Columna "DNI"
            self.model.setItem(row, 3, QStandardItem(poblacion.nombre if poblacion else ""))  # Columna "Población"
            self.model.setItem(row, 4, QStandardItem(estudiante.modalidad))  # Columna "Modalidad"
            self.model.setItem(row, 5, QStandardItem(estudiante.usuario))  # Columna "Usuario"
            self.model.setItem(row, 6, QStandardItem(str(estudiante.id_estudiante)))  # Columna "Id" (oculta)

        # Configura el modelo en la tabla de la UI
        self.ui.vcGridEstudiantes.setModel(self.model)
        self.ui.vcGridEstudiantes.setColumnHidden(6, True)  # Oculta la columna de "Id"
        self.ui.vcGridEstudiantes.resizeColumnsToContents()  # Ajusta el tamaño de las columnas
        self.ui.vcGridEstudiantes.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # Estira columnas
        self.ui.vcGridEstudiantes.setSelectionBehavior(QAbstractItemView.SelectRows)  # Permite seleccionar filas
        self.ui.vcGridEstudiantes.setSelectionMode(QAbstractItemView.SingleSelection)  # Selección única
        self.ui.vcGridEstudiantes.setEditTriggers(QAbstractItemView.NoEditTriggers)  # Deshabilita edición

    def open_modal(self, nuevo: bool):
        """
        Abre un modal para la creación o modificación de un estudiante.
        
        :param nuevo: Si es True, abre el modal para crear un nuevo estudiante. 
                     Si es False, abre el modal para modificar el estudiante seleccionado.
        """
        if self.estudiante_seleccionado is not None or nuevo:
            if nuevo:
                self.controlador = EstudianteController(None)
            else:
                self.controlador = EstudianteController(self.estudiante_seleccionado)

            if not isinstance(self.controlador, QDialog):
                raise TypeError("El controlador debe heredar de QDialog para ser modal.")
            
            self.controlador.setModal(True)
            self.controlador.finished.connect(self.config_table)  # Actualiza tabla al cerrar
            self.controlador.exec()
        else:
            MessageBox("Seleccione un estudiante para ver los datos", "warning").show()

    def click_estudiante(self, index: QModelIndex):
        """
        Maneja el evento de clic en una fila de la tabla de estudiantes.
        
        :param index: Índice de la fila clickeada en la tabla.
        """
        row = index.row()
        estudiante_id_item = self.model.item(row, 6)  # Obtiene el valor de la columna "Id" (oculta)

        if estudiante_id_item:
            self.estudiante_seleccionado = int(estudiante_id_item.text()) if estudiante_id_item.text() else None

    def eliminar_estudiante(self):
        """
        Elimina el estudiante seleccionado de la base de datos.
        """
        if self.estudiante_seleccionado:
            confirmacion = MessageBox(
                "¿Está seguro de eliminar este estudiante?",
                "question",
                "Esta acción no se puede deshacer."
            ).show()
            
            if confirmacion:
                try:
                    self.dao_estudiante.delete(self.estudiante_seleccionado)
                    MessageBox("Estudiante eliminado correctamente", "info").show()
                    self.config_table()  # Actualiza la tabla
                    self.estudiante_seleccionado = None
                except Exception as e:
                    MessageBox("Error al eliminar estudiante", "error", str(e)).show()
        else:
            MessageBox("Seleccione un estudiante para eliminar", "warning").show()

    def buscar_estudiantes(self):
        """
        Busca estudiantes según el texto ingresado en el campo de búsqueda.
        """
        texto_busqueda = self.ui.txtBuscar.text().strip()
        if texto_busqueda:
            estudiantes = self.dao_estudiante.buscar_por_nombre(texto_busqueda)
            self.config_table(estudiantes)
        else:
            self.config_table()

    def filtrar_por_poblacion(self):
        """
        Filtra los estudiantes por la población seleccionada en el combobox.
        """
        poblacion_id = self.ui.cboPoblacion.currentData()
        if poblacion_id and poblacion_id > 0:
            estudiantes = self.dao_estudiante.filtrar_por_poblacion(poblacion_id)
            self.config_table(estudiantes)
        else:
            self.config_table()