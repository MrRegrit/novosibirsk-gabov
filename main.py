import sys
import sqlite3

import PyQt5.QtWidgets

import Ui


class MainWidget(
    PyQt5.QtWidgets.QWidget,
    Ui.Ui_Form,
):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.setupUi(self)

        connect = sqlite3.connect("coffee.sqlite")
        cursor = connect.cursor()
        coffee = cursor.execute("SELECT * FROM coffee").fetchall()

        self.table.setRowCount(len(coffee))
        self.table.setColumnCount(7)

        for y, cof in enumerate(coffee):
            for x, table_item in enumerate(cof):
                self.table.setItem(
                    y,
                    x,
                    PyQt5.QtWidgets.QTableWidgetItem(str(table_item)),
                )

        self.table.resizeColumnsToContents()
        self.table.setHorizontalHeaderLabels(
            [
                'ID',
                'название сорта',
                'степень обжарки',
                'молотый/в зернах',
                'описание вкуса',
                'цена',
                'объем упаковки'
            ],
        )


if __name__ == '__main__':
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    ex = MainWidget()
    ex.show()
    sys.exit(app.exec())
