
from PyQt5 import QtCore, QtGui, QtWidgets
from Accets.icons_rc_py import iconePrincipal_rc

class Ui_telaBancodedados(object):
    def setupUi(self, telaBancodedados):
        telaBancodedados.setObjectName("telaBancodedados")
        telaBancodedados.resize(835, 540)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(telaBancodedados.sizePolicy().hasHeightForWidth())
        telaBancodedados.setSizePolicy(sizePolicy)
        telaBancodedados.setStyleSheet("background-color: rgb(0, 128, 129);")
        self.centralwidget = QtWidgets.QWidget(telaBancodedados)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.TBW_GERAL_BANCOS = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.TBW_GERAL_BANCOS.setFont(font)
        self.TBW_GERAL_BANCOS.setIconSize(QtCore.QSize(20, 16))
        self.TBW_GERAL_BANCOS.setObjectName("TBW_GERAL_BANCOS")
        self.TBW_BANCO_DADOS_FUNCS = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TBW_BANCO_DADOS_FUNCS.sizePolicy().hasHeightForWidth())
        self.TBW_BANCO_DADOS_FUNCS.setSizePolicy(sizePolicy)
        self.TBW_BANCO_DADOS_FUNCS.setObjectName("TBW_BANCO_DADOS_FUNCS")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.TBW_BANCO_DADOS_FUNCS)
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_12.setSpacing(0)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.FRAME_DA_TBE_FUNC = QtWidgets.QFrame(self.TBW_BANCO_DADOS_FUNCS)
        self.FRAME_DA_TBE_FUNC.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.FRAME_DA_TBE_FUNC.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FRAME_DA_TBE_FUNC.setObjectName("FRAME_DA_TBE_FUNC")
        self.gridLayout_47 = QtWidgets.QGridLayout(self.FRAME_DA_TBE_FUNC)
        self.gridLayout_47.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_47.setSpacing(0)
        self.gridLayout_47.setObjectName("gridLayout_47")
        self.FRAME_DA_TBW_FUNCS = QtWidgets.QFrame(self.FRAME_DA_TBE_FUNC)
        self.FRAME_DA_TBW_FUNCS.setStyleSheet("QFrame{\n"
"margin:0px;\n"
"background-color: rgb(0, 128, 129);\n"
"color: rgb(0, 0, 0);\n"
"}")
        self.FRAME_DA_TBW_FUNCS.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FRAME_DA_TBW_FUNCS.setObjectName("FRAME_DA_TBW_FUNCS")
        self.gridLayout_51 = QtWidgets.QGridLayout(self.FRAME_DA_TBW_FUNCS)
        self.gridLayout_51.setContentsMargins(9, 0, 9, 9)
        self.gridLayout_51.setSpacing(0)
        self.gridLayout_51.setObjectName("gridLayout_51")
        self.TBW_FUNCS = QtWidgets.QTreeWidget(self.FRAME_DA_TBW_FUNCS)
        self.TBW_FUNCS.setStyleSheet("QTreeView{\n"
"margin:0px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(o, o, o);\n"
"}")
        self.TBW_FUNCS.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.TBW_FUNCS.setObjectName("TBW_FUNCS")
        self.TBW_FUNCS.headerItem().setText(0, "1")
        self.gridLayout_51.addWidget(self.TBW_FUNCS, 0, 0, 1, 1)
        self.gridLayout_47.addWidget(self.FRAME_DA_TBW_FUNCS, 2, 0, 1, 1)
        self.FRAME_FILTRO_FUNCS = QtWidgets.QFrame(self.FRAME_DA_TBE_FUNC)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FRAME_FILTRO_FUNCS.sizePolicy().hasHeightForWidth())
        self.FRAME_FILTRO_FUNCS.setSizePolicy(sizePolicy)
        self.FRAME_FILTRO_FUNCS.setMinimumSize(QtCore.QSize(0, 50))
        self.FRAME_FILTRO_FUNCS.setMaximumSize(QtCore.QSize(16777215, 50))
        self.FRAME_FILTRO_FUNCS.setStyleSheet("QFrame{\n"
"    margin: 0px;\n"
"}")
        self.FRAME_FILTRO_FUNCS.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.FRAME_FILTRO_FUNCS.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FRAME_FILTRO_FUNCS.setObjectName("FRAME_FILTRO_FUNCS")
        self.gridLayout_48 = QtWidgets.QGridLayout(self.FRAME_FILTRO_FUNCS)
        self.gridLayout_48.setContentsMargins(6, 0, 1, 0)
        self.gridLayout_48.setHorizontalSpacing(2)
        self.gridLayout_48.setVerticalSpacing(0)
        self.gridLayout_48.setObjectName("gridLayout_48")
        self.FRAME_TXT_FILTRO_FUNCS = QtWidgets.QFrame(self.FRAME_FILTRO_FUNCS)
        self.FRAME_TXT_FILTRO_FUNCS.setMinimumSize(QtCore.QSize(0, 35))
        self.FRAME_TXT_FILTRO_FUNCS.setMaximumSize(QtCore.QSize(16777215, 35))
        self.FRAME_TXT_FILTRO_FUNCS.setStyleSheet("QFrame{\n"
"    margin: 3px;\n"
"}")
        self.FRAME_TXT_FILTRO_FUNCS.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.FRAME_TXT_FILTRO_FUNCS.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FRAME_TXT_FILTRO_FUNCS.setObjectName("FRAME_TXT_FILTRO_FUNCS")
        self.gridLayout_50 = QtWidgets.QGridLayout(self.FRAME_TXT_FILTRO_FUNCS)
        self.gridLayout_50.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_50.setSpacing(0)
        self.gridLayout_50.setObjectName("gridLayout_50")
        self.TXT_FILTRO_FUNCS = QtWidgets.QLineEdit(self.FRAME_TXT_FILTRO_FUNCS)
        self.TXT_FILTRO_FUNCS.setMinimumSize(QtCore.QSize(0, 35))
        self.TXT_FILTRO_FUNCS.setMaximumSize(QtCore.QSize(16777215, 35))
        self.TXT_FILTRO_FUNCS.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.TXT_FILTRO_FUNCS.setDragEnabled(True)
        self.TXT_FILTRO_FUNCS.setObjectName("TXT_FILTRO_FUNCS")
        self.gridLayout_50.addWidget(self.TXT_FILTRO_FUNCS, 0, 0, 1, 1)
        self.gridLayout_48.addWidget(self.FRAME_TXT_FILTRO_FUNCS, 0, 0, 1, 1)
        self.FRAME_BTN_FILTRO_FUNCS = QtWidgets.QFrame(self.FRAME_FILTRO_FUNCS)
        self.FRAME_BTN_FILTRO_FUNCS.setMinimumSize(QtCore.QSize(110, 34))
        self.FRAME_BTN_FILTRO_FUNCS.setMaximumSize(QtCore.QSize(110, 34))
        self.FRAME_BTN_FILTRO_FUNCS.setStyleSheet("QToolButton {\n"
"    border: none;\n"
"    padding: 6px;\n"
"    border-radius: 3px;\n"
"    background:     rgba(255, 255, 255, 200);\n"
"\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"    box-shadow: 0px 1px 3px rgba(0, 0, 0, 0.2),\n"
"                inset 0px 1px 0px rgba(255, 255, 255, 0.4);\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"    box-shadow: inset 0px 1px 2px rgba(0, 0, 0, 0.1);\n"
"}")
        self.FRAME_BTN_FILTRO_FUNCS.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.FRAME_BTN_FILTRO_FUNCS.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FRAME_BTN_FILTRO_FUNCS.setObjectName("FRAME_BTN_FILTRO_FUNCS")
        self.gridLayout_49 = QtWidgets.QGridLayout(self.FRAME_BTN_FILTRO_FUNCS)
        self.gridLayout_49.setContentsMargins(0, 4, 5, 0)
        self.gridLayout_49.setHorizontalSpacing(6)
        self.gridLayout_49.setVerticalSpacing(0)
        self.gridLayout_49.setObjectName("gridLayout_49")
        self.BTN_EXCLUIR_FUNCS = QtWidgets.QToolButton(self.FRAME_BTN_FILTRO_FUNCS)
        self.BTN_EXCLUIR_FUNCS.setMinimumSize(QtCore.QSize(30, 30))
        self.BTN_EXCLUIR_FUNCS.setMaximumSize(QtCore.QSize(30, 30))
        self.BTN_EXCLUIR_FUNCS.setStyleSheet("QToolButton{\n"
"    background-color: transparent;\n"
"    border-radius: 3px;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QToolButton:hover {\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"    box-shadow: 0px 1px 3px rgba(0, 0, 0, 0.2),\n"
"                inset 0px 1px 0px rgba(255, 255, 255, 0.4);\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"    box-shadow: inset 0px 1px 2px rgba(0, 0, 0, 0.1);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Accets/icons/iconCancelar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BTN_EXCLUIR_FUNCS.setIcon(icon)
        self.BTN_EXCLUIR_FUNCS.setIconSize(QtCore.QSize(25, 25))
        self.BTN_EXCLUIR_FUNCS.setObjectName("BTN_EXCLUIR_FUNCS")
        self.gridLayout_49.addWidget(self.BTN_EXCLUIR_FUNCS, 0, 1, 1, 1)
        self.BTN_FILTRO_FUNCS = QtWidgets.QToolButton(self.FRAME_BTN_FILTRO_FUNCS)
        self.BTN_FILTRO_FUNCS.setMinimumSize(QtCore.QSize(30, 30))
        self.BTN_FILTRO_FUNCS.setMaximumSize(QtCore.QSize(30, 30))
        self.BTN_FILTRO_FUNCS.setStyleSheet("QToolButton{\n"
"    background-color: transparent;\n"
"    border-radius: 3px;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QToolButton:hover {\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"    box-shadow: 0px 1px 3px rgba(0, 0, 0, 0.2),\n"
"                inset 0px 1px 0px rgba(255, 255, 255, 0.4);\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"    box-shadow: inset 0px 1px 2px rgba(0, 0, 0, 0.1);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Accets/icons/iconFiltro.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BTN_FILTRO_FUNCS.setIcon(icon1)
        self.BTN_FILTRO_FUNCS.setIconSize(QtCore.QSize(25, 25))
        self.BTN_FILTRO_FUNCS.setObjectName("BTN_FILTRO_FUNCS")
        self.gridLayout_49.addWidget(self.BTN_FILTRO_FUNCS, 0, 0, 1, 1)
        self.BTN_LIMPAR_TBW_FUNCS = QtWidgets.QToolButton(self.FRAME_BTN_FILTRO_FUNCS)
        self.BTN_LIMPAR_TBW_FUNCS.setMinimumSize(QtCore.QSize(30, 30))
        self.BTN_LIMPAR_TBW_FUNCS.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setPointSize(5)
        self.BTN_LIMPAR_TBW_FUNCS.setFont(font)
        self.BTN_LIMPAR_TBW_FUNCS.setStyleSheet("QToolButton{\n"
"    background-color: transparent;\n"
"    border-radius: 3px;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QToolButton:hover {\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"    box-shadow: 0px 1px 3px rgba(0, 0, 0, 0.2),\n"
"                inset 0px 1px 0px rgba(255, 255, 255, 0.4);\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"    box-shadow: inset 0px 1px 2px rgba(0, 0, 0, 0.1);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.BTN_LIMPAR_TBW_FUNCS.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Accets/icons/iconVassoura.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BTN_LIMPAR_TBW_FUNCS.setIcon(icon2)
        self.BTN_LIMPAR_TBW_FUNCS.setIconSize(QtCore.QSize(25, 25))
        self.BTN_LIMPAR_TBW_FUNCS.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.BTN_LIMPAR_TBW_FUNCS.setObjectName("BTN_LIMPAR_TBW_FUNCS")
        self.gridLayout_49.addWidget(self.BTN_LIMPAR_TBW_FUNCS, 0, 2, 1, 1)
        self.gridLayout_48.addWidget(self.FRAME_BTN_FILTRO_FUNCS, 0, 1, 1, 1)
        self.gridLayout_47.addWidget(self.FRAME_FILTRO_FUNCS, 1, 0, 1, 1)
        self.gridLayout_12.addWidget(self.FRAME_DA_TBE_FUNC, 0, 0, 1, 1)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Accets/icons/iconbancodedados.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.TBW_GERAL_BANCOS.addTab(self.TBW_BANCO_DADOS_FUNCS, icon3, "")
        self.TBW_BANCO_DADOS_CLIENTE = QtWidgets.QWidget()
        self.TBW_BANCO_DADOS_CLIENTE.setObjectName("TBW_BANCO_DADOS_CLIENTE")
        self.gridLayout_44 = QtWidgets.QGridLayout(self.TBW_BANCO_DADOS_CLIENTE)
        self.gridLayout_44.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_44.setSpacing(0)
        self.gridLayout_44.setObjectName("gridLayout_44")
        self.FRAME_BANCO_DADOS = QtWidgets.QFrame(self.TBW_BANCO_DADOS_CLIENTE)
        self.FRAME_BANCO_DADOS.setStyleSheet("QFrame{\n"
"background-color: rgb(0, 128, 129);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QToolBuntton{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"QLineEdit{\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"QTableWidget{\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.FRAME_BANCO_DADOS.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.FRAME_BANCO_DADOS.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FRAME_BANCO_DADOS.setObjectName("FRAME_BANCO_DADOS")
        self.gridLayout_20 = QtWidgets.QGridLayout(self.FRAME_BANCO_DADOS)
        self.gridLayout_20.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_20.setSpacing(0)
        self.gridLayout_20.setObjectName("gridLayout_20")
        self.FRAME_FILTRO_PESQUISA = QtWidgets.QFrame(self.FRAME_BANCO_DADOS)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FRAME_FILTRO_PESQUISA.sizePolicy().hasHeightForWidth())
        self.FRAME_FILTRO_PESQUISA.setSizePolicy(sizePolicy)
        self.FRAME_FILTRO_PESQUISA.setMinimumSize(QtCore.QSize(0, 50))
        self.FRAME_FILTRO_PESQUISA.setMaximumSize(QtCore.QSize(16777215, 50))
        self.FRAME_FILTRO_PESQUISA.setStyleSheet("QFrame{\n"
"    margin: 3px;\n"
"}")
        self.FRAME_FILTRO_PESQUISA.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.FRAME_FILTRO_PESQUISA.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FRAME_FILTRO_PESQUISA.setObjectName("FRAME_FILTRO_PESQUISA")
        self.gridLayout_19 = QtWidgets.QGridLayout(self.FRAME_FILTRO_PESQUISA)
        self.gridLayout_19.setContentsMargins(3, 2, 0, 2)
        self.gridLayout_19.setSpacing(0)
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.FRAME_BOTOES_FILTRO_CLIENTE = QtWidgets.QFrame(self.FRAME_FILTRO_PESQUISA)
        self.FRAME_BOTOES_FILTRO_CLIENTE.setMinimumSize(QtCore.QSize(85, 34))
        self.FRAME_BOTOES_FILTRO_CLIENTE.setMaximumSize(QtCore.QSize(85, 34))
        self.FRAME_BOTOES_FILTRO_CLIENTE.setStyleSheet("QFrame{\n"
" background: transparent;\n"
"}\n"
"")
        self.FRAME_BOTOES_FILTRO_CLIENTE.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.FRAME_BOTOES_FILTRO_CLIENTE.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FRAME_BOTOES_FILTRO_CLIENTE.setObjectName("FRAME_BOTOES_FILTRO_CLIENTE")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.FRAME_BOTOES_FILTRO_CLIENTE)
        self.gridLayout_10.setContentsMargins(0, 1, 1, 0)
        self.gridLayout_10.setHorizontalSpacing(9)
        self.gridLayout_10.setVerticalSpacing(0)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.BTN_FILTRO_CLIENTE = QtWidgets.QToolButton(self.FRAME_BOTOES_FILTRO_CLIENTE)
        self.BTN_FILTRO_CLIENTE.setMinimumSize(QtCore.QSize(30, 30))
        self.BTN_FILTRO_CLIENTE.setMaximumSize(QtCore.QSize(30, 30))
        self.BTN_FILTRO_CLIENTE.setStyleSheet("QToolButton{\n"
"    background-color: transparent;\n"
"    border-radius: 3px;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QToolButton:hover {\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"    box-shadow: 0px 1px 3px rgba(0, 0, 0, 0.2),\n"
"                inset 0px 1px 0px rgba(255, 255, 255, 0.4);\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"    box-shadow: inset 0px 1px 2px rgba(0, 0, 0, 0.1);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.BTN_FILTRO_CLIENTE.setIcon(icon1)
        self.BTN_FILTRO_CLIENTE.setIconSize(QtCore.QSize(20, 20))
        self.BTN_FILTRO_CLIENTE.setObjectName("BTN_FILTRO_CLIENTE")
        self.gridLayout_10.addWidget(self.BTN_FILTRO_CLIENTE, 0, 0, 1, 1)
        self.BTN_EXCLUIR_CCLIENTE = QtWidgets.QToolButton(self.FRAME_BOTOES_FILTRO_CLIENTE)
        self.BTN_EXCLUIR_CCLIENTE.setMinimumSize(QtCore.QSize(30, 30))
        self.BTN_EXCLUIR_CCLIENTE.setMaximumSize(QtCore.QSize(30, 30))
        self.BTN_EXCLUIR_CCLIENTE.setStyleSheet("QToolButton{\n"
"    background-color: transparent;\n"
"    border-radius: 3px;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QToolButton:hover {\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"    box-shadow: 0px 1px 3px rgba(0, 0, 0, 0.2),\n"
"                inset 0px 1px 0px rgba(255, 255, 255, 0.4);\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"    box-shadow: inset 0px 1px 2px rgba(0, 0, 0, 0.1);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.BTN_EXCLUIR_CCLIENTE.setIcon(icon)
        self.BTN_EXCLUIR_CCLIENTE.setIconSize(QtCore.QSize(20, 20))
        self.BTN_EXCLUIR_CCLIENTE.setObjectName("BTN_EXCLUIR_CCLIENTE")
        self.gridLayout_10.addWidget(self.BTN_EXCLUIR_CCLIENTE, 0, 1, 1, 1)
        self.gridLayout_19.addWidget(self.FRAME_BOTOES_FILTRO_CLIENTE, 0, 1, 1, 1, QtCore.Qt.AlignRight)
        self.FRAME_TXT_FILTRO_CLIENTE = QtWidgets.QFrame(self.FRAME_FILTRO_PESQUISA)
        self.FRAME_TXT_FILTRO_CLIENTE.setMinimumSize(QtCore.QSize(0, 35))
        self.FRAME_TXT_FILTRO_CLIENTE.setMaximumSize(QtCore.QSize(16777215, 35))
        self.FRAME_TXT_FILTRO_CLIENTE.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.FRAME_TXT_FILTRO_CLIENTE.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FRAME_TXT_FILTRO_CLIENTE.setObjectName("FRAME_TXT_FILTRO_CLIENTE")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.FRAME_TXT_FILTRO_CLIENTE)
        self.gridLayout_8.setContentsMargins(0, 0, 1, 0)
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.TXT_FILTRO_CLIENTE = QtWidgets.QLineEdit(self.FRAME_TXT_FILTRO_CLIENTE)
        self.TXT_FILTRO_CLIENTE.setMinimumSize(QtCore.QSize(0, 35))
        self.TXT_FILTRO_CLIENTE.setMaximumSize(QtCore.QSize(16777215, 35))
        self.TXT_FILTRO_CLIENTE.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.TXT_FILTRO_CLIENTE.setDragEnabled(True)
        self.TXT_FILTRO_CLIENTE.setObjectName("TXT_FILTRO_CLIENTE")
        self.gridLayout_8.addWidget(self.TXT_FILTRO_CLIENTE, 0, 0, 1, 1)
        self.gridLayout_19.addWidget(self.FRAME_TXT_FILTRO_CLIENTE, 0, 0, 1, 1)
        self.gridLayout_20.addWidget(self.FRAME_FILTRO_PESQUISA, 0, 0, 1, 1)
        self.FRAME_TBW_FILTRO_PESQUISA = QtWidgets.QFrame(self.FRAME_BANCO_DADOS)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FRAME_TBW_FILTRO_PESQUISA.sizePolicy().hasHeightForWidth())
        self.FRAME_TBW_FILTRO_PESQUISA.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.FRAME_TBW_FILTRO_PESQUISA.setFont(font)
        self.FRAME_TBW_FILTRO_PESQUISA.setStyleSheet("QFrame{\n"
"margin:0px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(0, 128, 129);\n"
"}")
        self.FRAME_TBW_FILTRO_PESQUISA.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.FRAME_TBW_FILTRO_PESQUISA.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FRAME_TBW_FILTRO_PESQUISA.setObjectName("FRAME_TBW_FILTRO_PESQUISA")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.FRAME_TBW_FILTRO_PESQUISA)
        self.gridLayout_13.setContentsMargins(10, 1, 9, 9)
        self.gridLayout_13.setSpacing(0)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.TBW_CLIENTES = QtWidgets.QTreeWidget(self.FRAME_TBW_FILTRO_PESQUISA)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.TBW_CLIENTES.setFont(font)
        self.TBW_CLIENTES.setStyleSheet("QTreeView{\n"
"margin:0px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"}")
        self.TBW_CLIENTES.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.TBW_CLIENTES.setObjectName("TBW_CLIENTES")
        self.TBW_CLIENTES.headerItem().setText(0, "1")
        self.TBW_CLIENTES.header().setMinimumSectionSize(42)
        self.gridLayout_13.addWidget(self.TBW_CLIENTES, 0, 0, 1, 1)
        self.gridLayout_20.addWidget(self.FRAME_TBW_FILTRO_PESQUISA, 1, 0, 1, 1)
        self.gridLayout_44.addWidget(self.FRAME_BANCO_DADOS, 0, 0, 1, 1)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Accets/icons/iconClientes2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.TBW_GERAL_BANCOS.addTab(self.TBW_BANCO_DADOS_CLIENTE, icon4, "")
        self.TBW_GERAL_EQUIPAMENTOS = QtWidgets.QWidget()
        self.TBW_GERAL_EQUIPAMENTOS.setObjectName("TBW_GERAL_EQUIPAMENTOS")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.TBW_GERAL_EQUIPAMENTOS)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame = QtWidgets.QFrame(self.TBW_GERAL_EQUIPAMENTOS)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 40))
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_4.setContentsMargins(0, 0, 3, 0)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setMinimumSize(QtCore.QSize(0, 45))
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 45))
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_6.setContentsMargins(9, 7, 4, 0)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.TXT_FILTRO_EQUIPAMENTOS = QtWidgets.QLineEdit(self.frame_4)
        self.TXT_FILTRO_EQUIPAMENTOS.setMinimumSize(QtCore.QSize(0, 32))
        self.TXT_FILTRO_EQUIPAMENTOS.setMaximumSize(QtCore.QSize(16777215, 32))
        self.TXT_FILTRO_EQUIPAMENTOS.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.TXT_FILTRO_EQUIPAMENTOS.setObjectName("TXT_FILTRO_EQUIPAMENTOS")
        self.gridLayout_6.addWidget(self.TXT_FILTRO_EQUIPAMENTOS, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.frame_4, 0, 0, 1, 1)
        self.frame_5 = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setMinimumSize(QtCore.QSize(85, 36))
        self.frame_5.setMaximumSize(QtCore.QSize(85, 36))
        self.frame_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_5.setContentsMargins(9, 6, 9, 0)
        self.gridLayout_5.setHorizontalSpacing(12)
        self.gridLayout_5.setVerticalSpacing(0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.BN_FILTRO_EQUIPAMENTOS = QtWidgets.QToolButton(self.frame_5)
        self.BN_FILTRO_EQUIPAMENTOS.setMinimumSize(QtCore.QSize(30, 30))
        self.BN_FILTRO_EQUIPAMENTOS.setMaximumSize(QtCore.QSize(30, 30))
        self.BN_FILTRO_EQUIPAMENTOS.setStyleSheet("QToolButton{\n"
"    background-color: transparent;\n"
"    border-radius: 3px;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QToolButton:hover {\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"    box-shadow: 0px 1px 3px rgba(0, 0, 0, 0.2),\n"
"                inset 0px 1px 0px rgba(255, 255, 255, 0.4);\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"    box-shadow: inset 0px 1px 2px rgba(0, 0, 0, 0.1);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../icons/iconFiltro.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BN_FILTRO_EQUIPAMENTOS.setIcon(icon5)
        self.BN_FILTRO_EQUIPAMENTOS.setIconSize(QtCore.QSize(20, 20))
        self.BN_FILTRO_EQUIPAMENTOS.setObjectName("BN_FILTRO_EQUIPAMENTOS")
        self.gridLayout_5.addWidget(self.BN_FILTRO_EQUIPAMENTOS, 0, 0, 1, 1, QtCore.Qt.AlignVCenter)
        self.BTN_CANCELAR_EQUIPAMENTOS = QtWidgets.QToolButton(self.frame_5)
        self.BTN_CANCELAR_EQUIPAMENTOS.setMinimumSize(QtCore.QSize(30, 30))
        self.BTN_CANCELAR_EQUIPAMENTOS.setMaximumSize(QtCore.QSize(30, 30))
        self.BTN_CANCELAR_EQUIPAMENTOS.setStyleSheet("QToolButton{\n"
"    background-color: transparent;\n"
"    border-radius: 3px;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QToolButton:hover {\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"    box-shadow: 0px 1px 3px rgba(0, 0, 0, 0.2),\n"
"                inset 0px 1px 0px rgba(255, 255, 255, 0.4);\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"    box-shadow: inset 0px 1px 2px rgba(0, 0, 0, 0.1);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("../icons/iconCancelar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BTN_CANCELAR_EQUIPAMENTOS.setIcon(icon6)
        self.BTN_CANCELAR_EQUIPAMENTOS.setIconSize(QtCore.QSize(20, 20))
        self.BTN_CANCELAR_EQUIPAMENTOS.setObjectName("BTN_CANCELAR_EQUIPAMENTOS")
        self.gridLayout_5.addWidget(self.BTN_CANCELAR_EQUIPAMENTOS, 0, 1, 1, 1)
        self.gridLayout_4.addWidget(self.frame_5, 0, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.gridLayout_3.addWidget(self.frame_2, 0, 0, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_7.setContentsMargins(10, 5, -1, -1)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.TBW_EQUIPAMENTOS = QtWidgets.QTreeWidget(self.frame_3)
        self.TBW_EQUIPAMENTOS.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.TBW_EQUIPAMENTOS.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.TBW_EQUIPAMENTOS.setObjectName("TBW_EQUIPAMENTOS")
        self.TBW_EQUIPAMENTOS.headerItem().setText(0, "1")
        self.gridLayout_7.addWidget(self.TBW_EQUIPAMENTOS, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.frame_3, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("../icons/iconLaptop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.TBW_GERAL_BANCOS.addTab(self.TBW_GERAL_EQUIPAMENTOS, icon7, "")
        self.gridLayout.addWidget(self.TBW_GERAL_BANCOS, 1, 0, 1, 1)
        self.frame_6 = QtWidgets.QFrame(self.centralwidget)
        self.frame_6.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_6.setStyleSheet("QToolButton{\n"
"    background-color: transparent;\n"
"    border-radius: 3px;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QToolButton:hover {\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"    box-shadow: 0px 1px 3px rgba(0, 0, 0, 0.2),\n"
"                inset 0px 1px 0px rgba(255, 255, 255, 0.4);\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"    box-shadow: inset 0px 1px 2px rgba(0, 0, 0, 0.1);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.frame_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.BTN_MINIMIZAR = QtWidgets.QToolButton(self.frame_6)
        self.BTN_MINIMIZAR.setMinimumSize(QtCore.QSize(30, 30))
        self.BTN_MINIMIZAR.setMaximumSize(QtCore.QSize(30, 30))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("../icons/Minimize.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BTN_MINIMIZAR.setIcon(icon8)
        self.BTN_MINIMIZAR.setIconSize(QtCore.QSize(25, 25))
        self.BTN_MINIMIZAR.setObjectName("BTN_MINIMIZAR")
        self.gridLayout_9.addWidget(self.BTN_MINIMIZAR, 0, 1, 1, 1)
        self.BTN_MAXIMIZAR = QtWidgets.QToolButton(self.frame_6)
        self.BTN_MAXIMIZAR.setMinimumSize(QtCore.QSize(30, 30))
        self.BTN_MAXIMIZAR.setMaximumSize(QtCore.QSize(30, 30))
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("../icons/Maximize.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BTN_MAXIMIZAR.setIcon(icon9)
        self.BTN_MAXIMIZAR.setIconSize(QtCore.QSize(25, 25))
        self.BTN_MAXIMIZAR.setObjectName("BTN_MAXIMIZAR")
        self.gridLayout_9.addWidget(self.BTN_MAXIMIZAR, 0, 2, 1, 1)
        self.BTN_FECHAR = QtWidgets.QToolButton(self.frame_6)
        self.BTN_FECHAR.setMinimumSize(QtCore.QSize(30, 30))
        self.BTN_FECHAR.setMaximumSize(QtCore.QSize(30, 30))
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("../icons/iconRetornar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BTN_FECHAR.setIcon(icon10)
        self.BTN_FECHAR.setIconSize(QtCore.QSize(25, 25))
        self.BTN_FECHAR.setObjectName("BTN_FECHAR")
        self.gridLayout_9.addWidget(self.BTN_FECHAR, 0, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame_6, 0, 0, 1, 1)
        telaBancodedados.setCentralWidget(self.centralwidget)

        self.retranslateUi(telaBancodedados)
        self.TBW_GERAL_BANCOS.setCurrentIndex(2)
        self.BTN_FECHAR.clicked.connect(telaBancodedados.close) # type: ignore
        self.BTN_MAXIMIZAR.clicked.connect(telaBancodedados.showMaximized) # type: ignore
        self.BTN_MINIMIZAR.clicked.connect(telaBancodedados.showNormal) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(telaBancodedados)

    def retranslateUi(self, telaBancodedados):
        _translate = QtCore.QCoreApplication.translate
        telaBancodedados.setWindowTitle(_translate("telaBancodedados", "BANCO DE DADOS"))
        self.TXT_FILTRO_FUNCS.setPlaceholderText(_translate("telaBancodedados", "Buscar por:  \"Nome, Sobre-nome, Código\""))
        self.BTN_EXCLUIR_FUNCS.setText(_translate("telaBancodedados", "..."))
        self.BTN_FILTRO_FUNCS.setText(_translate("telaBancodedados", "..."))
        self.TBW_GERAL_BANCOS.setTabText(self.TBW_GERAL_BANCOS.indexOf(self.TBW_BANCO_DADOS_FUNCS), _translate("telaBancodedados", "BANCO DE DADOS FUNCIONARIOS"))
        self.BTN_FILTRO_CLIENTE.setText(_translate("telaBancodedados", "..."))
        self.BTN_EXCLUIR_CCLIENTE.setText(_translate("telaBancodedados", "..."))
        self.TXT_FILTRO_CLIENTE.setPlaceholderText(_translate("telaBancodedados", "Buscar por:  \"Nome, Sobre-nome, Código\""))
        self.TBW_GERAL_BANCOS.setTabText(self.TBW_GERAL_BANCOS.indexOf(self.TBW_BANCO_DADOS_CLIENTE), _translate("telaBancodedados", "BANCO DE DADOS CLIENTE"))
        self.BN_FILTRO_EQUIPAMENTOS.setText(_translate("telaBancodedados", "..."))
        self.BTN_CANCELAR_EQUIPAMENTOS.setText(_translate("telaBancodedados", "..."))
        self.TBW_GERAL_BANCOS.setTabText(self.TBW_GERAL_BANCOS.indexOf(self.TBW_GERAL_EQUIPAMENTOS), _translate("telaBancodedados", "EQUIPAMENTOS"))
        self.BTN_MINIMIZAR.setText(_translate("telaBancodedados", "..."))
        self.BTN_MAXIMIZAR.setText(_translate("telaBancodedados", "..."))
        self.BTN_FECHAR.setText(_translate("telaBancodedados", "..."))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    telaBancodedados = QtWidgets.QMainWindow()
    ui = Ui_telaBancodedados()
    ui.setupUi(telaBancodedados)
    telaBancodedados.show()
    sys.exit(app.exec_())
