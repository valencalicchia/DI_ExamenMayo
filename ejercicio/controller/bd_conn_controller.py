from PySide6.QtWidgets import QDialog
from model.config import DBConfig
from model.datos import BaseDAO
from util.message_box import MessageBox
from view.conexion_bd_ui import Ui_ConexionBD

class ConexionBDController(QDialog):
    '''
    Clase que se encarga de mostrar el apartado de "Conexion BD" para que el usuario indica a donde apunta la BD con la que va a trabajar
    '''
    def __init__(self):
        super().__init__()
        self.ui = Ui_ConexionBD()
        self.ui.setupUi(self)
        self.ui.vcTxtHost.setText('localhost')
        self.ui.vcTxtPuerto.setText('3307')
        self.ui.vcTxtUsuario.setText('root')
        self.ui.vcTxtContrasenia.setText('root')
        self.ui.vcTxtBD.setText('EXAMEN2DI')

        self.ui.vcbtnConfirmar.clicked.connect(self.save_config)

    def save_config(self):
        """Guarda la configuración y prueba la conexión a la BD."""
        config = {
            "host": self.ui.vcTxtHost.text(),
            "port": int(self.ui.vcTxtPuerto.text()) if self.ui.vcTxtPuerto.text().isdigit() else 3306,
            "user": self.ui.vcTxtUsuario.text(),
            "psw": self.ui.vcTxtContrasenia.text(),
            "db": self.ui.vcTxtBD.text(),
        }

        DBConfig.set_config(config)  # Guarda la configuración en DBConfig

        # Verificar conexión a la base de datos
        try:
            dao = BaseDAO()  # Intenta conectar con la BD
            dao.close()  # Si funciona, cierra la conexión
            MessageBox("Conexión exitosa").show()
            self.accept()  # Cierra el diálogo con éxito
        except Exception as e:
            MessageBox(f"Fallo en la conexión:\n{e}", "error").show()
