import PyQt5
from PyQt5 import QtWidgets
import psycopg2 as db
import gerenciador_de_telas

connection = db.connect(user="postgres", password="welL2801", host="localhost", port="5432", database="teste")



app = QtWidgets.QApplication([])

if __name__ == '__main__':
    gerenciador_de_telas.load_screens()
    gerenciador_de_telas.load_actions()
    gerenciador_de_telas.tela_login_admin.show()

    app.exec()
