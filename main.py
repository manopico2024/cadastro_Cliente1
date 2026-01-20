###############################################################
#                 CRIADO POR MVDevTECHteam!                   #                                                              
#                                                             #
#          Créditos: Developer Marcus Vinicius Nunes          #
#                                                             #        
#                          @2025                              #
#                        Game-PASS                            #                            
#                           \o/                               #
#                      Tem mais Atualizações                  #                              
###############################################################

# IMPORTANDO AS LIBS DE INTERFACE GRÁFICA
from PyQt5.QtWidgets import (QDialog, QMessageBox, 
QMainWindow, QApplication, QTreeWidgetItem, QVBoxLayout, QTextEdit, QPushButton, QShortcut,
QHBoxLayout, QComboBox, QLabel, QInputDialog, QTableWidget, QTableWidgetItem, QFrame)
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
QHBoxLayout, QPushButton, QTreeWidget, QTreeWidgetItem, QLineEdit, QLabel, QMessageBox, QFileDialog)
from PyQt5.QtWidgets import QFileDialog, QProgressDialog
#from tkinter import Tk
from PyQt5.QtCore import Qt, QCoreApplication
from PyQt5.QtGui import QKeySequence
from PyQt5 import QtWidgets, QtGui
from datetime import datetime
from PyQt5.QtCore import Qt
from PyQt5 import QtCore
import pandas as pd
from PyQt5.QtGui import QPixmap
# IMPORTANDO AS LIBS DE BANCO DE DADOS
import sqlite3
# IMPORTANDO AS LIBS DE SISTEMA
from pathlib import Path
import shutil
import sys
import os
from banco.sqlite import sqlite_db
# IMPORTANDO AS TELAS
from models.telaLogin import Ui_telaLogin
from models.telaGrafico import Ui_telaGrafico
from models.telaBancodados import Ui_telaBancodedados
from models.telaFichacliente import Ui_telaFichacliente
from models.telaVendas import Ui_telaVendas
from models.telaPrincipal import Ui_telaPrincipal
from funcoes.funcoes_da_tela import TelaArrastavelBase
from models.telaRegistrofuncs import Ui_telaFuncionario
from models.telatelaOrdemservicos import Ui_telaOrdemservicos
from models.telaConsultacliente import Ui_telaConsultacliente
from models.telaNotafiscal import Ui_telaNotafiscal

from models.telaProduto import Ui_telaProduto
from models.telaPedido import Ui_telaPedido
from funcoes.funcoes_da_tela_grafico import mostrar_o_grafico
from db.query_equipamentos import SqliteDb 
from database.query_equipamentos import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os
from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog, QInputDialog, QVBoxLayout, QPushButton, QTextEdit, QTreeWidgetItem
from PyQt5.QtCore import Qt
from models.telaEstoque import Ui_telaGerenicamentoestoque
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime
import shutil
#IMPORTANDO OS LOGS DE ERRO
import traceback
import logging

class Login(TelaArrastavelBase):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_telaLogin()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowIcon(QtGui.QIcon("Accets/icons/icons/logoSpike.png"))
        self.ui.TXT_SENHA.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ui.TXT_NOME.setFocus()        
        self.login_sucesso = False
        
        self.configurar_shortcuts_login()
        
        # CONECTAR BOTÕES DO LOGIN
        self.ui.BTN_LOGIN.clicked.connect(self.novo_login)
        self.ui.TXT_SENHA.returnPressed.connect(self.novo_login)
        self.ui.TXT_NOME.returnPressed.connect(self.focar_senha)
        
    def configurar_shortcuts_login(self):           
        if hasattr(self, 'shortcutEnterNome') and self.shortcutEnterNome:
            self.shortcutEnterNome.deleteLater()
        if hasattr(self, 'shortcutEnterSenha') and self.shortcutEnterSenha:
            self.shortcutEnterSenha.deleteLater()
        if hasattr(self, 'shortcutEsc') and self.shortcutEsc:
            self.shortcutEsc.deleteLater()
        self.shortcutEnterNome = QShortcut(QKeySequence(Qt.Key_Return), self)
        self.shortcutEnterNome.activated.connect(self.focar_senha)
        self.shortcutEnterNome.setContext(Qt.WidgetShortcut)
        self.shortcutEnterSenha = QShortcut(QKeySequence(Qt.Key_Enter), self)
        self.shortcutEnterSenha.activated.connect(self.novo_login)
        self.shortcutEnterSenha.setContext(Qt.WidgetShortcut)
        self.shortcutEsc = QShortcut(QKeySequence(Qt.Key_Escape), self)
        self.shortcutEsc.activated.connect(self.fechar_aplicacao)
        self.shortcutEsc.setContext(Qt.ApplicationShortcut)

    def focar_senha(self):
        self.ui.TXT_SENHA.setFocus()

    def fechar_aplicacao(self):
        self.close()
        QCoreApplication.quit()

    def novo_login(self):
        admin = "admin"
        senha = "admin"
        user = self.ui.TXT_NOME.text().strip()
        password = self.ui.TXT_SENHA.text().strip()
        if not user or not password:
            self.mostrar_mensagem("Atenção", "📝 Por favor, preencha todos os campos!")
            return
        if admin == user and senha == password:
            self.mostrar_mensagem("Sucesso", "✅ Login realizado com sucesso!\nBem-vindo ao sistema!")
            self.login_sucesso = True
            self.close()
        else:
            self.mostrar_mensagem("Erro", "❌ Credenciais inválidas!\nVerifique usuário e senha.")
            self.ui.TXT_SENHA.clear()
            self.ui.TXT_NOME.setFocus()

    # FUNCAO PARA MOSTRAR MENSAGENS DO LOGIN
    def mostrar_mensagem(self, titulo, mensagem):
        dialog = QDialog(self)
        dialog.setWindowTitle(titulo)
        dialog.setModal(True)
        dialog.setFixedSize(300, 150)
        dialog.setStyleSheet("background-color: #008081")
        try:
            dialog.setWindowIcon(QtGui.QIcon("Accets/icons/logoSpike.png"))
        except:
            pass
        
        layout = QVBoxLayout(dialog)
        label = QtWidgets.QLabel(mensagem)
        label.setStyleSheet("color: #ffffff; font-size: 14px; font-weight: bold; background-color: #008081")
        label.setAlignment(Qt.AlignCenter)

        btn_ok = QPushButton("OK")
        btn_ok.setStyleSheet("""
            QPushButton {
                background-color: white;
                color: black;
                border: 1px solid #cccccc;
                padding: 8px 16px;
                border-radius: 4px;
                font-size: 12px;
                font-weight: bold;}
            QPushButton:hover {
                background-color: #f8f8f8;
                border-color: #999999;}
            QPushButton:pressed {
                background-color: #f0f0f0;}""")
        btn_ok.clicked.connect(dialog.accept)
        
        layout.addWidget(label)
        layout.addWidget(btn_ok)
        dialog.setStyleSheet("QDialog { background-color: white; }")
        dialog.exec_()

    def login_foi_bem_sucedido(self):
        return self.login_sucesso
    
    def closeEvent(self, event):
        if not self.login_sucesso:
            QCoreApplication.quit()
        super().closeEvent(event)

class TelaFuncionarios(TelaArrastavelBase):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_telaFuncionario()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowIcon(QtGui.QIcon("Accets/icons/icons/logoSpike.png"))
        self.setGeometry(285, 70, 700, 600)
        self.db_funcs = sqlite_db("db/sistema.db")
        self.configurar_tela_funcs()
        self.carregar_dados_funcs()
    
    def configurar_tela_funcs(self):
        try:
            self.conectar_botoes_consulta_funcs()
            self.configurar_shortcuts_funcs()
        except Exception as e:
            print(f"Erro ao configurar tela: {e}")
    
    def configurar_shortcuts_funcs(self):
        try:
            self.shortcut_esc = QShortcut(QKeySequence(Qt.Key_Escape), self)
            self.shortcut_esc.activated.connect(self.fechar_tela)
            if hasattr(self.ui, 'TXT_FILTRO_FUNCS'):
                self.shortcut_enter_filtro = QShortcut(QKeySequence(Qt.Key_Return), self.ui.TXT_FILTRO_FUNCS)
                self.shortcut_enter_filtro.activated.connect(self.pesquisar_funcs)
        except Exception as e:
            print(f"Erro ao configurar shortcuts: {e}")
   
    def carregar_dados_funcs(self):
        try:
            self.pesquisar_funcs()
        except Exception as e:
            print(f"Erro ao carregar dados: {e}")

    def conectar_botoes_consulta_funcs(self):
        try:
            if hasattr(self.ui, 'BTN_RETORNAR_TELA_PRINCIPAL'):
                self.ui.BTN_VOLTAR_TELA_PRINCIPAL.clicked.connect(self.fechar_tela)
            if hasattr(self.ui, 'BTN_LIMPAR_TBW_FUNCS'):
                self.ui.BTN_LIMPAR_IMG_FUNCS.clicked.connect(self.limpar_campos)
            if hasattr(self.ui, 'BTN_FILTRO_FUNCS'):
                self.ui.BTN_FILTRO_FUNCS.clicked.connect(self.pesquisar_funcs)
            if hasattr(self.ui, 'TXT_FILTRO_FUNCS'):
                self.ui.TXT_FILTRO_FUNCS.textChanged.connect(self.filtrar_funcs)
        except Exception as e:
            print(f"Erro ao conectar botões: {e}")

    def preencher_tabela_funcs(self, funcs):
        try:
            if not hasattr(self.ui, 'TBW_FUNCS'):
                print("Widget TBW_FUNCS não encontrado")
                return
            self.ui.TBW_FUNCS.clear()
            colunas = ["ID", "Nome", "Endereço", "Documento", "Complemento", "Admin"]
            self.ui.TBW_FUNCS.setColumnCount(len(colunas))
            self.ui.TBW_FUNCS.setHeaderLabels(colunas)
            
            for func in funcs:
                item = QTreeWidgetItem([
                    str(func[0]),  # ID
                    func[1],       # Nome
                    func[2],       # Endereço
                    func[3],       # Documento
                    func[4],       # Complemento
                    "Sim" if func[5] else "Não"                ])
                self.ui.TBW_FUNCS.addTopLevelItem(item)
            self.atualizar_contagem_funcs(len(funcs))
        except Exception as e:
            print(f"Erro ao preencher tabela: {e}")

    def pesquisar_funcs(self):
        try:
            filtro = ""
            if hasattr(self.ui, 'TXT_FILTRO_FUNCS'):
                filtro = self.ui.TXT_FILTRO_FUNCS.text().strip()
            funcs = self.db_funcs.buscar_funcs(filtro)
            self.preencher_tabela_funcs(funcs)
        except Exception as e:
            print(f"Erro na pesquisa: {e}")

    def limpar_campos(self):
        self.ui.TXT_BAIRRO_FUNCS.clear()
        self.ui.TXT_CELULAR_FUNCS.clear()
        self.ui.LABEL_IMG_FUNCS.clear()
        self.ui.TXT_CEP_FUNCS.clear()
        self.ui.TXT_NOME_FUNCS.clear()
        self.ui.TXT_CODIGO_FUNCS.clear()
        self.ui.TXT_NUMERO_CASA_FUNCS.clear()
        self.ui.TXT_COMPLEMENTO_FUNCS.clear()
        self.ui.TXT_CNPJ_CPF_FUNCS.clear()
        self.ui.TXT_DATA_NASCIMENTO_FUNCS.clear()
        self.ui.TXT_EMAIL_FUNCS.clear()
        self.ui.TXT_CIDADE_FUNCS.clear()
        self.ui.TXT_NUMERO_CASA_FUNCS.clear()
        self.ui.TXT_OBSERVACOES_FUNCS.clear()
        self.ui.TXT_FILTRO_FUNCS.clear()
        self.ui.TXT_PROFISSAO_FUNCS.clear()
        self.ui.TXT_RG_FUNCS.clear()
        self.ui.TXT_UF_FUNCS.clear()
        self.ui.TXT_TELEFONE_FUNCS.clear()
        self.ui.TXT_ENDERECO_FUNCS.clear()

    def filtrar_funcs(self):
        try:
            self.pesquisar_funcs()
        except Exception as e:
            print(f"Erro no filtro: {e}")

    def atualizar_contagem_funcs(self, total):
        try:
            if hasattr(self.ui, 'LABEL_TOTAL_FUNCS'):
                self.ui.LABEL_TOTAL_FUNCS.setText(f"Total de Funcionários: {total}")
            else:
                print("Label 'LABEL_TOTAL_FUNCS' não encontrada na interface")
                
        except Exception as e:
            print(f"Erro ao atualizar contagem: {e}")

    def fechar_tela(self):
        self.db_funcs.fechar_conexao()
        self.close()

class TelaFichaCliente(TelaArrastavelBase):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_telaFichacliente()
        self.ui.setupUi(self)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowIcon(QtGui.QIcon("Accets/icons/icons/logoSpike.png"))
        self.setGeometry(300, 150, 600, 400)

class TelaNotaFiscal(TelaArrastavelBase):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_telaNotafiscal()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowIcon(QtCore.Qt("Accets/icons/icons/logoSpike.png"))
        self.geometry(300, 150, 600, 500)

class TelaEstoque(TelaArrastavelBase):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_telaGerenicamentoestoque()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowIcon(QtGui.QIcon("Accets/icons/icons/logoSpike.png"))
        self.setGeometry(300, 150, 600, 400)    

