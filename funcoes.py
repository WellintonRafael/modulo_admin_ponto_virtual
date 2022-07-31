import gerenciador_de_telas
import run_sql
from PyQt5 import QtWidgets

# Funções para abertura e fechamento de telas.
# Também limpa as labels e os campos de input.
def abre_tela_pesquisa() -> None:
    gerenciador_de_telas.tela_login_admin.close()
    gerenciador_de_telas.tela_pesquisa.show()
    gerenciador_de_telas.tela_pesquisa.label_5.setText('')
    gerenciador_de_telas.tela_pesquisa.lineEdit_2.setText('')
    gerenciador_de_telas.tela_pesquisa.lineEdit_3.setText('')
    gerenciador_de_telas.tela_pesquisa.pushButton_corrigir.setEnabled(False)
    gerenciador_de_telas.tela_pesquisa.pushButton_pdf.setEnabled(False)
    gerenciador_de_telas.tela_pesquisa.radioButton_tudo.setChecked(True)
    gerenciador_de_telas.tela_pesquisa.tableWidget.setRowCount(0)
    gerenciador_de_telas.tela_pesquisa.tableWidget.setColumnCount(8)
    lista_de_nomes = run_sql.select_todos_nomes()
    nova_lista = list()
    for item in lista_de_nomes:
        item = item[0]
        nova_lista.append(item)
    gerenciador_de_telas.tela_pesquisa.comboBox.addItems(nova_lista)
    # Iterador que lista os dados em uma "table" da tela pesquisa:
    for i in range(0):
        for c in range(0, 8):
            gerenciador_de_telas.tela_pesquisa.tableWidget.setItem
            (i, c, QtWidgets.QTableWidgetItem(''[i][c]))




def verificar_login(login, senha):
    run_sql.query_geral_de_1_item(login, senha, )
