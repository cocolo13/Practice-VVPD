"""Программа для расчёта расстояний между двумя прямоугольниками"""
import sys
import math
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMessageBox
import second

Form, Window = uic.loadUiType("program.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()


def cg_distance(x1, y1, x2, y2, x3, y3, x4, y4):
    first_cg = (math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)) / 2
    second_cg = (math.sqrt((x3 - x4) ** 2 + (y3 - y4) ** 2)) / 2
    cg_dist = round(math.sqrt((first_cg + second_cg) ** 2), 2)
    return cg_dist


def corner_distance(x1, y1, x2, y2, x3, y3, x4, y4):
    dist_left_corner = round(math.sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2), 2)
    dist_right_corner = round(math.sqrt((x2 - x4) ** 2 + (y2 - y4) ** 2), 2)
    return dist_left_corner + dist_right_corner


def click_in_btn1():
    global window_2
    window_2 = second.QtWidgets.QWidget()
    ui = second.Ui_Form()
    ui.setupUi(window_2)
    window_2.show()
    window.close()

    def click_in_done():
        try:
            x1 = ui.plainTextEdit.toPlainText()
            y1 = ui.plainTextEdit_2.toPlainText()
            x2 = ui.plainTextEdit_3.toPlainText()
            y2 = ui.plainTextEdit_8.toPlainText()
            x3 = ui.plainTextEdit_4.toPlainText()
            y3 = ui.plainTextEdit_5.toPlainText()
            x4 = ui.plainTextEdit_7.toPlainText()
            y4 = ui.plainTextEdit_6.toPlainText()
            if (not x1.isdigit() or not y1.isdigit() or
                    not x2.isdigit() or not y2.isdigit()
                    or not x3.isdigit() or not
                    y3.isdigit() or not x4.isdigit() or
                    not y4.isdigit()):
                raise AssertionError
            ui.pushButton.clicked.connect(window.show)
            ui.pushButton.clicked.connect(window_2.close)
            form.label.setText(f"                 "
                               f"Результат: "
                               f"{cg_distance(int(x1), int(y1), int(x2), int(y2), int(x3), int(y3), int(x4), int(y4))}")
        except AssertionError:
            error = QMessageBox()
            error.setWindowTitle("Ошибка")
            error.setText("Необходимо вводить целые числа!")
            error.setIcon(QMessageBox.Warning)
            error.StandardButton(QMessageBox.Ok)
            error.exec_()

    ui.pushButton.clicked.connect(click_in_done)


def click_in_btn2():
    global window_2
    window_2 = second.QtWidgets.QWidget()
    ui = second.Ui_Form()
    ui.setupUi(window_2)
    window_2.show()
    window.close()

    def click_in_done():
        try:
            x1 = ui.plainTextEdit.toPlainText()
            y1 = ui.plainTextEdit_2.toPlainText()
            x2 = ui.plainTextEdit_3.toPlainText()
            y2 = ui.plainTextEdit_8.toPlainText()
            x3 = ui.plainTextEdit_4.toPlainText()
            y3 = ui.plainTextEdit_5.toPlainText()
            x4 = ui.plainTextEdit_7.toPlainText()
            y4 = ui.plainTextEdit_6.toPlainText()
            if (not x1.isdigit() or not y1.isdigit()
                    or not x2.isdigit() or not y2.isdigit()
                    or not x3.isdigit() or not y3.isdigit()
                    or not x4.isdigit() or
                    not y4.isdigit()):
                raise AssertionError
            ui.pushButton.clicked.connect(window.show)
            ui.pushButton.clicked.connect(window_2.close)
            form.label.setText(f"                 "
                               f"Результат: {corner_distance(int(x1), int(y1), int(x2), int(y2), int(x3), int(y3), int(x4), int(y4))}")
        except AssertionError:
            error = QMessageBox()
            error.setWindowTitle("Ошибка")
            error.setText("Необходимо вводить целые числа!")
            error.setIcon(QMessageBox.Warning)
            error.StandardButton(QMessageBox.Ok)
            error.exec_()

    ui.pushButton.clicked.connect(click_in_done)


form.pushButton.clicked.connect(click_in_btn1)
form.pushButton_2.clicked.connect(click_in_btn2)
form.pushButton_3.clicked.connect(window.close)
sys.exit(app.exec_())