class TelaRegistro(TelaArrastavelBase):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_telaFuncionario()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowIcon(QtGui.QIcon("Accets/icons/icons/logoSpike.png"))
        self.setGeometry(300, 150, 800, 600)
        self.db_registro = sqlite_db("db/sistema.db")
        self.configurar_tela_registro()

    def configurar_tela_registro(self):
        try:
            # CONECTAR OS BOTÕES CORRETAMENTE
            if hasattr(self.ui, 'BTN_RETORNAR_TELA_PRINCIPAL'):
                self.ui.BTN_VOLTAR_TELA_PRINCIPAL.clicked.connect(self.fechar_tela)
            if hasattr(self.ui, "BTN_FILTRO_FUNCS"):
                self.ui.BTN_FILTRO_FUNCS.clicked.connect(self.filtrar_funcs)            
            if hasattr(self.ui, 'BTN_CADASTRAR_FUNCS'):
                self.ui.BTN_CADASTRAR_FUNCS.clicked.connect(self.cadastrar_funcs)            
            if hasattr(self.ui, 'TXT_FILTRO_FUNCS'):
                self.ui.TXT_FILTRO_FUNCS.textChanged.connect(self.filtrar_funcs)
            self.carregar_funcs()
                
        except Exception as e:
            print(f"Erro ao configurar tela de registro: {e}")

    def carregar_funcs(self, filtro=""):
        try:
            if hasattr(self.ui, 'TBW_FUNCS'):
                self.ui.TBW_FUNCS.clear()
                funcionarios = self.db_registro.buscar_funcs(filtro)
                colunas = ["ID", "Nome", "Endereço", "Documento", "Complemento", "Admin"]
                self.ui.TBW_FUNCS.setColumnCount(len(colunas))
                self.ui.TBW_FUNCS.setHeaderLabels(colunas)
                for func in funcionarios:
                    item = QTreeWidgetItem([
                        str(func[0]),  # ID
                        func[1] if len(func) > 1 else "N/D",  # Nome
                        func[2] if len(func) > 2 else "N/D",  # Endereço
                        func[3] if len(func) > 3 else "N/D",  # Documento
                        func[4] if len(func) > 4 else "N/D",  # Complemento
                        "Sim" if func[5] else "Não"])
                    self.ui.TBW_FUNCS.addTopLevelItem(item)
        except Exception as e:
            print(f"Erro ao carregar funcionários: {e}")

    def filtrar_funcs(self):
        try:
            filtro = ""
            if hasattr(self.ui, 'TXT_FILTRO_FUNCS'):
                filtro = self.ui.TXT_FILTRO_FUNCS.text().strip()
                print(f"Filtrando funcionários por: '{filtro}'")         
            self.carregar_funcs(filtro)
            
        except Exception as e:
            print(f"Erro ao filtrar funcionários: {e}")
            QMessageBox.critical(self, "Erro", f"Erro ao filtrar funcionários: {str(e)}")

    def cadastrar_funcs(self):
        try:
            # OBTER OS DADOS DOS CAMPOS CORRETAMENTE
            nome = self.ui.TXT_NOME_FUNCS.text().strip() if hasattr(self.ui, 'TXT_NOME_FUNCS') else ""
            endereco = self.ui.TXT_ENDERECO_FUNCS.text().strip() if hasattr(self.ui, 'TXT_ENDERECO_FUNCS') else ""
            documento = self.ui.TXT_CNPJ_CPF_FUNCS.text().strip() if hasattr(self.ui, 'TXT_CNPJ_CPF_FUNCS') else ""
            complemento = self.ui.TXT_COMPLEMENTO_FUNCS.text().strip() if hasattr(self.ui, 'TXT_COMPLEMENTO_FUNCS') else ""
            if not nome or not endereco or not documento:
                QMessageBox.warning(self, "Atenção", "Preencha todos os campos obrigatórios!")
                return            
            if self.db_registro.add_Cliente(nome, endereco, documento, complemento, 1):
                QMessageBox.information(self, "Sucesso", "Registro cadastrado com sucesso!")
                self.limpar_campos()
                self.carregar_funcs()
            else:
                QMessageBox.critical(self, "Erro", "Erro ao cadastrar registro!")
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao cadastrar registro: {str(e)}")
    
    def buscar_funcs(self):
        try:
            filtro = ""
            if hasattr(self.ui, 'TXT_FILTRO_FUNCS'):
                filtro = self.ui.TXT_FILTRO_FUNCS.text().strip()
            self.carregar_funcs(filtro)
            
        except Exception as e:
            print(f"Erro na busca de funcionários: {e}")
    
    def limpar_campos(self):
        try:
            campos = [
                'TXT_NOME_FUNCS', 'TXT_ENDERECO_FUNCS', 
                'TXT_CNPJ_CPF_FUNCS', 'TXT_COMPLEMENTO_FUNCS']
            for campo in campos:
                if hasattr(self.ui, campo):
                    widget = getattr(self.ui, campo)
                    if hasattr(widget, 'clear'):
                        widget.clear()
            if hasattr(self.ui, 'TXT_FILTRO_FUNCS'):
                self.ui.TXT_FILTRO_FUNCS.clear()
                
            print("Campos limpos com sucesso!")
            
        except Exception as e:
            print(f"Erro ao limpar campos: {e}")

    def fechar_tela(self):
        try:
            if hasattr(self, 'db_registro') and self.db_registro:
                self.db_registro.fechar_conexao()
            self.close()
        except Exception as e:
            print(f"Erro ao fechar tela: {e}")
            self.close()

class TelaVenda(TelaArrastavelBase):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_telaVendas()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowIcon(QtGui.QIcon("Accets/icons/icons/logoSpike.png"))
        self.setGeometry(300, 150, 800, 600)
        self.db_vendas = sqlite_db("db/sistema.db")
        self.configurar_tela_vendas()

    def configurar_tela_vendas(self):
        try:
            if hasattr(self.ui, 'BTN_RETORNAR_TELA_PRINCIPAL'):
                self.ui.BTN_FECHAR.clicked.connect(self.fechar_tela)
            if hasattr(self.ui, 'BTN_NOVA_VENDA'):
                self.ui.BTN_NOVA_VENDA.clicked.connect(self.abrir_tela_estoque)                
        
        except Exception as e:
            print(f"Erro ao configurar tela de vendas: {e}")

    def abrir_tela_estoque(self):
        try:
            self.tela_estoque = TelaEstoque(self)
            self.tela_estoque.destroyed.connect(self.on_tela_estoque_fechada)
            self.tela_estoque.show()
            
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao abrir tela de estoque: {str(e)}")
            print(f"Erro detalhado: {traceback.format_exc()}")        
          
    def on_tela_estoque_fechada(self):
        print("Tela ficha estoque fechada")
     
    def fechar_tela(self):
        self.db_vendas.fechar_conexao()
        self.close()

