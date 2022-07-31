from PyQt5 import uic
import funcoes

def load_screens():
    global tela_login_admin
    global tela_pesquisa

    tela_login_admin = uic.loadUi("tela_login_admin.ui")
    tela_pesquisa = uic.loadUi("tela_pesquisa.ui")

def load_actions():


    

    

    tela_login_admin.pushButton.clicked.connect(funcoes.verificar_login)
    
    