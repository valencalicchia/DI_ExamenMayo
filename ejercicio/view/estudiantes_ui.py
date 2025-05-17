# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'estudiantes.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QHeaderView,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QTableView, QVBoxLayout, QWidget)

class Ui_Estudiantes(object):
    def setupUi(self, Estudiantes):
        if not Estudiantes.objectName():
            Estudiantes.setObjectName(u"Estudiantes")
        Estudiantes.resize(796, 469)
        self.verticalLayout = QVBoxLayout(Estudiantes)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.vCLblTitulo = QLabel(Estudiantes)
        self.vCLblTitulo.setObjectName(u"vCLblTitulo")
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.vCLblTitulo.setFont(font)
        self.vCLblTitulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.vCLblTitulo)

        self.vcGridEstudiantes = QTableView(Estudiantes)
        self.vcGridEstudiantes.setObjectName(u"vcGridEstudiantes")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vcGridEstudiantes.sizePolicy().hasHeightForWidth())
        self.vcGridEstudiantes.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(14)
        self.vcGridEstudiantes.setFont(font1)

        self.verticalLayout.addWidget(self.vcGridEstudiantes)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.vcbtnNuevo = QPushButton(Estudiantes)
        self.vcbtnNuevo.setObjectName(u"vcbtnNuevo")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.vcbtnNuevo.sizePolicy().hasHeightForWidth())
        self.vcbtnNuevo.setSizePolicy(sizePolicy1)
        self.vcbtnNuevo.setMinimumSize(QSize(100, 40))
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        self.vcbtnNuevo.setFont(font2)

        self.horizontalLayout.addWidget(self.vcbtnNuevo)

        self.vcbtnModificar = QPushButton(Estudiantes)
        self.vcbtnModificar.setObjectName(u"vcbtnModificar")
        sizePolicy1.setHeightForWidth(self.vcbtnModificar.sizePolicy().hasHeightForWidth())
        self.vcbtnModificar.setSizePolicy(sizePolicy1)
        self.vcbtnModificar.setMinimumSize(QSize(100, 40))
        self.vcbtnModificar.setFont(font2)

        self.horizontalLayout.addWidget(self.vcbtnModificar)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Estudiantes)

        QMetaObject.connectSlotsByName(Estudiantes)
    # setupUi

    def retranslateUi(self, Estudiantes):
        Estudiantes.setWindowTitle(QCoreApplication.translate("Estudiantes", u"Dialog", None))
#if QT_CONFIG(tooltip)
        Estudiantes.setToolTip(QCoreApplication.translate("Estudiantes", u"Estudiantes", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.vCLblTitulo.setToolTip(QCoreApplication.translate("Estudiantes", u"Estudiantes", None))
#endif // QT_CONFIG(tooltip)
        self.vCLblTitulo.setText(QCoreApplication.translate("Estudiantes", u"ESTUDIANTES", None))
#if QT_CONFIG(tooltip)
        self.vcGridEstudiantes.setToolTip(QCoreApplication.translate("Estudiantes", u"Listado de estudiantes", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.vcbtnNuevo.setToolTip(QCoreApplication.translate("Estudiantes", u"Crear nuevo cliente", None))
#endif // QT_CONFIG(tooltip)
        self.vcbtnNuevo.setText(QCoreApplication.translate("Estudiantes", u"Nuevo", None))
#if QT_CONFIG(tooltip)
        self.vcbtnModificar.setToolTip(QCoreApplication.translate("Estudiantes", u"Modificar cliente seleccionado", None))
#endif // QT_CONFIG(tooltip)
        self.vcbtnModificar.setText(QCoreApplication.translate("Estudiantes", u"Ver Detalle", None))
    # retranslateUi