class TelaPedido(TelaArrastavelBase):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_telaProduto()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowIcon(QtGui.QIcon("icons/logoSpike.png"))
        self.setGeometry(300, 150, 800, 600)    

        self.db = SqliteDb("db/sistema.db")
        
        os.makedirs("arquivo", exist_ok=True)
        self.carregar_dados_pedido()
        self.configurar_tela()
        self.configurar_tree_widget_pedidos()
        self.conectar_botoes_pedido()


    def configurar_tela(self):
        try:
            self.conectar_botoes_pedido()
            self.configurar_tree_widget_pedidos()
            self.carregar_dados_pedido()
            self.atualizar_resumo_pedidos()
        except Exception as e:
            print(f"Erro ao configurar tela pedidos: {e}")
            QMessageBox.critical(self, "Erro", f"Erro ao configurar tela: {str(e)}")
    
    def conectar_botoes_pedido(self):
        try:
            if hasattr(self.ui, 'BTN_PROCURAR_PRODUTO'):
                self.ui.BTN_PROCURAR_PRODUTO.clicked.connect(self.buscar_pedido)
            if hasattr(self.ui, 'BTN_EXCLUIR_PRODUTO'):
                self.ui.BTN_EXCLUIR_PRODUTO.clicked.connect(self.excluir_pedido)
            if hasattr(self.ui, 'BTN_PRODUTO'):
                self.ui.BTN_PRODUTO.clicked.connect(self.novo_pedido)
            if hasattr(self.ui, 'BTN_VOLTAR'):
                self.ui.BTN_VOLTAR.clicked.connect(self.fechar_tela)
            if hasattr(self.ui, 'TXT_FILTRO_PEDIDOS'):
                self.ui.TXT_FILTRO_PEDIDOS.textChanged.connect(self.buscar_pedido)
        except Exception as e:
            print(f"Erro ao conectar botões: {e}")
        
    def configurar_tree_widget_pedidos(self):
        try:
            if hasattr(self.ui, 'TBW_PRODUTOS'):
                colunas = ["ID", "Nome", "Produto", "Quantidade", "Valor Unitário", "Total", "Status", "Data"]
                self.ui.TBW_PRODUTOS.setColumnCount(len(colunas))
                self.ui.TBW_PRODUTOS.setHeaderLabels(colunas)
                larguras = [50, 150, 150, 80, 100, 100, 100, 120]
                for i in range(len(colunas)):
                    self.ui.TBW_PRODUTOS.setColumnWidth(i, larguras[i])
                
                self.ui.TBW_PRODUTOS.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
                print("Tree widget de pedidos configurado com sucesso")
        except Exception as e:
            print(f"Erro ao configurar tree widget: {e}")

    def buscar_pedido_banco(self, filtro=""):
        try:
            if self.db and self.db.conn:
                pedidos = self.db.buscar_pedido()
                resultado_formatado = []
                for pedido in pedidos:
                    # Obter itens do pedido
                    itens = self.db.buscar_itens_pedido(pedido[0])
                    for item in itens:
                        resultado_formatado.append((
                            pedido[0],  # id_pedido
                            pedido[5],  # cliente_nome
                            item[1],    # produto_nome
                            item[3],    # quantidade
                            item[4],    # preco_unitario
                            pedido[3],  # status (corrigido para índice 3)
                            pedido[1],  # data_pedido (corrigido para índice 1)
                            pedido[5]))
                if filtro:
                    resultado_filtrado = []
                    for pedido in resultado_formatado:
                        if (filtro.lower() in str(pedido[1]).lower() or  # cliente
                            filtro.lower() in str(pedido[2]).lower() or  # produto
                            filtro.lower() in str(pedido[5]).lower()):   # status
                            resultado_filtrado.append(pedido)
                    return resultado_filtrado
                return resultado_formatado
            else:
                print("Erro: Conexão com banco de dados não está disponível")
                return []
        except Exception as e:
            print(f"❌ Erro ao buscar pedidos: {e}")
            return []

    def carregar_dados_pedido(self, filtro=""):
        try:
            if hasattr(self.ui, 'TBW_PRODUTOS'):
                self.ui.TBW_PRODUTOS.clear()
                pedidos = self.buscar_pedido_banco(filtro)
                print(f"Encontrados {len(pedidos)} pedidos")
                for pedido in pedidos:
                    try:
                        quantidade = int(pedido[3]) if pedido[3] is not None else 0
                    except:
                        quantidade = 0
                    try:
                        valor_unitario = float(pedido[4]) if pedido[4] is not None else 0.0
                    except:
                        valor_unitario = 0.0
                    total = quantidade * valor_unitario
                    data_pedido = pedido[6] if len(pedido) > 6 and pedido[6] is not None else "N/D"
                    if data_pedido and data_pedido != "N/D" and " " in data_pedido:
                        data_pedido = data_pedido.split(" ")[0]
                    
                    item = QTreeWidgetItem([
                        str(pedido[0]),  # ID
                        str(pedido[1]),  # Nome do Cliente
                        str(pedido[2]),  # Produto
                        str(quantidade),  # Quantidade
                        f"R$ {valor_unitario:.2f}",  # Valor Unitário
                        f"R$ {total:.2f}",  # Total
                        str(pedido[5]),  # Status
                        str(data_pedido)])
                    status = str(pedido[5]) if len(pedido) > 5 and pedido[5] is not None else ""
                    if status.lower() == "entregue":
                        for i in range(8):
                            item.setForeground(i, QtGui.QBrush(QtGui.QColor("green")))
                    elif status.lower() == "pendente":
                        for i in range(8):
                            item.setForeground(i, QtGui.QBrush(QtGui.QColor("orange")))
                    elif status.lower() == "cancelado":
                        for i in range(8):
                            item.setForeground(i, QtGui.QBrush(QtGui.QColor("red")))
                    elif status.lower() == "processando":
                        for i in range(8):
                            item.setForeground(i, QtGui.QBrush(QtGui.QColor("blue")))
                    else:
                        for i in range(8):
                            item.setForeground(i, QtGui.QBrush(QtGui.QColor("black")))
                    self.ui.TBW_PRODUTOS.addTopLevelItem(item)
                if len(pedidos) == 0:
                    item = QTreeWidgetItem(["", "Nenhum pedido encontrado", "", "", "", "", "", ""])
                    for i in range(8):
                        item.setForeground(i, QtGui.QBrush(QtGui.QColor("gray")))
                    self.ui.TBW_PRODUTOS.addTopLevelItem(item)
                    print("Nenhum pedido encontrado no banco")
                else:
                    print(f"Carregados {len(pedidos)} pedidos com sucesso")
        except Exception as e:
            print(f"Erro ao carregar pedidos: {e}")
            QMessageBox.critical(self, "Erro", f"Erro ao carregar pedidos: {str(e)}")

    def atualizar_resumo_pedidos(self):
        try:
            if not self.db or not self.db.conn:
                print("Erro: Conexão com banco não disponível")
                return
            pedidos = self.db.buscar_pedido()
            total_pedidos = len(pedidos)
            pedidos_pendentes = sum(1 for pedido in pedidos if str(pedido[3]).lower() == "pendente")
            pedidos_entregues = sum(1 for pedido in pedidos if str(pedido[3]).lower() == "entregue")
            valor_total = 0
            for pedido in pedidos:
                pedido_id = pedido[0]
                itens = self.db.buscar_itens_pedido(pedido_id)
                for item in itens:
                    valor_total += item[5] 
            print(f"Resumo - Total: {total_pedidos}, Pendentes: {pedidos_pendentes}, Entregues: {pedidos_entregues}, Valor: R$ {valor_total:.2f}")
            if hasattr(self.ui, "label_total_pedidos"):
                self.ui.label_total_pedidos.setText(f"Total: {total_pedidos}")
            if hasattr(self.ui, "label_pedidos_pendentes"):
                self.ui.label_pedidos_pendentes.setText(f"Pendentes: {pedidos_pendentes}")
            if hasattr(self.ui, "label_pedidos_entregues"):
                self.ui.label_pedidos_entregues.setText(f"Entregues: {pedidos_entregues}")
            if hasattr(self.ui, "label_valor_total"):
                self.ui.label_valor_total.setText(f"Valor Total: R$ {valor_total:.2f}")
        except Exception as e:
            print(f"Erro ao atualizar resumo de pedidos: {e}")

    def buscar_pedido(self):
        try:
            filtro = ""
            if hasattr(self.ui, 'TXT_FILTRO_PEDIDOS'):
                filtro = self.ui.TXT_FILTRO_PEDIDOS.text().strip()
                print(f"🔍 Buscando pedidos com filtro: '{filtro}'")
            self.carregar_dados_pedido(filtro)
            
        except Exception as e:
            print(f"❌ Erro na busca de pedidos: {e}")
            QMessageBox.critical(self, "Erro", f"Erro ao buscar pedidos:\n{str(e)}")
    
    def novo_pedido(self):
        try:
            print("Abrindo formulário para novo pedido")
            if not self.db or not self.db.conn:
                QMessageBox.critical(self, "Erro", "Conexão com banco de dados não disponível")
                return
            
            # Buscar clientes
            self.db.cursor.execute("SELECT id, nome FROM pedidos ORDER BY nome")
            pedidos = self.db.cursor.fetchall()
            
            if not pedidos:
                QMessageBox.warning(self, "Aviso", "Não há pedidos cadastrados. Cadastre um pedido primeiro.")
                return
            pedidos_lista = [f"{cliente[1]} (ID: {cliente[0]})" for cliente in pedidos]
            pedidos_selecionado, ok = QInputDialog.getItem(
                self, 
                "Selecionar Cliente", 
                "Escolha o cliente:", 
                pedidos_lista, 
                0, 
                False)
            if not ok or not pedidos_selecionado:
                return
            cliente_id = int(pedidos_selecionado.split("(ID: ")[1].replace(")", ""))
            self.db.cursor.execute("SELECT id, nome, preco, estoque FROM produtos ORDER BY nome")
            produtos = self.db.cursor.fetchall()
            if not produtos:
                QMessageBox.warning(self, "Aviso", "Não há produtos cadastrados. Cadastre produtos primeiro.")
                return
            produtos_lista = [f"{produto[1]} - R$ {produto[2]:.2f} (Estoque: {produto[3]})" for produto in produtos]
            produto_selecionado, ok = QInputDialog.getItem(self,
                "Selecionar Produto",
                "Escolha o produto:",
                produtos_lista,
                0,
                False)
            if not ok or not produto_selecionado:
                return
            produto_index = produtos_lista.index(produto_selecionado)
            produto_id = produtos[produto_index][0]
            produto_preco = produtos[produto_index][2]
            produto_estoque = produtos[produto_index][3]
            quantidade, ok = QInputDialog.getInt(
                self, 
                "Quantidade", 
                f"Digite a quantidade (estoque disponível: {produto_estoque}):", 
                value=1, 
                min=1, 
                max=produto_estoque, 
                step=1)
            if not ok:
                return
            status, ok = QInputDialog.getItem(
                self,
                "Status do Pedido",
                "Selecione o status:",
                ["pendente", "processando", "enviado", "entregue", "cancelado"],
                0,
                False)
            if not ok:
                return
            forma_pagamento, ok = QInputDialog.getItem(
                self,
                "Forma de Pagamento",
                "Selecione a forma de pagamento:",
                ["cartao", "boleto", "pix", "transferencia"],
                0,
                False)
            if not ok:
                return
            produtos_list = [{'id': produto_id, 'quantidade': quantidade}]
            pedido_id, mensagem = self.db.criar_pedido(
                cliente_id,
                produtos_list,
                forma_pagamento,
                status=status)
            if pedido_id:
                QMessageBox.information(
                    self, 
                    "Sucesso", 
                    f"✅ Pedido #{pedido_id} criado com sucesso!\n\n"
                    f"📦 Produto: {produto_selecionado}\n"
                    f"🔢 Quantidade: {quantidade}\n"
                    f"💰 Valor Unitário: R$ {produto_preco:.2f}\n"
                    f"💵 Total: R$ {quantidade * produto_preco:.2f}\n"
                    f"📊 Status: {status}\n"
                    f"💳 Pagamento: {forma_pagamento}")
                self.carregar_dados_pedido()
                self.atualizar_resumo_pedidos()
            else:
                QMessageBox.critical(self, "Erro", f"❌ Erro ao criar pedido: {mensagem}")
        except Exception as e:
            print(f"Erro ao criar novo pedido: {e}")
            QMessageBox.critical(self, "Erro", f"❌ Erro ao criar pedido: {str(e)}")

    def excluir_pedido(self):
        try:
            current_item = self.ui.TBW_PRODUTOS.currentItem() if hasattr(self.ui, 'TBW_PRODUTOS') else None
            if not current_item:
                QMessageBox.warning(self, "Aviso", "Nenhum pedido selecionado!")
                return
            
            pedido_id = current_item.text(0) 
            produto_nome = current_item.text(2)
            if not pedido_id or pedido_id == "" or produto_nome == "Nenhum pedido encontrado":
                QMessageBox.warning(self, "Aviso", "Selecione um pedido válido!")
                return
            reply = QMessageBox.question(self, "Confirmação", 
                                       f"Tem certeza que deseja excluir o pedido #{pedido_id}?\n{produto_nome}?",
                                       QMessageBox.Yes | QMessageBox.No)
            if reply == QMessageBox.Yes:
                try:
                    self.db.cursor.execute("DELETE FROM pedido_itens WHERE pedido_id = ?", (pedido_id,))
                    self.db.cursor.execute("DELETE FROM pedidos WHERE id = ?", (pedido_id,))
                    self.db.conn.commit()
                    QMessageBox.information(self, "Sucesso", "Pedido excluído com sucesso!")
                    self.carregar_dados_pedido()  
                    self.atualizar_resumo_pedidos()
                except Exception as e:
                    self.db.conn.rollback()
                    QMessageBox.critical(self, "Erro", f"Erro ao excluir pedido: {str(e)}")
        except Exception as e:
            print(f"Erro ao excluir pedido: {e}")
            QMessageBox.critical(self, "Erro", f"Erro ao excluir pedido: {str(e)}")

    def gerar_relatorio_pedidos(self):
        try:
            if not self.db or not self.db.conn:
                QMessageBox.critical(self, "Erro", "Conexão com banco não disponível")
                return            
            pedidos = self.db.buscar_pedido()
            
            relatorio = f"""
            ===== RELATÓRIO DE PEDIDOS =====
            Data: {datetime.now().strftime('%d/%m/%Y %H:%M')}
            Total de Pedidos: {len(pedidos)}
            
            DETALHES DOS PEDIDOS:
            """
            valor_total = 0
            for pedido in pedidos:
                pedido_id = pedido[0]
                itens = self.db.buscar_itens_pedido(pedido_id)
                
                relatorio += f"""
            ------------------------------------
            Pedido ID: {pedido_id}
            Cliente: {pedido[5]}
            Data: {pedido[1]}
            Status: {pedido[3]}
            Forma de Pagamento: {pedido[4]}
            Total: R$ {pedido[3]:.2f}
            
            Itens:"""
                for item in itens:
                    relatorio += f"""
              • {item[1]} ({item[6]} {item[7]})
                Quantidade: {item[3]}
                Preço Unitário: R$ {item[4]:.2f}
                Subtotal: R$ {item[5]:.2f}"""
                    valor_total += item[5]
            relatorio += f"""
            
            =====================================
            VALOR TOTAL GERAL: R$ {valor_total:.2f}
            =====================================
            """

            os.makedirs("arquivo", exist_ok=True)
            with open('arquivo/relatorio_pedidos.txt', 'w', encoding='utf-8') as f:
                f.write(relatorio)
            QMessageBox.information(self, "Sucesso", "Relatório de pedidos gerado com sucesso!")
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao gerar relatório: {str(e)}")

    def mostrar_conteudo_pedidos(self):
        try:
            arquivo_path = "arquivo/relatorio_pedidos.txt"
            
            if not os.path.exists(arquivo_path):
                # Gerar relatório primeiro se não existir
                self.gerar_relatorio_pedidos()
            
            with open(arquivo_path, 'r', encoding='utf-8') as arquivo:
                conteudo = arquivo.read()

            dialog = QtWidgets.QDialog(self)
            dialog.setWindowTitle("Relatório de Pedidos")
            dialog.resize(700, 500)
            dialog.setStyleSheet("background-color: #ffffff;")
            layout = QVBoxLayout(dialog)
            
            titulo_label = QtWidgets.QLabel("📋 RELATÓRIO DE PEDIDOS")
            titulo_label.setStyleSheet("font-size: 16px; font-weight: bold; background-color: #ffffff; color: #000000; margin: 10px;")
            titulo_label.setAlignment(QtCore.Qt.AlignCenter)
            layout.addWidget(titulo_label)
            
            text_edit = QTextEdit()
            text_edit.setPlainText(conteudo)
            text_edit.setReadOnly(True)
            text_edit.setStyleSheet("""
                QTextEdit {
                    font-family: 'Courier New';
                    font-size: 12px;
                    color: #000000;
                    background-color: #ffffff;
                    border: 1px solid #ddd;
                    border-radius: 5px;
                    padding: 10px;
}""")
            
            btn_layout = QtWidgets.QHBoxLayout()
            btn_fechar = QPushButton("Fechar")
            btn_fechar.clicked.connect(dialog.close)
            btn_fechar.setStyleSheet("""
                QPushButton {
                    background-color: #e74c3c;
                    color: white;
                    border: none;
                    padding: 8px 16px;
                    border-radius: 4px;
                    font-weight: bold;}
                QPushButton:hover {
                    background-color: #C06156FF;}""")
            btn_exportar = QPushButton("Exportar")
            btn_exportar.clicked.connect(lambda: self.exportar_arquivo_pedidos(arquivo_path))
            btn_exportar.setStyleSheet("""
                QPushButton {
                    background-color: #3498db;
                    color: white;
                    border: none;
                    padding: 8px 16px;
                    border-radius: 4px;
                    font-weight: bold;}
                QPushButton:hover {
                    background-color: #6B9AB9FF;}""")
            btn_limpar = QPushButton("Limpar Arquivo")
            btn_limpar.clicked.connect(lambda: self.limpar_arquivo_pedidos(arquivo_path, dialog))
            btn_limpar.setStyleSheet("""
                QPushButton {
                    background-color: #f39c12;
                    color: white;
                    border: none;
                    padding: 8px 16px;
                    border-radius: 4px;
                    font-weight: bold;}
                QPushButton:hover {
                    background-color: #d35400;}""")
            btn_layout.addWidget(btn_exportar)
            btn_layout.addWidget(btn_limpar)
            btn_layout.addWidget(btn_fechar)
            layout.addWidget(text_edit)
            layout.addLayout(btn_layout)
            dialog.exec_()
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao ler arquivo de pedidos: {str(e)}")

    def exportar_arquivo_pedidos(self, arquivo_path):
        try:
            from PyQt5.QtWidgets import QFileDialog
            import shutil
            destino, _ = QFileDialog.getSaveFileName(
                self, "Exportar Arquivo", "relatorio_pedidos_backup.txt", "Arquivos de Texto (*.txt)")
            if destino:
                shutil.copy2(arquivo_path, destino)
                QMessageBox.information(self, "Sucesso", f"Arquivo exportado para:\n{destino}")
                
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao exportar arquivo: {str(e)}")

    def limpar_arquivo_pedidos(self, arquivo_path, dialog):
        try:
            resposta = QMessageBox.question(
                self, 
                "Confirmar Limpeza", 
                "Tem certeza que deseja limpar todo o conteúdo do arquivo de pedidos?",
                QMessageBox.Yes | QMessageBox.No)
            if resposta == QMessageBox.Yes:
                with open(arquivo_path, 'w', encoding='utf-8') as arquivo:
                    arquivo.write("===== RELATÓRIO DE PEDIDOS =====\n")
                    arquivo.write(f"Arquivo limpo em: {datetime.now().strftime('%d/%m/%Y %H:%M')}\n")
                    arquivo.write("Nenhum pedido cadastrado.\n")
                    arquivo.write("==============================\n")
                QMessageBox.information(self, "Sucesso", "Arquivo limpo com sucesso!")
                dialog.close()
                self.mostrar_conteudo_pedidos()
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao limpar arquivo: {str(e)}")

    def limpar_campos_pedido(self):
        try:
            # Limpar campos de texto se existirem
            campos = ['TXT_FILTRO_PEDIDOS']
            for campo in campos:
                if hasattr(self.ui, campo):
                    widget = getattr(self.ui, campo)
                    if hasattr(widget, 'clear'):
                        widget.clear()
                        
            print("Campos de pedido limpos com sucesso!")
            
        except Exception as e:
            print(f"Erro ao limpar campos: {e}")

    def fechar_tela(self):
        try:
            if hasattr(self, 'db') and self.db:
                self.db.close()
            self.close()
        except Exception as e:
            print(f"Erro ao fechar tela: {e}")
            self.close()

