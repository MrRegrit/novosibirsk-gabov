import sqlite3
import sys

import PyQt5.QtWidgets
import PyQt5.uic

import UI.addEditCoffeeForm
import UI.main_Ui


class MainWidget(
    PyQt5.QtWidgets.QWidget,
    UI.main_Ui.Ui_Form,
):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.setupUi(self)

        connect = sqlite3.connect("data/coffee.sqlite")
        cursor = connect.cursor()
        coffee = cursor.execute("SELECT * FROM coffee").fetchall()
        connect.close()

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
                "ID",
                "название сорта",
                "степень обжарки",
                "молотый/в зернах",
                "описание вкуса",
                "цена",
                "объем упаковки",
            ],
        )


class AddEditCoffeeWidget(
    PyQt5.QtWidgets.QWidget,
    UI.addEditCoffeeForm.Ui_Form
):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ex = MainWidget()
        self.ex.show()
        self.load_coffee_title()
        self.select_box.activated.connect(self.load_coffee)
        self.chenge.clicked.connect(self.change_coffee)
        self.create_b.clicked.connect(self.create_coffee)
        if self.select_box.currentIndex() != -1:
            self.load_coffee(0)

    def load_coffee_title(self):
        connect = sqlite3.connect("data/coffee.sqlite")
        cursor = connect.cursor()
        coffee_titles = cursor.execute("SELECT title FROM coffee").fetchall()
        connect.close()
        coffee_titles = [i[0] for i in coffee_titles]
        self.select_box.clear()
        self.select_box.addItems(coffee_titles)

    def load_coffee(self, s):
        connect = sqlite3.connect("data/coffee.sqlite")
        cursor = connect.cursor()
        coffee = cursor.execute(
            f"SELECT * FROM coffee " f"WHERE id = {s + 1}",
        ).fetchone()
        connect.close()
        self.title.setText(coffee[1])
        self.roasting.setText(coffee[2])
        self.ground.setText(coffee[3])
        self.taste.setText(coffee[4])
        self.price.setValue(coffee[5])
        self.packege.setValue(coffee[6])

    def change_coffee(self):
        title = self.title.text()
        roasting = self.roasting.text()
        ground = self.ground.text()
        taste = self.taste.text()
        price = self.price.value()
        packege = self.packege.value()
        id = self.select_box.currentIndex() + 1
        connect = sqlite3.connect("data/coffee.sqlite")
        cursor = connect.cursor()
        cursor.execute(
            "UPDATE coffee "
            f"SET title = '{title}', "
            f"roasting = '{roasting}', "
            f"ground = '{ground}', "
            f"taste = '{taste}', "
            f"price = {price}, "
            f"packege = {packege} "
            f"WHERE id = {id}",
        )
        connect.commit()
        connect.close()
        self.load_coffee_title()
        self.ex = MainWidget()
        self.ex.show()

    def create_coffee(self):
        title = self.title.text()
        roasting = self.roasting.text()
        ground = self.ground.text()
        taste = self.taste.text()
        price = self.price.value()
        packege = self.packege.value()
        connect = sqlite3.connect("data/coffee.sqlite")
        cursor = connect.cursor()
        cursor.execute(
            "INSERT INTO coffee "
            "(title, roasting, ground, taste, price, packege) "
            "VALUES "
            f"('{title}', "
            f"'{roasting}', "
            f"'{ground}', "
            f"'{taste}', "
            f"{price},"
            f"{packege})",
        )
        connect.commit()
        connect.close()
        self.load_coffee_title()
        self.ex = MainWidget()
        self.ex.show()


if __name__ == "__main__":
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    ex = AddEditCoffeeWidget()
    ex.show()
    sys.exit(app.exec())
