# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'alta_alumnosYibCjW.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateEdit,
    QFormLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_alumnos(object):
    def setupUi(self, alumnos):
        if not alumnos.objectName():
            alumnos.setObjectName(u"alumnos")
        alumnos.resize(605, 487)
        alumnos.setMinimumSize(QSize(605, 487))
        alumnos.setMaximumSize(QSize(605, 487))
        self.verticalLayout = QVBoxLayout(alumnos)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(alumnos)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setStyleStrategy(QFont.PreferDefault)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_6)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.vcLblNombre = QLabel(alumnos)
        self.vcLblNombre.setObjectName(u"vcLblNombre")
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        self.vcLblNombre.setFont(font1)

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.vcLblNombre)

        self.vcTxtNombre = QLineEdit(alumnos)
        self.vcTxtNombre.setObjectName(u"vcTxtNombre")
        self.vcTxtNombre.setMinimumSize(QSize(0, 35))
        self.vcTxtNombre.setMaximumSize(QSize(16777215, 35))
        font2 = QFont()
        font2.setPointSize(11)
        self.vcTxtNombre.setFont(font2)

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.FieldRole, self.vcTxtNombre)

        self.vcLblApell = QLabel(alumnos)
        self.vcLblApell.setObjectName(u"vcLblApell")
        self.vcLblApell.setFont(font1)

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.LabelRole, self.vcLblApell)

        self.vcTxtApell = QLineEdit(alumnos)
        self.vcTxtApell.setObjectName(u"vcTxtApell")
        self.vcTxtApell.setMinimumSize(QSize(0, 35))
        self.vcTxtApell.setMaximumSize(QSize(16777215, 35))
        self.vcTxtApell.setFont(font2)

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.FieldRole, self.vcTxtApell)

        self.vcLblDni = QLabel(alumnos)
        self.vcLblDni.setObjectName(u"vcLblDni")
        self.vcLblDni.setFont(font1)

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.LabelRole, self.vcLblDni)

        self.vcTxtDni = QLineEdit(alumnos)
        self.vcTxtDni.setObjectName(u"vcTxtDni")
        self.vcTxtDni.setMinimumSize(QSize(0, 35))
        self.vcTxtDni.setMaximumSize(QSize(16777215, 35))
        self.vcTxtDni.setFont(font2)

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.FieldRole, self.vcTxtDni)

        self.vcLblFechaNac = QLabel(alumnos)
        self.vcLblFechaNac.setObjectName(u"vcLblFechaNac")
        self.vcLblFechaNac.setFont(font1)

        self.formLayout_2.setWidget(3, QFormLayout.ItemRole.LabelRole, self.vcLblFechaNac)

        self.vcDateEdit = QDateEdit(alumnos)
        self.vcDateEdit.setObjectName(u"vcDateEdit")
        self.vcDateEdit.setFont(font2)

        self.formLayout_2.setWidget(3, QFormLayout.ItemRole.FieldRole, self.vcDateEdit)

        self.vcLblPoblacion = QLabel(alumnos)
        self.vcLblPoblacion.setObjectName(u"vcLblPoblacion")
        self.vcLblPoblacion.setFont(font1)

        self.formLayout_2.setWidget(4, QFormLayout.ItemRole.LabelRole, self.vcLblPoblacion)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.vccboboxPobl = QComboBox(alumnos)
        self.vccboboxPobl.setObjectName(u"vccboboxPobl")
        self.vccboboxPobl.setFont(font2)

        self.horizontalLayout_2.addWidget(self.vccboboxPobl)

        self.vcLblDni_2 = QLabel(alumnos)
        self.vcLblDni_2.setObjectName(u"vcLblDni_2")
        self.vcLblDni_2.setFont(font1)

        self.horizontalLayout_2.addWidget(self.vcLblDni_2)

        self.vcspinBoxDist = QSpinBox(alumnos)
        self.vcspinBoxDist.setObjectName(u"vcspinBoxDist")
        self.vcspinBoxDist.setFont(font2)
        self.vcspinBoxDist.setMaximum(30)

        self.horizontalLayout_2.addWidget(self.vcspinBoxDist)


        self.formLayout_2.setLayout(4, QFormLayout.ItemRole.FieldRole, self.horizontalLayout_2)

        self.vcLblTutor = QLabel(alumnos)
        self.vcLblTutor.setObjectName(u"vcLblTutor")
        self.vcLblTutor.setFont(font1)

        self.formLayout_2.setWidget(5, QFormLayout.ItemRole.LabelRole, self.vcLblTutor)

        self.vcTxtTutor = QLineEdit(alumnos)
        self.vcTxtTutor.setObjectName(u"vcTxtTutor")
        self.vcTxtTutor.setMinimumSize(QSize(0, 35))
        self.vcTxtTutor.setMaximumSize(QSize(16777215, 35))
        self.vcTxtTutor.setFont(font2)

        self.formLayout_2.setWidget(5, QFormLayout.ItemRole.FieldRole, self.vcTxtTutor)

        self.vcverticalSpacer_5 = QSpacerItem(456, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout_2.setItem(7, QFormLayout.ItemRole.FieldRole, self.vcverticalSpacer_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.vclblModalidad = QLabel(alumnos)
        self.vclblModalidad.setObjectName(u"vclblModalidad")
        self.vclblModalidad.setFont(font1)
        self.vclblModalidad.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.vclblModalidad.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_2.addWidget(self.vclblModalidad)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout_6.addLayout(self.verticalLayout_2)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.vcRdBtnDist = QRadioButton(alumnos)
        self.vcRdBtnDist.setObjectName(u"vcRdBtnDist")
        self.vcRdBtnDist.setFont(font2)

        self.verticalLayout_5.addWidget(self.vcRdBtnDist)

        self.vcRdBtnPrese = QRadioButton(alumnos)
        self.vcRdBtnPrese.setObjectName(u"vcRdBtnPrese")
        self.vcRdBtnPrese.setFont(font2)

        self.verticalLayout_5.addWidget(self.vcRdBtnPrese)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)


        self.horizontalLayout_6.addLayout(self.verticalLayout_5)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_6)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.vcLblExtra = QLabel(alumnos)
        self.vcLblExtra.setObjectName(u"vcLblExtra")
        self.vcLblExtra.setFont(font1)
        self.vcLblExtra.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_3.addWidget(self.vcLblExtra)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.vcChkboxAjedrez = QCheckBox(alumnos)
        self.vcChkboxAjedrez.setObjectName(u"vcChkboxAjedrez")
        self.vcChkboxAjedrez.setFont(font2)

        self.verticalLayout_4.addWidget(self.vcChkboxAjedrez)

        self.vcChkBoDanza = QCheckBox(alumnos)
        self.vcChkBoDanza.setObjectName(u"vcChkBoDanza")
        self.vcChkBoDanza.setFont(font2)

        self.verticalLayout_4.addWidget(self.vcChkBoDanza)

        self.vcChkBoxFtbol = QCheckBox(alumnos)
        self.vcChkBoxFtbol.setObjectName(u"vcChkBoxFtbol")
        self.vcChkBoxFtbol.setFont(font2)

        self.verticalLayout_4.addWidget(self.vcChkBoxFtbol)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_4)


        self.horizontalLayout_3.addLayout(self.verticalLayout_4)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)


        self.formLayout_2.setLayout(8, QFormLayout.ItemRole.FieldRole, self.horizontalLayout_4)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.vcLblTlf = QLabel(alumnos)
        self.vcLblTlf.setObjectName(u"vcLblTlf")
        self.vcLblTlf.setFont(font1)

        self.horizontalLayout_7.addWidget(self.vcLblTlf)

        self.vcTxtTlf = QLineEdit(alumnos)
        self.vcTxtTlf.setObjectName(u"vcTxtTlf")
        self.vcTxtTlf.setMinimumSize(QSize(0, 35))
        self.vcTxtTlf.setMaximumSize(QSize(16777215, 35))
        self.vcTxtTlf.setFont(font2)

        self.horizontalLayout_7.addWidget(self.vcTxtTlf)


        self.formLayout_2.setLayout(6, QFormLayout.ItemRole.FieldRole, self.horizontalLayout_7)


        self.verticalLayout.addLayout(self.formLayout_2)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_8)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_7)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.VcBtnCancelar = QPushButton(alumnos)
        self.VcBtnCancelar.setObjectName(u"VcBtnCancelar")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.VcBtnCancelar.sizePolicy().hasHeightForWidth())
        self.VcBtnCancelar.setSizePolicy(sizePolicy)
        self.VcBtnCancelar.setMinimumSize(QSize(90, 35))
        self.VcBtnCancelar.setFont(font1)

        self.horizontalLayout.addWidget(self.VcBtnCancelar)

        self.vcBtnGuardar = QPushButton(alumnos)
        self.vcBtnGuardar.setObjectName(u"vcBtnGuardar")
        sizePolicy.setHeightForWidth(self.vcBtnGuardar.sizePolicy().hasHeightForWidth())
        self.vcBtnGuardar.setSizePolicy(sizePolicy)
        self.vcBtnGuardar.setMinimumSize(QSize(90, 35))
        self.vcBtnGuardar.setFont(font1)

        self.horizontalLayout.addWidget(self.vcBtnGuardar)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(alumnos)

        QMetaObject.connectSlotsByName(alumnos)
    # setupUi

    def retranslateUi(self, alumnos):
        alumnos.setWindowTitle(QCoreApplication.translate("alumnos", u"Alta alumnos", None))
        self.label.setText(QCoreApplication.translate("alumnos", u"ALTA ALUMNO", None))
        self.vcLblNombre.setText(QCoreApplication.translate("alumnos", u"Nombre", None))
        self.vcLblApell.setText(QCoreApplication.translate("alumnos", u"Apellidos", None))
        self.vcLblDni.setText(QCoreApplication.translate("alumnos", u"DNI", None))
        self.vcLblFechaNac.setText(QCoreApplication.translate("alumnos", u"Fec. Nacimiento", None))
        self.vcLblPoblacion.setText(QCoreApplication.translate("alumnos", u"Poblaci\u00f3n", None))
        self.vcLblDni_2.setText(QCoreApplication.translate("alumnos", u"Distancia hasta el centro (Km)", None))
        self.vcLblTutor.setText(QCoreApplication.translate("alumnos", u"Tutor", None))
        self.vclblModalidad.setText(QCoreApplication.translate("alumnos", u"Modalidad", None))
        self.vcRdBtnDist.setText(QCoreApplication.translate("alumnos", u"Presencial", None))
        self.vcRdBtnPrese.setText(QCoreApplication.translate("alumnos", u"A Distancia", None))
        self.vcLblExtra.setText(QCoreApplication.translate("alumnos", u"Extraescolares", None))
        self.vcChkboxAjedrez.setText(QCoreApplication.translate("alumnos", u"Ajedrez", None))
        self.vcChkBoDanza.setText(QCoreApplication.translate("alumnos", u"Danza", None))
        self.vcChkBoxFtbol.setText(QCoreApplication.translate("alumnos", u"F\u00fatbol", None))
        self.vcLblTlf.setText(QCoreApplication.translate("alumnos", u"Tlf.", None))
        self.VcBtnCancelar.setText(QCoreApplication.translate("alumnos", u"Eliminar", None))
        self.vcBtnGuardar.setText(QCoreApplication.translate("alumnos", u"Confirmar", None))
    # retranslateUi