class BancoDados(TelaArrastavelBase):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_telaBancodedados()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowIcon(QtGui.QIcon("Accets/icons/icons/logoSpike.png"))
        self.setGeometry(230, 100, 800, 600)
        
        # CORREÇÃO: Usar apenas UMA conexão com o banco
        self.db = sqlite_db("db/sistema.db") 
        os.makedirs("arquivo", exist_ok=True)

        self.configurar_tela_funcs()
        self.carregar_dados_funcs()
        self.carregar_dados_cliente()
        self.configurar_tela_cliente()

    def configurar_tela_funcs(self):
        try:
            self.conectar_botoes_consulta_funcs()            
        except Exception as e:
            print(f"Erro ao configurar tela cliente: {e}")
   
    ### FUNÇÃO BANCO DE DADOS FUNCS
    def carregar_dados_funcs(self):
        try:
            self.pesquisar_funcs()
        except Exception as e:
            print(f"Erro ao carregar dados funcs: {e}")

    def conectar_botoes_consulta_funcs(self):
        try:
            if hasattr(self.ui, 'BTN_FILTRO_FUNCS'):
                self.ui.BTN_FILTRO_FUNCS.clicked.connect(self.pesquisar_funcs)
            if hasattr(self.ui, 'TXT_FILTRO_FUNCS'):
                self.ui.TXT_FILTRO_FUNCS.textChanged.connect(self.filtrar_funcs)
        except Exception as e:
            print(f"Erro ao conectar botões funcs: {e}")

    def preencher_tabela_funcs(self, funcs):
        try:
            if not hasattr(self.ui, 'TBW_FUNCS'):
                print("Widget TBW_FUNCS não encontrado")
                return   
            self.ui.TBW_FUNCS.clear()
            colunas = ["ID", "Nome", "Endereço", "Documento", "Complemento", "Admin"]
            self.ui.TBW_FUNCS.setColumnCount(len(colunas))
            self.ui.TBW_FUNCS.setHeaderLabels(colunas)
            
            for func in funcs:
                item = QTreeWidgetItem([
                    str(func[0]),  
                    func[1],       
                    func[2],       
                    func[3],      
                    func[4],      
                    "Sim" if func[5] else "Não" ])
                self.ui.TBW_FUNCS.addTopLevelItem(item)
        except Exception as e:
            print(f"Erro ao preencher tabela funcs: {e}")

    def pesquisar_funcs(self):
        try:
            filtro = ""
            if hasattr(self.ui, 'TXT_FILTRO_FUNCS'):
                filtro = self.ui.TXT_FILTRO_FUNCS.text().strip()
            funcs = self.db.buscar_funcs(filtro)
            self.preencher_tabela_funcs(funcs)
        except Exception as e:
            print(f"Erro na pesquisa funcs: {e}")

    def filtrar_funcs(self):
        try:
            self.pesquisar_funcs()
        except Exception as e:
            print(f"Erro no filtro funcs: {e}")
    
    def fechar_tela_funcs(self):
        self.db.fechar_conexao() 
        self.close()
    
    ### FUNÇÃO DO BANCO DE DADOS CLIENTE
    def configurar_tela_cliente(self):
        try:
            self.conectar_botoes_consulta_cliente()            
        except Exception as e:
            print(f"Erro ao configurar tela cliente: {e}")

    def conectar_botoes_consulta_cliente(self):
        try:
            if hasattr(self.ui, 'TXT_FILTRO_CLIENTE'):
                self.ui.TXT_FILTRO_CLIENTE.textChanged.connect(self.filtrar_clientes)
        except Exception as e:
            print(f"Erro ao conectar botões cliente: {e}")

    def carregar_dados_cliente(self):
        try:
            self.pesquisar_clientes()
        except Exception as e:
            print(f"Erro ao carregar dados cliente: {e}")

    def preencher_tabela_clientes(self, clientes):
        try:
            if not hasattr(self.ui, 'TBW_CLIENTES'):
                print("Widget TBW_CLIENTES não encontrado")
                return
            
            self.ui.TBW_CLIENTES.clear()
            colunas = ["ID", "Nome", "Endereço", "Documento", "Complemento", "Status"]
            self.ui.TBW_CLIENTES.setColumnCount(len(colunas))
            self.ui.TBW_CLIENTES.setHeaderLabels(colunas)
            
            for cliente in clientes:
                item = QTreeWidgetItem([
                    str(cliente[0]),  # ID
                    cliente[1],       # Nome
                    cliente[2],       # Endereço
                    cliente[3],       # Documento
                    cliente[4],       # Complemento
                    "Ativo" if cliente[5] else "Inativo"])
                self.ui.TBW_CLIENTES.addTopLevelItem(item)
        except Exception as e:
            print(f"Erro ao preencher tabela clientes: {e}")

    def pesquisar_clientes(self):
        try:
            filtro = ""
            if hasattr(self.ui, 'TXT_FILTRO_CLIENTE'):
                filtro = self.ui.TXT_FILTRO_CLIENTE.text().strip()
            clientes = self.db.buscar_clientes(filtro)  # CORREÇÃO: usar self.db
            self.preencher_tabela_clientes(clientes) 
        except Exception as e:
            print(f"Erro na pesquisa clientes: {e}")

    def filtrar_clientes(self):
        try:
            self.pesquisar_clientes()
        except Exception as e:
            print(f"Erro no filtro clientes: {e}")

    def fechar_tela_cliente(self):
        self.db.fechar_conexao() 
        self.close()
   
class TelaGrafico(TelaArrastavelBase):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_telaGrafico()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowIcon(QtGui.QIcon("Accets/icons/icons/logoSpike.png"))
        self.setGeometry(300, 150, 600, 400)
        self.mostrar_o_grafico()
        
    def mostrar_o_grafico(self):
        try:
            self.numero_1 = 100
            self.numero_2 = 235
            self.soma = self.numero_1 + self.numero_2
            if hasattr(self.ui, 'TABELA_GRAFICO'):
                container = self.ui.TABELA_GRAFICO
                self.limpar_container(container)
                self.figura = Figure(figsize=(6, 4), dpi=80)
                self.canvas = FigureCanvas(self.figura)
                self.ax = self.figura.add_subplot(111)
                categorias = ['Número 1', 'Número 2', 'Soma']
                valores = [self.numero_1, self.numero_2, self.soma]
                cores = ['#3498db', '#2ecc71', '#e74c3c']
                barras = self.ax.bar(categorias, valores, color=cores, width=0.6)
                for barra, valor in zip(barras, valores):
                    altura = barra.get_height()
                    self.ax.text(barra.get_x() + barra.get_width()/2., altura + 5, f'{valor}', ha='center', va='bottom', fontsize=11, fontweight='bold')
                self.ax.set_ylabel('Valores', fontsize=12, fontweight='bold')
                self.ax.set_xlabel('Categorias', fontsize=12, fontweight='bold')
                self.ax.set_title('Gráfico de Números e Soma', fontsize=14, fontweight='bold', pad=15)
                self.ax.grid(True, alpha=0.3, linestyle='--', axis='y')
                self.ax.set_ylim(0, max(valores) * 1.2)                
                self.figura.tight_layout()
                
                if container.layout() is None:
                    layout = QtWidgets.QVBoxLayout(container)
                    layout.setContentsMargins(5, 5, 5, 5)
                else:
                    layout = container.layout()
                layout.addWidget(self.canvas)
                self.canvas.draw()
                print(f"Soma calculada: {self.soma}")
            else:
                self.criar_grafico_dinamico()
        except Exception as e:
            print(f"Erro ao criar gráfico: {str(e)}")
            import traceback
            traceback.print_exc()
            QMessageBox.critical(self, "Erro", f"Erro ao criar gráfico: {str(e)}")
    
    def limpar_container(self, container):
        if container.layout() is not None:
            while container.layout().count():
                item = container.layout().takeAt(0)
                if item.widget():
                    item.widget().deleteLater()
        else:
            for child in container.children():
                if isinstance(child, QtWidgets.QWidget):
                    child.deleteLater()
    
    def criar_grafico_dinamico(self):
        try:
            print("TABELA_GRAFICO não encontrado. Criando gráfico dinâmico...")
            container = QtWidgets.QWidget(self)
            container.setObjectName("grafico_dinamico")
            container.setGeometry(20, 20, 560, 360)
            container.setStyleSheet("background-color: #f8f9fa; border: 1px solid #dee2e6; border-radius: 8px;")
            figura = Figure(figsize=(5.5, 4), dpi=80)
            canvas = FigureCanvas(figura)
            ax = figura.add_subplot(111)
            self.numero_1 = 100
            self.numero_2 = 235
            self.soma = self.numero_1 + self.numero_2
            categorias = ['Número 1', 'Número 2', 'Soma']
            valores = [self.numero_1, self.numero_2, self.soma]
            cores = ['#3498db', '#2ecc71', '#e74c3c']
            explode = (0.05, 0.05, 0.05)  # Separar as fatias 
            wedges, texts, autotexts = ax.pie(valores, explode=explode, colors=cores, autopct='%1.1f%%', shadow=True, startangle=90)
            ax.set_title('Distribuição dos Valores', fontsize=14, fontweight='bold', pad=20)
            ax.legend(wedges, categorias, title="Categorias", loc="center left", 
                     bbox_to_anchor=(1, 0, 0.5, 1))
            layout = QtWidgets.QVBoxLayout(container)
            layout.setContentsMargins(10, 10, 10, 10)
            layout.addWidget(canvas)
            container.show()
            print(f"Soma calculada: {self.soma}")
        except Exception as e:
            print(f"Erro ao criar gráfico dinâmico: {str(e)}")

    def fechar_tela(self):
        self.close()

