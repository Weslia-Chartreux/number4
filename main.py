import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QTableWidgetItem
from PyQt5 import uic
import sqlite3


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        con = sqlite3.connect("coffee.sqlite")
        cur = con.cursor()
        res = cur.execute('SELECT * FROM list').fetchall()
        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels(['ID', 'название сорта',
                                              'степень обжарки', 'молотый', 'описание вкуса',
                                              'цена', 'объем упаковки'])
        self.table.setRowCount(0)
        for i, row in enumerate(res):
            self.table.setRowCount(
                self.table.rowCount() + 1)
            for j, elem in enumerate(row):
                if j == 3:
                    elem = 'да' if elem else 'нет'
                self.table.setItem(
                    i, j, QTableWidgetItem(str(elem)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())