class OrdemServicos(TelaArrastavelBase):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_telaOrdemservicos()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowIcon(QtGui.QIcon("Accets/icons/logoSpike.png"))  
        self.setGeometry(300, 150, 800, 600)        
        # Inicializa o banco de dados
        self.db = SqliteDb("db/sistema.db")       
        os.makedirs("arquivo", exist_ok=True)       
        self.os_selecionada = None
        self.preencher_tabela_ordem_servico()
        self.configurar_tree_widget_ordem_servicos()
        self.conectar_botoes_ordem_Servicos()
        self.carregar_ordem_servicos()
        
        # Conectar clique na tabela para selecionar OS
        self.ui.TBW_ORDENS_DE_SERVICOS.itemClicked.connect(self.selecionar_os_na_tabela)

    def conectar_botoes_ordem_Servicos(self):
        # BOTOES DE ORDEM DE SERVIÇOS
        self.ui.BTN_CADASTRAR_ORDEM_DE_SERVICOS.clicked.connect(self.salvar_relatorio_completo_os)
        self.ui.BTN_GERAR_ORDEM_DE_SERVICOS.clicked.connect(self.gerar_relatorio_equipamento)
        self.ui.BTN_MOSTRAR_OS.clicked.connect(self.mostrar_conteudo_os_selecionada)
        self.ui.BTN_EXCLUIR_ORDENS_DE_SERVICOS.clicked.connect(self.excluir_ordem_servico)
        self.ui.BTN_VOLTAR_TELA_PRINCIPAL.clicked.connect(self.fechar_tela)
        self.ui.BTN_FILTRO_ORDEM_DE_SERVICOS.clicked.connect(self.filtrar_ordem_servicos)
    
    def selecionar_os_na_tabela(self, item):
        try:
            valor_original = item.data(8, QtCore.Qt.UserRole)
            if valor_original is None:
                texto_formatado = item.text(8)
                try:
                    valor_texto = texto_formatado.replace("R$", "").replace(",", ".").strip()
                    valor_original = float(valor_texto) if valor_texto.replace('.', '', 1).isdigit() else 0.0
                except:
                    valor_original = 0.0
            self.os_selecionada = {
                'id': item.text(0),
                'tipo_equipamento': item.text(1),
                'numero_serie': item.text(2),
                'numero_placa': item.text(3) if item.columnCount() > 3 else "",
                'revisao': item.text(6) if item.columnCount() > 6 else "",
                'etiqueta': item.text(4) if item.columnCount() > 4 else "",
                'backup': item.text(5) if item.columnCount() > 5 else "",
                'data': item.text(7) if item.columnCount() > 7 else "",
                'valor_do_reparo': valor_original,  # VALOR ORIGINAL (float), não formatado
                'relatorio': item.text(9) if item.columnCount() > 9 else ""}
            for i in range(self.ui.TBW_ORDENS_DE_SERVICOS.topLevelItemCount()):
                current_item = self.ui.TBW_ORDENS_DE_SERVICOS.topLevelItem(i)
                for j in range(current_item.columnCount()):
                    current_item.setBackground(j, QtGui.QBrush(Qt.white))
                    current_item.setForeground(j, QtGui.QBrush(Qt.black))
            for i in range(item.columnCount()):
                item.setBackground(i, QtGui.QBrush(QtGui.QColor("#3498db")))
                item.setForeground(i, QtGui.QBrush(Qt.white))
            try:
                self.ui.DBS_VALOR_DO_REPARO_OREDEM_DE_SERVICOS.setValue(valor_original)
                print(f"Valor do reparo da OS {self.os_selecionada['id']}: R$ {valor_original:.2f}")
            except Exception as e:
                print(f"Erro ao definir valor na spinbox: {e}")
                self.ui.DBS_VALOR_DO_REPARO_OREDEM_DE_SERVICOS.setValue(0.0)
            print(f"OS {self.os_selecionada['id']} selecionada: {self.os_selecionada['tipo_equipamento']}")
        except Exception as e:
            print(f"Erro ao selecionar OS: {e}")
 
    def mostrar_conteudo_os_selecionada(self):
        try:
            if not self.os_selecionada:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setWindowTitle("Aviso")
                msg.setText("Por favor, selecione uma OS na tabela primeiro!")
                msg.setStyleSheet("""
                    QMessageBox {
                        background-color: white;
                        color: black;}
                    QMessageBox QLabel {
                        color: black;}
                    QPushButton {
                        background-color: #f0f0f0;
                        color: black;
                        border: 1px solid #ccc;
                        padding: 5px 15px;
                        border-radius: 3px;}
                    QPushButton:hover {
                        background-color: #e0e0e0;}""")
                msg.exec_()
                return            
            relatorio = f"""
            ===== DETALHES DA ORDEM DE SERVIÇO =====
            
            ID: {self.os_selecionada['id']}
            Data: {self.os_selecionada['data']}
            
            EQUIPAMENTO:
            - Tipo: {self.os_selecionada['tipo_equipamento']}
            - N° Série: {self.os_selecionada['numero_serie']}
            - N° Placa: {self.os_selecionada['numero_placa']}
            - Valor do Reparo: {self.os_selecionada['valor_do_reparo']}
            - Revisão: {self.os_selecionada['revisao']}
            
            INFORMAÇÕES ADICIONAIS:
            - Etiqueta: {self.os_selecionada['etiqueta']}
            - Backup: {self.os_selecionada['backup']}
            - Relatório: {self.os_selecionada['relatorio']}
            
            STATUS: Ativa
            
            ========================================
            Data de consulta: {datetime.now().strftime('%d/%m/%Y %H:%M')}
            """
            
            dialog = QtWidgets.QDialog(self)
            dialog.setWindowTitle(f"OS #{self.os_selecionada['id']} - {self.os_selecionada['tipo_equipamento']}")
            dialog.resize(600, 400)
            dialog.setStyleSheet("""
                background-color: white;
                color: black;""")
            layout = QVBoxLayout(dialog)
            titulo_label = QtWidgets.QLabel(f"📋 DETALHES DA OS #{self.os_selecionada['id']}")
            titulo_label.setStyleSheet("""
                font-size: 18px; 
                font-weight: bold; 
                color: black; 
                margin: 10px;
                padding: 10px;
                background-color: #f8f9fa;
                border-radius: 5px;
                border: 1px solid #dee2e6;""")
            titulo_label.setAlignment(Qt.AlignCenter)
            layout.addWidget(titulo_label)
            text_edit = QTextEdit()
            text_edit.setPlainText(relatorio)
            text_edit.setReadOnly(True)
            text_edit.setStyleSheet("""
                QTextEdit {
                    font-family: 'Courier New';
                    font-size: 12px;
                    color: black;
                    background-color: white;
                    border: 1px solid #ced4da;
                    border-radius: 5px;
                    padding: 15px;
                    margin: 10px;}""")
            btn_layout = QtWidgets.QHBoxLayout()
            btn_exportar_os = QPushButton("📄 Exportar esta OS")
            btn_exportar_os.clicked.connect(lambda: self.exportar_os_especifica(self.os_selecionada))
            btn_exportar_os.setStyleSheet("""
                QPushButton {
                    background-color: #f0f0f0;
                    color: black;
                    border: 1px solid #ced4da;
                    padding: 10px 20px;
                    border-radius: 5px;
                    font-weight: bold;
                    font-size: 12px;}
                QPushButton:hover {
                    background-color: #e2e6ea;}""")
            btn_preencher_campos = QPushButton("✏️ Preencher Campos")
            btn_preencher_campos.clicked.connect(self.preencher_campos_com_os_selecionada)
            btn_preencher_campos.setStyleSheet("""
                QPushButton {
                    background-color: #f0f0f0;
                    color: black;
                    border: 1px solid #ced4da;
                    padding: 10px 20px;
                    border-radius: 5px;
                    font-weight: bold;
                    font-size: 12px;}
                QPushButton:hover {
                    background-color: #e2e6ea;}""")
            
            # Botão fechar
            btn_fechar = QPushButton("❌ Fechar")
            btn_fechar.clicked.connect(dialog.close)
            btn_fechar.setStyleSheet("""
                QPushButton {
                    background-color: #f0f0f0;
                    color: black;
                    border: 1px solid #ced4da;
                    padding: 10px 20px;
                    border-radius: 5px;
                    font-weight: bold;
                    font-size: 12px;}
                QPushButton:hover {
                    background-color: #e2e6ea;}""")
            
            btn_layout.addWidget(btn_exportar_os)
            btn_layout.addWidget(btn_preencher_campos)
            btn_layout.addWidget(btn_fechar)
            
            layout.addWidget(text_edit)
            layout.addLayout(btn_layout)
            
            dialog.exec_()
            
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Erro")
            msg.setText(f"Erro ao mostrar OS: {str(e)}")
            msg.setStyleSheet("""
                QMessageBox {
                    background-color: white;
                    color: black;}
                QMessageBox QLabel {
                    color: black;}
                QPushButton {
                    background-color: #f0f0f0;
                    color: black;
                    border: 1px solid #ccc;
                    padding: 5px 15px;
                    border-radius: 3px;}
                QPushButton:hover {
                    background-color: #e0e0e0;}""")
            msg.exec_()

    def preencher_campos_com_os_selecionada(self):
        try:
            if not self.os_selecionada:
                return
            self.ui.TXT_TIPO_DE_EQUIPAMENTO_ORDEM_DE_SERVICOS.setText(self.os_selecionada['tipo_equipamento'])
            self.ui.TXT_NUMERO_DE_SERIE_EQUIPAMENTO_ORDEM_DE_SERVICOS.setText(self.os_selecionada['numero_serie'])
            self.ui.TXT_REVISAO_DA_PLACA_ORDEM_DE_SERVICOS.setText(self.os_selecionada['revisao'])
            valor_reparo = self.os_selecionada['valor_do_reparo']
            self.ui.DBS_VALOR_DO_REPARO_OREDEM_DE_SERVICOS.setValue(float(valor_reparo))
            if hasattr(self.ui, 'TXT_OBSERVACOES_RELATORIO'):
                self.ui.TXT_OBSERVACOES_RELATORIO.setPlainText(self.os_selecionada['relatorio'])
            backup = self.os_selecionada['backup'].lower()
            if 'com' in backup:
                self.ui.RDB_COM_BACKUP_ORDEM_DE_SERVICOS.setChecked(True)
            elif 'sem' in backup:
                self.ui.RDB_SEM_BACKUP_ORDEM_DE_SERVICOS.setChecked(True)
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Sucesso")
            msg.setText(f"Campos preenchidos com os dados da OS selecionada!\nValor do reparo: R$ {valor_reparo:.2f}")
            msg.setStyleSheet("""
                QMessageBox {
                    background-color: white; color: black;}
                QMessageBox QLabel {
                    color: black;}
                QPushButton {
                    background-color: #f0f0f0; color: black;
                    border: 1px solid #ccc; padding: 5px 15px;
                    border-radius: 3px;}
                QPushButton:hover {
                    background-color: #e0e0e0;}""")
            msg.exec_()   
        except Exception as e:
            print(f"Erro ao preencher campos: {e}")
  
    def exportar_os_especifica(self, os_data):
        try:
            if not os_data:
                return
            formatos = ["Arquivo de Texto (*.txt)", "Arquivo PDF (*.pdf)"]
            formato, ok = QInputDialog.getItem(
                self,
                "Formato de Exportação",
                "Escolha o formato para exportar:",
                formatos,
                0,
                False)
            if not ok:
                return
            if "PDF" in formato:
                self.exportar_os_para_pdf(os_data)
            else:
                self.exportar_os_para_txt(os_data)
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Erro")
            msg.setText(f"Erro ao exportar OS: {str(e)}")
            msg.setStyleSheet("""
                QMessageBox {
                    background-color: white;
                    color: black;}
                QMessageBox QLabel {
                    color: black;}
                QPushButton {
                    background-color: #f0f0f0;
                    color: black;
                    border: 1px solid #ccc;
                    padding: 5px 15px;
                    border-radius: 3px;}
                QPushButton:hover {
                    background-color: #e0e0e0;}""")
            msg.exec_()

    def exportar_os_para_txt(self, os_data):
        try:
            # Gera nome do arquivo
            nome_arquivo = f"OS_{os_data['id']}_{os_data['tipo_equipamento'].replace(' ', '_')}.txt"
            
            # Gera o conteúdo
            conteudo = f"""
    ===== ORDEM DE SERVIÇO =====

    ID: {os_data['id']}
    Data da OS: {os_data['data']}
    Data de Exportação: {datetime.now().strftime('%d/%m/%Y %H:%M')}

    DADOS DO EQUIPAMENTO:
    - Tipo: {os_data['tipo_equipamento']}
    - N° Série: {os_data['numero_serie']}
    - N° Placa: {os_data['numero_placa']}
    - Valor do Reparo: {os_data['valor_do_reparo']}
    - Revisão: {os_data['revisao']}

    INFORMAÇÕES:
    - Etiqueta: {os_data['etiqueta']}
    - Configuração Backup: {os_data['backup']}
    - Relatório: {os_data['relatorio']}

    EXPEDIDO por MVDevteam@2025

    =====================================
    """
            
            # Solicita local para salvar
            destino, _ = QFileDialog.getSaveFileName(
                self, 
                "Exportar OS como TXT", 
                nome_arquivo, 
                "Arquivos de Texto (*.txt)")
            if destino:
                with open(destino, 'w', encoding='utf-8') as f:
                    f.write(conteudo)
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle("Sucesso")
                msg.setText(f"OS #{os_data['id']} exportada como TXT!\n\n"
                        f"Arquivo: {os.path.basename(destino)}\n"
                        f"Local: {destino}")
                msg.setStyleSheet("""
                    QMessageBox {
                        background-color: white;
                        color: black;}
                    QMessageBox QLabel {
                        color: black;}
                    QPushButton {
                        background-color: #f0f0f0;
                        color: black;
                        border: 1px solid #ccc;
                        padding: 5px 15px;
                        border-radius: 3px;}
                    QPushButton:hover {
                        background-color: #e0e0e0;}""")
                msg.exec_()
                
        except KeyError as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Erro de Dados")
            msg.setText(f"Campo faltando nos dados da OS: {str(e)}")
            msg.setStyleSheet("""
                QMessageBox {
                    background-color: white;
                    color: black;}
                QMessageBox QLabel {
                    color: black;}
                QPushButton {
                    background-color: #f0f0f0;
                    color: black;
                    border: 1px solid #ccc;
                    padding: 5px 15px;
                    border-radius: 3px;}
                QPushButton:hover {
                    background-color: #e0e0e0;}""")
            msg.exec_()
            
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Erro")
            msg.setText(f"Erro ao exportar TXT: {str(e)}")
            msg.setStyleSheet("""
                QMessageBox {
                    background-color: white;
                    color: black;}
                QMessageBox QLabel {
                    color: black;}
                QPushButton {
                    background-color: #f0f0f0;
                    color: black;
                    border: 1px solid #ccc;
                    padding: 5px 15px;
                    border-radius: 3px;}
                QPushButton:hover {
                    background-color: #e0e0e0;}""")
            msg.exec_()

    def exportar_os_para_pdf(self, os_data):
        try:
            # Gera nome do arquivo
            nome_arquivo = f"OS_{os_data['id']}_{os_data['tipo_equipamento'].replace(' ', '_')}.pdf"
            
            # Solicita local para salvar
            destino, _ = QFileDialog.getSaveFileName(
                self, 
                "Exportar OS como PDF", 
                nome_arquivo, 
                "Arquivos PDF (*.pdf)")
            if not destino:
                return
            
            # Cria o PDF
            c = canvas.Canvas(destino, pagesize=letter)
            width, height = letter
            
            # Configurações de fonte
            c.setFont("Helvetica-Bold", 16)
            
            # Título
            c.drawString(100, height - 50, "ORDEM DE SERVIÇO")
            c.setFont("Helvetica", 10)
            c.drawString(100, height - 70, f"ID: {os_data['id']}")
            
            # Linha separadora
            c.line(100, height - 80, width - 100, height - 80)
            
            # Data
            y = height - 100
            c.setFont("Helvetica-Bold", 12)
            c.drawString(100, y, "INFORMAÇÕES DA OS:")
            y -= 20
            
            c.setFont("Helvetica", 10)
            info_items = [
                f"Data da OS: {os_data['data']}",
                f"Data de Exportação: {datetime.now().strftime('%d/%m/%Y %H:%M')}",
                "",
                "DADOS DO EQUIPAMENTO:",
                f"• Tipo: {os_data['tipo_equipamento']}",
                f"• N° Série: {os_data['numero_serie']}",
                f"• N° Placa: {os_data['numero_placa']}",
                f"• Valor do Reparo: {os_data['valor_do_reparo']}",
                f"• Revisão: {os_data['revisao']}",
                f"• Relatório: {os_data['relatorio'][:100]}...",
                "",
                "INFORMAÇÕES ADICIONAIS:",
                f"• Etiqueta: {os_data['etiqueta']}",
                f"• Configuração Backup: {os_data['backup']}",
                "",
                "STATUS: Ativa"]
            for item in info_items:
                if item.startswith("DADOS DO") or item.startswith("INFORMAÇÕES"):
                    c.setFont("Helvetica-Bold", 11)
                    c.drawString(100, y, item)
                    y -= 20
                elif item:
                    c.setFont("Helvetica", 10)
                    if len(item) > 60 and "•" in item:
                        parts = []
                        current = item
                        while len(current) > 60:
                            break_point = current[:60].rfind(' ')
                            if break_point == -1:
                                break_point = 60
                            parts.append(current[:break_point])
                            current = "    " + current[break_point:].strip()
                        parts.append(current)
                        
                        for part in parts:
                            c.drawString(120, y, part)
                            y -= 15
                    else:
                        c.drawString(120, y, item)
                        y -= 15
                else:
                    y -= 10
            
            if len(os_data['relatorio']) > 100:
                c.showPage()
                y = height - 50
                c.setFont("Helvetica-Bold", 14)
                c.drawString(100, y, "RELATÓRIO COMPLETO:")
                y -= 30
                c.setFont("Helvetica", 10)
                relatorio_lines = os_data['relatorio'].split('\n')
                for line in relatorio_lines:
                    if y < 50:
                        c.showPage()
                        y = height - 50
                    while len(line) > 80:
                        break_point = line[:80].rfind(' ')
                        if break_point == -1:
                            break_point = 80
                        c.drawString(100, y, line[:break_point])
                        line = line[break_point:].strip()
                        y -= 15
                    c.drawString(100, y, line)
                    y -= 15
            
            c.setFont("Helvetica-Oblique", 8)
            c.drawString(100, 50, f"Documento gerado por Sistema de OS em {datetime.now().strftime('%d/%m/%Y')}")
            c.save()
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Sucesso")
            msg.setText(f"OS #{os_data['id']} exportada como PDF!\n\n"
                       f"Arquivo: {os.path.basename(destino)}\n"
                       f"Local: {destino}")
            msg.setStyleSheet("""
                QMessageBox {
                    background-color: white;
                    color: black;}
                QMessageBox QLabel {
                    color: black;}
                QPushButton {
                    background-color: #f0f0f0;
                    color: black;
                    border: 1px solid #ccc;
                    padding: 5px 15px;
                    border-radius: 3px;}
                QPushButton:hover {
                    background-color: #e0e0e0;}""")
            msg.exec_()
            
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Erro")
            msg.setText(f"Erro ao exportar PDF: {str(e)}")
            msg.setStyleSheet("""
                QMessageBox {
                    background-color: white;
                    color: black;}
                QMessageBox QLabel {
                    color: black;}
                QPushButton {
                    background-color: #f0f0f0;
                    color: black;
                    border: 1px solid #ccc;
                    padding: 5px 15px;
                    border-radius: 3px;}
                QPushButton:hover {
                    background-color: #e0e0e0;}""")
            msg.exec_()
 
    def configurar_tree_widget_ordem_servicos(self):
        colunas = ["ID", "Tipo Equipamento", "N° Série", "N° Placa", "Etiqueta de Serviço", "Backup", "Revisão", "Data", "Valor do Reparo", "Relatório"]
        self.ui.TBW_ORDENS_DE_SERVICOS.setColumnCount(len(colunas))
        self.ui.TBW_ORDENS_DE_SERVICOS.setHeaderLabels(colunas)
        larguras = [50, 120, 100, 100, 120, 100, 80, 80, 100, 200]
        for i in range(min(len(colunas), len(larguras))):
            self.ui.TBW_ORDENS_DE_SERVICOS.setColumnWidth(i, larguras[i])
        self.ui.TBW_ORDENS_DE_SERVICOS.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.ui.TBW_ORDENS_DE_SERVICOS.itemChanged.connect(self.atualizar_valor_na_tabela)

    def atualizar_valor_na_tabela(self, item, column):
        if column == 8:
            try:
                texto = item.text(column)
                valor_texto = texto.replace("R$", "").replace(",", ".").strip()
                valor_float = float(valor_texto) if valor_texto.replace('.', '', 1).isdigit() else 0.0
                item.setText(column, f"R$ {valor_float:.2f}")
                # ATUALIZA OS DADOS DO  ITEM
                item.setData(column, QtCore.Qt.UserRole, valor_float)
                # ATUALIZA A SPINBOX
                self.ui.DBS_VALOR_DO_REPARO_OREDEM_DE_SERVICOS.setValue(valor_float)
                print(f"Valor atualizado na tabela: R$ {valor_float:.2f}")
            except Exception as e:
                print(f"Erro ao atualizar valor na tabela: {e}")
                item.setText(column, "R$ 0.00")
    
    def gerar_relatorio_equipamento(self):
        try:
            tipo_equipamento = self.ui.TXT_TIPO_DE_EQUIPAMENTO_ORDEM_DE_SERVICOS.text()
            numero_serie = self.ui.TXT_NUMERO_DE_SERIE_EQUIPAMENTO_ORDEM_DE_SERVICOS.text()
            revisao_placa = self.ui.TXT_REVISAO_DA_PLACA_ORDEM_DE_SERVICOS.text()
            valor_do_reparo = self.ui.DBS_VALOR_DO_REPARO_OREDEM_DE_SERVICOS.value()
            valor_formatado = f"R$ {valor_do_reparo:.2f}"
            obs_finais = ""
            if hasattr(self.ui, 'TXT_OBSERVACOES_RELATORIO'):
                obs_finais = self.ui.TXT_OBSERVACOES_RELATORIO.toPlainText()
            relatorio = f"""
            ===== RELATÓRIO DE EQUIPAMENTO =====
            Data: {datetime.now().strftime('%d/%m/%Y %H:%M')}
            Tipo: {tipo_equipamento}
            N° Série: {numero_serie}
            Valor do Reparo: {valor_formatado}
            Revisão Placa: {revisao_placa}

            CONFIGURAÇÃO BACKUP:
            - Com Backup: {'Sim' if self.ui.RDB_COM_BACKUP_ORDEM_DE_SERVICOS.isChecked() else 'Não'}
            - Sem Backup: {'Sim' if self.ui.RDB_SEM_BACKUP_ORDEM_DE_SERVICOS.isChecked() else 'Não'}
            
            OBSERVAÇÕES/RELATÓRIO:
            {obs_finais if obs_finais.strip() else 'Nenhuma observação registrada.'}
            
            =====================================
            """

            os.makedirs("arquivo", exist_ok=True)
            with open('arquivo/ordens_de_servicos.txt', 'w', encoding='utf-8') as f:
                f.write(relatorio)
            
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Sucesso")
            msg.setText("Relatório do equipamento gerado com sucesso!")
            msg.setStyleSheet("""
                QMessageBox {
                    background-color: white; color: black;}
                QMessageBox QLabel {
                    color: black;}
                QPushButton {
                    background-color: #f0f0f0; color: black;
                    border: 1px solid #ccc; padding: 5px 15px;
                    border-radius: 3px;}
                QPushButton:hover {
                    background-color: #e0e0e0;}""")
            msg.exec_()
            
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Erro")
            msg.setText(f"Erro ao gerar relatório: {str(e)}")
            msg.setStyleSheet("""
                QMessageBox {
                    background-color: white; color: black;}
                QMessageBox QLabel {
                    color: black;}
                QPushButton {
                    background-color: #f0f0f0; color: black;
                    border: 1px solid #ccc; padding: 5px 15px;
                    border-radius: 3px;}
                QPushButton:hover {
                    background-color: #e0e0e0;}""")
            msg.exec_()
    
    def salvar_relatorio_completo_os(self):
        try:
            tipo_equipamento = self.ui.TXT_TIPO_DE_EQUIPAMENTO_ORDEM_DE_SERVICOS.text().strip()
            numero_serie = self.ui.TXT_NUMERO_DE_SERIE_EQUIPAMENTO_ORDEM_DE_SERVICOS.text().strip()
            revisao_placa = self.ui.TXT_REVISAO_DA_PLACA_ORDEM_DE_SERVICOS.text().strip()
            valor_do_reparo = self.ui.DBS_VALOR_DO_REPARO_OREDEM_DE_SERVICOS.value()
            obs_finais = ""
            if hasattr(self.ui, 'TXT_OBSERVACOES_RELATORIO'):
                obs_finais = self.ui.TXT_OBSERVACOES_RELATORIO.toPlainText().strip()
            com_backup = "Sim" if self.ui.RDB_COM_BACKUP_ORDEM_DE_SERVICOS.isChecked() else "Não"
            sem_backup = "Sim" if self.ui.RDB_SEM_BACKUP_ORDEM_DE_SERVICOS.isChecked() else "Não"
            if not all([tipo_equipamento, numero_serie]):
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setWindowTitle("Campos Obrigatórios")
                msg.setText("Preencha Tipo e Número de Série do equipamento!")
                msg.setStyleSheet("""
                    QMessageBox {
                        background-color: white;
                        color: black;}
                    QMessageBox QLabel {
                        color: black;}
                    QPushButton {
                        background-color: #f0f0f0;
                        color: black;
                        border: 1px solid #ccc;
                        padding: 5px 15px;
                        border-radius: 3px;}
                    QPushButton:hover {
                        background-color: #e0e0e0;}""")
                msg.exec_()
                return
            
            if self.db.inserir_ordem_servico(tipo_equipamento, numero_serie, revisao_placa, obs_finais, valor_do_reparo, com_backup, sem_backup):
                self.gerar_relatorio_equipamento()
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle("Sucesso")
                msg.setText(f"Ordem de serviço salva!\nValor do reparo: R$ {valor_do_reparo:.2f}")
                msg.setStyleSheet("""
                    QMessageBox {
                        background-color: white;
                        color: black;}
                    QMessageBox QLabel {
                        color: black;}
                    QPushButton {
                        background-color: #f0f0f0;
                        color: black;
                        border: 1px solid #ccc;
                        padding: 5px 15px;
                        border-radius: 3px;}
                    QPushButton:hover {
                        background-color: #e0e0e0;}""")
                msg.exec_()
                
                self.limpar_campos_os()
                self.carregar_ordem_servicos()
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setWindowTitle("Erro")
                msg.setText("Erro ao salvar ordem de serviço no banco!")
                msg.setStyleSheet("""
                    QMessageBox {
                        background-color: white;
                        color: black;}
                    QMessageBox QLabel {
                        color: black;}
                    QPushButton {
                        background-color: #f0f0f0;
                        color: black;
                        border: 1px solid #ccc;
                        padding: 5px 15px;
                        border-radius: 3px;}
                    QPushButton:hover {
                        background-color: #e0e0e0;}""")
                msg.exec_()
                
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Erro")
            msg.setText(f"Erro ao salvar ordem de serviço: {str(e)}")
            msg.setStyleSheet("""
                QMessageBox {
                    background-color: white;
                    color: black;}
                QMessageBox QLabel {
                    color: black;}
                QPushButton {
                    background-color: #f0f0f0;
                    color: black;
                    border: 1px solid #ccc;
                    padding: 5px 15px;
                    border-radius: 3px;}
                QPushButton:hover {
                    background-color: #e0e0e0;}""")
            msg.exec_()
  
    def carregar_ordem_servicos(self, filtro=""):
        try:
            self.ui.TBW_ORDENS_DE_SERVICOS.clear()
            ordens = self.db.buscar_ordem_servicos(filtro)    
            for ordem in ordens:
                valor_banco = 0.0
                if len(ordem) > 9:
                    try:
                        valor_banco = float(ordem[9]) if ordem[9] not in [None, ""] else 0.0
                    except (ValueError, TypeError):
                        valor_banco = 0.0
                valor_formatado = f"R$ {valor_banco:.2f}"
                item = QTreeWidgetItem([
                    str(ordem[0]),  # ID
                    ordem[1] if len(ordem) > 1 else "N/D",
                    ordem[2] if len(ordem) > 2 else "N/D",
                    ordem[3] if len(ordem) > 3 else "N/D",
                    ordem[4] if len(ordem) > 4 else "N/D",
                    ordem[5] if len(ordem) > 5 else "N/D",
                    ordem[6] if len(ordem) > 6 else "N/D",
                    ordem[8] if len(ordem) > 8 else "N/D",
                    valor_formatado,
                    ordem[10] if len(ordem) > 10 else "N/D",])
                item.setData(8, QtCore.Qt.UserRole, valor_banco)
                for i in range(item.columnCount()):
                    item.setForeground(i, QtGui.QBrush(QtGui.QColor("black")))
                
                self.ui.TBW_ORDENS_DE_SERVICOS.addTopLevelItem(item)      
                self.ui.TBW_ORDENS_DE_SERVICOS.header().setStretchLastSection(True)
            
        except Exception as e:
            print(f"Erro ao carregar ordens de serviço: {e}")
            import traceback
            traceback.print_exc()
    
    def excluir_ordem_servico(self):
        current_item = self.ui.TBW_ORDENS_DE_SERVICOS.currentItem()
        if not current_item:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("AVISO")
            msg.setText("Nenhuma ordem de serviço selecionada!")
            msg.setStyleSheet("""
                QMessageBox {
                    background-color: white;
                    color: black;}
                QMessageBox QLabel {
                    color: black;}
                QPushButton {
                    background-color: #f0f0f0;
                    color: black;
                    border: 1px solid #ccc;
                    padding: 5px 15px;
                    border-radius: 3px;}
                QPushButton:hover {
                    background-color: #e0e0e0;}""")
            msg.exec_()
            return
        id_ordem = current_item.text(0)
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Question)
        msg.setWindowTitle("Confirmação")
        msg.setText(f"Excluir ordem de serviço '{current_item.text(1)} - {current_item.text(2)}'?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg.setStyleSheet("""
            QMessageBox {
                background-color: white;
                color: black;}
            QMessageBox QLabel {
                color: black;}
            QPushButton {
                background-color: #f0f0f0;
                color: black;
                border: 1px solid #ccc;
                padding: 5px 15px;
                border-radius: 3px;}
            QPushButton:hover {
                background-color: #e0e0e0;}""")
        reply = msg.exec_()
        if reply == QMessageBox.Yes:
            if self.db.excluir_ordem_servico(id_ordem):
                self.carregar_ordem_servicos()
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle("SUCESSO")
                msg.setText("Ordem de serviço excluída!")
                msg.setStyleSheet("""
                    QMessageBox {
                        background-color: white;
                        color: black;}
                    QMessageBox QLabel {
                        color: black;}
                    QPushButton {
                        background-color: #f0f0f0;
                        color: black;
                        border: 1px solid #ccc;
                        padding: 5px 15px;
                        border-radius: 3px;}
                    QPushButton:hover {
                        background-color: #e0e0e0;}""")
                msg.exec_()
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setWindowTitle("Erro")
                msg.setText("Erro ao excluir ordem de serviço!")
                msg.setStyleSheet("""
                    QMessageBox {
                        background-color: white;
                        color: black;}
                    QMessageBox QLabel {
                        color: black;}
                    QPushButton {
                        background-color: #f0f0f0;
                        color: black;
                        border: 1px solid #ccc;
                        padding: 5px 15px;
                        border-radius: 3px;}
                    QPushButton:hover {
                        background-color: #e0e0e0;}""")
                msg.exec_()
    
    def mostrar_conteudo_os(self):
        try:
            arquivo_path = "arquivo/ordens_de_servicos.txt"
            if not os.path.exists(arquivo_path):
                valor_reparo = self.ui.DBS_VALOR_DO_REPARO_OREDEM_DE_SERVICOS.value()
                valor_formatado = f"R$ {valor_reparo:.2f}"
                exemplo_conteudo = f"""
                ===== ORDENS DE SERVIÇO =====
                
                Nenhuma ordem de serviço cadastrada ainda.
                
                Use o botão "Gerar Ordem de Serviço" para criar 
                relatórios de equipamentos.
                
                VALOR DO REPARO: {valor_formatado}
                
                =============================
                """
                os.makedirs("arquivo", exist_ok=True)    
                with open(arquivo_path, 'w', encoding='utf-8') as arquivo:
                    arquivo.write(exemplo_conteudo) 
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle("Info")
                msg.setText("Arquivo criado com conteúdo de exemplo!")
                msg.setStyleSheet("""
                    QMessageBox {
                        background-color: white;
                        color: black;}
                    QMessageBox QLabel {
                        color: black;}
                    QPushButton {
                        background-color: #f0f0f0;
                        color: black;
                        border: 1px solid #ccc;
                        padding: 5px 15px;
                        border-radius: 3px;}
                    QPushButton:hover {
                        background-color: #e0e0e0;}""")
                msg.exec_()
            with open(arquivo_path, 'r', encoding='utf-8') as arquivo:
                conteudo = arquivo.read()
            valor_reparo = self.ui.DBS_VALOR_DO_REPARO_OREDEM_DE_SERVICOS.value()
            valor_formatado = f"VALOR DO REPARO: R$ {valor_reparo:.2f}"
            if "VALOR DO REPARO:" not in conteudo:
                conteudo += f"\n\n{valor_formatado}\n"
            else:
                import re
                padrao = r"VALOR DO REPARO:.*"
                conteudo = re.sub(padrao, valor_formatado, conteudo)
            
            dialog = QtWidgets.QDialog(self)
            dialog.setWindowTitle("Conteúdo - Ordens de Serviço")
            dialog.resize(700, 500)
            dialog.setStyleSheet("""
                background-color: white;
                color: black;""")
            layout = QVBoxLayout(dialog)
            
            titulo_label = QtWidgets.QLabel("📋 RELATÓRIO DE ORDENS DE SERVIÇO")
            titulo_label.setStyleSheet("""
                font-size: 16px; 
                font-weight: bold; 
                background-color: white; 
                color: black; 
                margin: 10px;
                border: 1px solid #dee2e6;
                padding: 10px;
                border-radius: 5px;""")
            titulo_label.setAlignment(Qt.AlignCenter)
            layout.addWidget(titulo_label)
            
            # Adicionar informações adicionais sobre o valor
            info_label = QtWidgets.QLabel(f"💰 Valor atual do reparo: R$ {valor_reparo:.2f}")
            info_label.setStyleSheet("""
                font-size: 12px;
                font-weight: bold;
                color: #28a745;
                margin: 5px;
                padding: 5px;
                border: 1px solid #c3e6cb;
                background-color: #d4edda;
                border-radius: 3px;
            """)
            info_label.setAlignment(Qt.AlignCenter)
            layout.addWidget(info_label)
            
            text_edit = QTextEdit()
            text_edit.setPlainText(conteudo)
            text_edit.setReadOnly(True)
            text_edit.setStyleSheet("""
                QTextEdit {
                    font-family: 'Courier New';
                    font-size: 12px;
                    color: black;
                    background-color: white;
                    border: 1px solid #dee2e6;
                    border-radius: 5px;
                    padding: 10px;}""")
            btn_layout = QtWidgets.QHBoxLayout()
            btn_atualizar_valor = QPushButton("Atualizar Valor do Reparo")
            btn_atualizar_valor.clicked.connect(lambda: self.atualizar_valor_reparo_arquivo(arquivo_path, text_edit))
            btn_atualizar_valor.setStyleSheet("""
                QPushButton {
                    background-color: #17a2b8;
                    color: white;
                    border: 1px solid #117a8b;
                    padding: 8px 16px;
                    border-radius: 4px;
                    font-weight: bold;}
                QPushButton:hover {
                    background-color: #138496;}""")
            btn_exportar = QPushButton("Exportar")
            btn_exportar.clicked.connect(lambda: self.exportar_arquivo(arquivo_path))
            btn_exportar.setStyleSheet("""
                QPushButton {
                    background-color: #f0f0f0;
                    color: black;
                    border: 1px solid #ced4da;
                    padding: 8px 16px;
                    border-radius: 4px;
                    font-weight: bold;}
                QPushButton:hover {
                    background-color: #e2e6ea;}""")
            btn_limpar = QPushButton("Limpar Arquivo")
            btn_limpar.clicked.connect(lambda: self.limpar_arquivo_os(arquivo_path, dialog))
            btn_limpar.setStyleSheet("""
                QPushButton {
                    background-color: #f0f0f0;
                    color: black;
                    border: 1px solid #ced4da;
                    padding: 8px 16px;
                    border-radius: 4px;
                    font-weight: bold;}
                QPushButton:hover {
                    background-color: #e2e6ea;}""")
            
            btn_fechar = QPushButton("Fechar")
            btn_fechar.clicked.connect(dialog.close)
            btn_fechar.setStyleSheet("""
                QPushButton {
                    background-color: #f0f0f0;
                    color: black;
                    border: 1px solid #ced4da;
                    padding: 8px 16px;
                    border-radius: 4px;
                    font-weight: bold;}
                QPushButton:hover {
                    background-color: #e2e6ea;}""")
            btn_layout.addWidget(btn_atualizar_valor)
            btn_layout.addWidget(btn_exportar)
            btn_layout.addWidget(btn_limpar)
            btn_layout.addWidget(btn_fechar)
            layout.addWidget(text_edit)
            layout.addLayout(btn_layout)
            with open(arquivo_path, 'w', encoding='utf-8') as arquivo:
                arquivo.write(conteudo)
                
            dialog.exec_()
            
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Erro")
            msg.setText(f"Erro ao ler arquivo de ordens de serviço: {str(e)}")
            msg.setStyleSheet("""
                QMessageBox {
                    background-color: white;
                    color: black;}
                QMessageBox QLabel {
                    color: black;}
                QPushButton {
                    background-color: #f0f0f0;
                    color: black;
                    border: 1px solid #ccc;
                    padding: 5px 15px;
                    border-radius: 3px;}
                QPushButton:hover {
                    background-color: #e0e0e0;}""")
            msg.exec_()
    
    def atualizar_valor_reparo_arquivo(self, arquivo_path, text_edit):
        try:
            valor_reparo = self.ui.DBS_VALOR_DO_REPARO_OREDEM_DE_SERVICOS.value()
            valor_formatado = f"VALOR DO REPARO: R$ {valor_reparo:.2f}"
            with open(arquivo_path, 'r', encoding='utf-8') as arquivo:
                conteudo = arquivo.read()
            if "VALOR DO REPARO:" in conteudo:
                import re
                padrao = r"VALOR DO REPARO:.*"
                conteudo = re.sub(padrao, valor_formatado, conteudo)
            else:
                conteudo += f"\n\n{valor_formatado}\n"          
            with open(arquivo_path, 'w', encoding='utf-8') as arquivo:
                arquivo.write(conteudo)
            text_edit.setPlainText(conteudo)
            self.carregar_ordem_servicos()
            QMessageBox.information(self, "Sucesso", 
                               f"Valor do reparo atualizado para: R$ {valor_reparo:.2f}")
        except Exception as e:
            QMessageBox.critical(self, "Erro", 
                            f"Erro ao atualizar valor: {str(e)}")

    def exportar_arquivo(self, arquivo_path):
        try:
            destino, _ = QFileDialog.getSaveFileName(
                self, "Exportar Arquivo", "ordens_de_servico_backup.txt", "Arquivos de Texto (*.txt)")
            if destino:
                shutil.copy2(arquivo_path, destino)
                
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle("Sucesso")
                msg.setText(f"Arquivo exportado para:\n{destino}")
                msg.setStyleSheet("""
                    QMessageBox {
                        background-color: white;
                        color: black;}
                    QMessageBox QLabel {
                        color: black;}
                    QPushButton {
                        background-color: #f0f0f0;
                        color: black;
                        border: 1px solid #ccc;
                        padding: 5px 15px;
                        border-radius: 3px;}
                    QPushButton:hover {
                        background-color: #e0e0e0;}""")
                msg.exec_()
                
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Erro")
            msg.setText(f"Erro ao exportar arquivo: {str(e)}")
            msg.setStyleSheet("""
                QMessageBox {
                    background-color: white;
                    color: black;}
                QMessageBox QLabel {
                    color: black;}
                QPushButton {
                    background-color: #f0f0f0;
                    color: black;
                    border: 1px solid #ccc;
                    padding: 5px 15px;
                    border-radius: 3px;}
                QPushButton:hover {
                    background-color: #e0e0e0;}""")
            msg.exec_()

    def preencher_tabela_ordem_servico(self):
        try:
            if not hasattr(self.ui, 'TBW_ORDENS_DE_SERVICOS'):
                print("Widget TBW_ORDENS_DE_SERVICOS não encontrado")
                return
            self.ui.TBW_ORDENS_DE_SERVICOS.clear()
            equipamentos = self.db.buscar_todos_ordem_servicos()
            colunas = ["ID", "Tipo de Equipamento", "Número de Série", "Revisão da Placa", "Com Backup", "Sem Backup", "Valor do Reparo", "Status"]
            self.ui.TBW_ORDENS_DE_SERVICOS.setColumnCount(len(colunas))
            self.ui.TBW_ORDENS_DE_SERVICOS.setHeaderLabels(colunas)
            if equipamentos:
                for servico in equipamentos:
                    valor_reparo = servico[6] if len(servico) > 6 else 0.0
                    valor_formatado = f"R$ {float(valor_reparo):.2f}"
                    
                    item = QTreeWidgetItem([
                        str(servico[0]),
                        servico[1] if len(servico) > 1 else "",
                        servico[2] if len(servico) > 2 else "",
                        servico[3] if len(servico) > 3 else "",
                        servico[4] if len(servico) > 4 else "",
                        servico[5] if len(servico) > 5 else "",
                        valor_formatado,"Ativo"])
                    self.ui.TBW_ORDENS_DE_SERVICOS.addTopLevelItem(item)
        except Exception as e:
            print(f"Erro ao preencher tabela ordens de servicos: {e}")

    def pesquisar_ordem_servico(self):
        try:
            filtro = ""
            if hasattr(self.ui, 'TXT_FILTRO_ORDEM_DE_SERVICOS'):
                filtro = self.ui.TXT_FILTRO_ORDEM_DE_SERVICOS.text().strip()
                self.carregar_ordem_servicos(filtro)
                    
        except Exception as e:
            print(f"Erro na pesquisa de ordens: {e}")
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Erro")
            msg.setText(f"Erro ao pesquisar: {str(e)}")
            msg.setStyleSheet("""
                QMessageBox {
                    background-color: white;
                    color: black;}
                QMessageBox QLabel {
                    color: black;}
                QPushButton {
                    background-color: #f0f0f0;
                    color: black;
                    border: 1px solid #ccc;
                    padding: 5px 15px;
                    border-radius: 3px;}
                QPushButton:hover {
                    background-color: #e0e0e0;}""")
            msg.exec_()
   
    def limpar_arquivo_os(self, arquivo_path, dialog):
        try:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Question)
            msg.setWindowTitle("Confirmar Limpeza")
            msg.setText("Tem certeza que deseja limpar todo o conteúdo do arquivo de ordens de serviço?")
            msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            msg.setStyleSheet("""
                QMessageBox {
                    background-color: white;
                    color: black;
                }
                QMessageBox QLabel {
                    color: black;
                }
                QPushButton {
                    background-color: #f0f0f0;
                    color: black;
                    border: 1px solid #ccc;
                    padding: 5px 15px;
                    border-radius: 3px;
                }
                QPushButton:hover {
                    background-color: #e0e0e0;
                }
            """)
            
            resposta = msg.exec_()
            
            if resposta == QMessageBox.Yes:
                with open(arquivo_path, 'w', encoding='utf-8') as arquivo:
                    arquivo.write("===== ORDENS DE SERVIÇO =====\n")
                    arquivo.write(f"Arquivo limpo em: {datetime.now().strftime('%d/%m/%Y %H:%M')}\n")
                    arquivo.write("Nenhuma ordem de serviço cadastrada.\n")
                    arquivo.write("==============================\n")
                
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle("Sucesso")
                msg.setText("Arquivo limpo com sucesso!")
                msg.setStyleSheet("""
                    QMessageBox {
                        background-color: white;
                        color: black;
                    }
                    QMessageBox QLabel {
                        color: black;
                    }
                    QPushButton {
                        background-color: #f0f0f0;
                        color: black;
                        border: 1px solid #ccc;
                        padding: 5px 15px;
                        border-radius: 3px;
                    }
                    QPushButton:hover {
                        background-color: #e0e0e0;
                    }
                """)
                msg.exec_()
                
                dialog.close()
                self.mostrar_conteudo_os()
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Erro")
            msg.setText(f"Erro ao limpar arquivo: {str(e)}")
            msg.setStyleSheet("""
                QMessageBox {
                    background-color: white;
                    color: black;
                }
                QMessageBox QLabel {
                    color: black;
                }
                QPushButton {
                    background-color: #f0f0f0;
                    color: black;
                    border: 1px solid #ccc;
                    padding: 5px 15px;
                    border-radius: 3px;
                }
                QPushButton:hover {
                    background-color: #e0e0e0;
                }
            """)
            msg.exec_()

    def limpar_campos_os(self):
        try:
            campos = [
                self.ui.TXT_TIPO_DE_EQUIPAMENTO_ORDEM_DE_SERVICOS,
                self.ui.TXT_NUMERO_DE_SERIE_EQUIPAMENTO_ORDEM_DE_SERVICOS,
                self.ui.TXT_REVISAO_DA_PLACA_ORDEM_DE_SERVICOS]
            if hasattr(self.ui, 'TXT_FILTRO_ORDEM_DE_SERVICOS'):
                campos.append(self.ui.TXT_FILTRO_ORDEM_DE_SERVICOS)
            for campo in campos:
                if campo:
                    campo.clear()
            if hasattr(self.ui, 'TXT_OBSERVACOES_RELATORIO'):
                self.ui.TXT_OBSERVACOES_RELATORIO.clear()
            self.ui.RDB_COM_BACKUP_ORDEM_DE_SERVICOS.setAutoExclusive(False)
            self.ui.RDB_COM_BACKUP_ORDEM_DE_SERVICOS.setChecked(False)
            self.ui.RDB_SEM_BACKUP_ORDEM_DE_SERVICOS.setChecked(False)
            self.ui.RDB_COM_BACKUP_ORDEM_DE_SERVICOS.setAutoExclusive(True)
            self.ui.DBS_VALOR_DO_REPARO_OREDEM_DE_SERVICOS.setValue(0.0)
            self.os_selecionada = None
            for i in range(self.ui.TBW_ORDENS_DE_SERVICOS.topLevelItemCount()):
                item = self.ui.TBW_ORDENS_DE_SERVICOS.topLevelItem(i)
                for j in range(item.columnCount()):
                    item.setBackground(j, QtGui.QBrush(Qt.white))
                    item.setForeground(j, QtGui.QBrush(Qt.black))
                
        except Exception as e:
            print(f"Erro ao limpar campos: {e}")

    def buscar_ordem_servicos(self):
        self.pesquisar_ordem_servico()

    def filtrar_ordem_servicos(self):
        try:
            self.buscar_ordem_servicos()
        except Exception as e:
            print(f"Erro no filtro: {e}")

    def fechar_tela(self):
        try:
            if hasattr(self, 'db') and self.db:
                self.db.close()
            self.close()
        except Exception as e:
            print(f"Erro ao fechar tela: {e}")
            self.close()

    def closeEvent(self, event):
        try:
            if hasattr(self, 'db') and self.db:
                self.db.close()
        except:
            pass
        event.accept()

class ConsultarCliente(TelaArrastavelBase):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_telaConsultacliente()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowIcon(QtGui.QIcon("Accets/icons/icons/logoSpike.png"))
        self.setGeometry(300, 150, 800, 600)
        self.db_clientes = sqlite_db("db/sistema.db")
        # CONFIGURAÇÕES ADICIONAIS
        self.configurar_tela()

    def configurar_tela(self):
        try:
            self.conectar_botoes_consulta()
            self.carregar_dados_clientes()
        except Exception as e:
            print(f"Erro ao configurar tela: {e}")

    def conectar_botoes_consulta(self):
        try:
            if hasattr(self.ui, 'BTN_RETORNAR_TELA_PRINCIPAL'):
                self.ui.BTN_RETORNAR_TELA_PRINCIPAL.clicked.connect(self.fechar_tela)            
            if hasattr(self.ui, 'BTN_CONSULTAR_CLIENTE'):
                self.ui.BTN_CONSULTAR_CLIENTE.clicked.connect(self.pesquisar_clientes)
            if hasattr(self.ui, 'TXT_FILTRO_CONSULTA'):
                self.ui.TXT_FILTRO_CONSULTA.textChanged.connect(self.filtrar_clientes)
        except Exception as e:
            print(f"Erro ao conectar botões: {e}")

    def carregar_dados_clientes(self):
        try:
            self.pesquisar_clientes()
        except Exception as e:
            print(f"Erro ao carregar dados: {e}")

    def preencher_tabela(self, clientes):
        try:
            # Verificar se o widget existe
            if not hasattr(self.ui, 'TBW_CONSULTA_CLIENTES'):
                print("Widget TBW_CONSULTA_CLIENTES não encontrado")
                return
            self.ui.TBW_CONSULTA_CLIENTES.clear()
            colunas = ["ID", "Nome", "Endereço", "Documento", "Complemento", "Status"]
            self.ui.TBW_CONSULTA_CLIENTES.setColumnCount(len(colunas))
            self.ui.TBW_CONSULTA_CLIENTES.setHeaderLabels(colunas)
            for cliente in clientes:
                item = QTreeWidgetItem([
                    str(cliente[0]),  # ID
                    cliente[1],       # Nome
                    cliente[2],       # Endereço
                    cliente[3],       # Documento
                    cliente[4],       # Complemento
                    "Ativo" if cliente[5] else "Inativo"  # Status
                ])
                self.ui.TBW_CONSULTA_CLIENTES.addTopLevelItem(item)
        except Exception as e:
            print(f"Erro ao preencher tabela: {e}")

    def pesquisar_clientes(self):
        try:
            filtro = ""
            if hasattr(self.ui, 'TXT_FILTRO_CONSULTA'):
                filtro = self.ui.TXT_FILTRO_CONSULTA.text().strip()
            clientes = self.db_clientes.buscar_clientes(filtro)
            self.preencher_tabela(clientes)
        except Exception as e:
            print(f"Erro na pesquisa: {e}")

    def filtrar_clientes(self):
        try:
            self.pesquisar_clientes()
        except Exception as e:
            print(f"Erro no filtro: {e}")

    def fechar_tela(self):
        self.db_clientes.fechar_conexao()
        self.close()

class NotaFiscal(TelaArrastavelBase):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_telaNotafiscal()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowIcon(QtGui.QIcon("Accets/icons/icons/logoSpike.png"))
        self.setGeometry(300, 150, 800, 600)
        self.ui.setUi(self)

class ClienteApp(TelaArrastavelBase):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_telaPrincipal()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowIcon(QtGui.QIcon("Accets/icons/icons/logoSpike.png"))
        self.ui.setupUi(self)
        # INICIALIZAR BANCO DE DADOS
        self.db = sqlite_db("db/sistema.db")
        os.makedirs("arquivo", exist_ok=True)
        # CONECTAR TODOS OS BOTÕES
        self.conectar_botoes()
        self.mousePressEvent
        self.mouseMoveEvent
        # CONFIGURAR SHORTCUTS
        self.configurar_shortcuts_principal()
        self.drag_position = QtCore.QPoint()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.showFullScreen()

    # FUNÇÕES DAS CONEXÕES DOS BOTÕES
    def conectar_botoes(self):
        # BOTÕES PRINCIPAIS
        self.ui.BTN_ORNDENS_DE_SERVICOS.clicked.connect(self.abrir_tela_consultar_geral_ordens_servicos)
        self.ui.BTN_NOVO_USUARIO.clicked.connect(self.abrir_tela_login)
        self.ui.BTN_FORNECEDORES.clicked.connect(self.abrir_tela_pedido)
        self.ui.BTN_BANCO_DE_DADOS.clicked.connect(self.abrir_tela_banco_dados)
        self.ui.BTN_CLIENTES_DEVEDORES.clicked.connect(self.abrir_tela_ficha_cliente)
        self.ui.BTN_GERAR_NOTA_FISCAL.clicked.connect(self.abrir_telanota)
        self.ui.BTN_PEDIDOS.clicked.connect(self.abrir_tela_estoque)
        self.ui.BTN_MANUAL_DO_APP.clicked.connect(self.mostrar_atalhos_disponiveis)
        # CONECTAR ACTIONS DO MENU
        self.ui.actionFLUXO_DE_CAIXA.triggered.connect(self.abrir_tela_consultar_cliente)
        self.ui.actionFECHAMENTO_DE_CAIXA.triggered.connect(self.abrir_tela_grafico)
        self.ui.actionREGISTRO_DE_FUNCIONARIOS.triggered.connect(self.consulta_geral_funcs)
        self.ui.actionPEDIDOS.triggered.connect(self.abrir_tela_pedido)
        self.ui.actionPEDIDOS_CLIENTES.triggered.connect(self.abrir_tela_Lancamentos)
        self.ui.actionrREGISTRO.triggered.connect(self.abrir_tela_registro)
        self.ui.actionLOGIN.triggered.connect(self.abrir_tela_login)

    def configurar_shortcuts_principal(self):
        try:
            # F3 - Abrir tela de equipamentos (ordens de serviço)
            self.shortcut_equipamentos = QShortcut(QKeySequence(Qt.Key_F3), self)
            self.shortcut_equipamentos.activated.connect(self.abrir_tela_consultar_geral_ordens_servicos)
            # F4 - Abrir tela de consulta de clientes
            self.shortcut_clientes = QShortcut(QKeySequence(Qt.Key_F4), self)
            self.shortcut_clientes.activated.connect(self.abrir_tela_consultar_cliente)
            # F5 - Abrir tela de gráficos
            self.shortcut_graficos = QShortcut(QKeySequence(Qt.Key_F5), self)
            self.shortcut_graficos.activated.connect(self.abrir_tela_grafico)
            # ESC - Fechar aplicação
            self.shortcut_esc = QShortcut(QKeySequence(Qt.Key_Escape), self)
            self.shortcut_esc.activated.connect(self.fechar_aplicacao)
            # F2 - Consulta geral de funcionários
            self.shortcut_consulta_funcs = QShortcut(QKeySequence(Qt.Key_F2), self)
            self.shortcut_consulta_funcs.activated.connect(self.consulta_geral_funcs)
            # F1 - Mostrar ajuda com atalhos
            self.shortcut_ajuda = QShortcut(QKeySequence(Qt.Key_F1), self)
            self.shortcut_ajuda.activated.connect(self.mostrar_atalhos_disponiveis)
            print("✅ Shortcuts da tela principal configurados com sucesso!")
        except Exception as e:
            print(f"❌ Erro ao configurar shortcuts: {e}")
    
    def fechar_aplicacao(self):
        reply = QMessageBox.question(self, "Confirmação", 
                                   "Deseja realmente sair do sistema?",
                                   QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.fechar_conexoes()
            QCoreApplication.quit()
    
    def mostrar_atalhos_disponiveis(self):
        atalhos = """
    📋 ATALHOS DE TECLADO DISPONÍVEIS:
    F1 - Mostrar esta ajuda
    F2 - Consulta geral de funcionários
    F3 - Tela de equipamentos (Ordens de Serviço)
    F4 - Tela de consulta de clientes  
    F5 - Tela de gráficos
    ESC - Sair do sistema
    
    💡 Dica: Para arrastar as telas, clique e arraste em qualquer área vazia!
    os bancos de dados irão conectar automaticamete após o inicio da aplicação...
    Use estes atalhos para navegar mais rapidamente!
    """
        QMessageBox.information(self, "Atalhos do Sistema", atalhos)
    
    def consulta_geral_funcs(self):
        try:
            self.tela_funcionarios = TelaFuncionarios(self)
            self.tela_funcionarios.show()
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao abrir tela de funcionários: {str(e)}")
  
    # CONFIGURAÇÃO DAS TELAS SECUNDÁRIAS
    def abrir_tela_pedido(self):
        try:
            self.tela_pedido = TelaPedido(self)
            self.tela_pedido.destroyed.connect(self.on_tela_pedido_fechada)
            self.tela_pedido.show()
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao abrir tela de pedido: {str(e)}")
            print(f"Erro detalhado: {traceback.format_exc()}")        
    
    def abrir_tela_ficha_cliente(self):
        try:
            self.tela_ficha_cliente = TelaFichaCliente(self)
            self.tela_ficha_cliente.destroyed.connect(self.on_tela_ficha_cliente_fechada)
            self.tela_ficha_cliente.show()
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao abrir tela ficha cliente: {str(e)}")
            print(f"Erro detalhado: {traceback.format_exc()}") 
    
    def abrir_tela_consultar_cliente(self):
        try:
            self.tela_consultar_cliente = TelaPedido(self)
            self.tela_consultar_cliente.destroyed.connect(self.on_tela_consultar_cliente_fechada)
            self.tela_consultar_cliente.show()
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao abrir tela consultar cliente: {str(e)}")
            print(f"Erro detalhado: {traceback.format_exc()}")   

    def abrir_tela_registro(self):
        try:
            self.tela_registro = TelaRegistro(self)
            self.tela_registro.destroyed.connect(self.on_tela_registro_fechada)
            self.tela_registro.show()
            
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao abrir tela de registro: {str(e)}")
            print(f"Erro detalhado: {traceback.format_exc()}")
 
    def abrir_tela_registro_funcs(self):
        try:
            self.tela_registro_funcs = TelaFuncionarios(self)
            self.tela_registro_funcs.destroyed.connect(self.on_tela_registro_funcs_fechada)
            self.tela_registro_funcs.show()
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao abrir tela de registro de Funcionarios: {str(e)}")
            print(f"Erro detalhado: {traceback.format_exc()}")
    
    def abrir_tela_Lancamentos(self):
         try:
             self.tela_vendas = TelaVenda(self)
             self.tela_vendas.destroyed.connect(self.on_tela_vendas_fechada)
             self.tela_vendas.show()
         except Exception as e:
             QMessageBox.critical(self, "Erro", f"Erro ao abrir tela de Vendas: {str(e)}")
             print(f"Erro detalhado: {traceback.format_exc()}")        
   
    def abrir_tela_login(self):
        try:
            self.tela_login = Login(self)
            self.tela_login.destroyed.connect(self.on_tela_login_fechada)
            self.tela_login.show()
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao abrir tela de login: {str(e)}")
            print(f"Erro detalhado: {traceback.format_exc()}")

    def abrir_tela_grafico(self):
        try:
            self.tela_grafico = TelaGrafico(self)
            self.tela_grafico.destroyed.connect(self.on_tela_grafico_fechada)
            self.tela_grafico.show()
            
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao abrir tela de gráficos: {str(e)}")
            print(f"Erro detalhado: {traceback.format_exc()}")
    
    def abrir_tela_banco_dados(self):
        try:
            self.tela_banco_dados = BancoDados(self)
            self.tela_banco_dados.destroyed.connect(self.on_tela_banco_dados_fechada)
            self.tela_banco_dados.show()
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao abrir tela de gráficos: {str(e)}")
            print(f"Erro detalhado: {traceback.format_exc()}")

    def abrir_tela_consultar_geral_ordens_servicos(self):
        try:
            self.tela_ordem_servicos = OrdemServicos(self)
            self.tela_ordem_servicos.destroyed.connect(self.on_tela_ordem_servicos_fechada)
            self.tela_ordem_servicos.show()
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao abrir tela de ordens de serviço: {str(e)}")
            print(f"Erro detalhado: {traceback.format_exc()}")
 
    def abrir_tela_estoque(self):
        try:
            self.tela_estoque = TelaEstoque(self)
            self.tela_estoque.destroyed.connect(self.on_tela_estoque_fechada)
            self.tela_estoque.show()
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao abrir tela de estoque: {str(e)}")
            print(f"Erro detalhado: {traceback.format_exc()}")

    def abrir_telanota(self):
        try:
            self.telanota = TelaNotaFiscal(self)
            self.telanota.destroyed.connect(self.on_telanota_fechada)
            self.telanota.show()
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao abrir telanota de estoque: {str(e)}")
            print(f"Erro detalhado: {traceback.format_exc()}") 

    # FECHAMENTO DAS TELAS           
    def on_tela_estoque_fechada(self):
        print("Tela ficha estoque fechada!")

    def on_telanota_fechada(self):
        print("Tela Nota Fiscal Fechada!")    
    
    def on_tela_pedido_fechada(self):
        print("Tela pedido fechada")

    def on_tela_vendas_fechada(self):
         print("Tela de vendas fechada")
    
    def on_tela_ficha_cliente_fechada(self):
        print("Tela ficha cliente fechada")
      
    def on_tela_banco_dados_fechada(self):
         print("Tela Banco Dados fechada")

    def on_tela_grafico_fechada(self): 
        print("Tela de gráficos fechada")
  
    def on_tela_pedido_fechada(self):
        print("Tela pedido fechada")
   
    def on_tela_login_fechada(self):
        print("Tela de login fechada")

    def on_tela_registro_fechada(self):
        print("Tela de registro fechada")

    def on_tela_consulta_fechada(self):
        print("Tela de consulta fechada")
    
    def on_tela_consultar_cliente_fechada(self):
        print("Tela de consulta cliente fechada")

    def on_tela_ordem_servicos_fechada(self):
        print("Tela de ordens de serviço fechada")
        
    # FUNÇÕES DE FECHAMENTO E ENCERRAMENTO
    def fechar_conexoes(self):
        if hasattr(self, 'db'):
            self.db.fechar_conexao()
    
    # FUNÇÕES DE ENCERRAMENTO         
    def closeEvent(self, event):
        self.fechar_conexoes()
        event.accept()

# EXECUÇÃO PRINCIPAL
if __name__ == "__main__":
    app = QApplication(sys.argv)
    login = Login()
    login.show()
    
    # Executar a aplicação e aguardar
    app.exec_()
    
    # Após fechar a janela de login, verificar se foi bem-sucedido
    if login.login_foi_bem_sucedido():
        main_window = ClienteApp()
        main_window.show()
        sys.exit(app.exec_())
    else:
        sys.exit()