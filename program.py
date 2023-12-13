# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'program.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CalculateDist(object):
    def setupUi(self, CalculateDist):
        CalculateDist.setObjectName("CalculateDist")
        CalculateDist.resize(1588, 800)
        font = QtGui.QFont()
        font.setPointSize(9)
        CalculateDist.setFont(font)
        CalculateDist.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.750273, cy:0.25, radius:2, fx:0, fy:1, stop:0 rgba(0, 17, 160, 255), stop:1 rgba(255, 255, 255, 255));\n"
"background-color: qradialgradient(spread:pad, cx:1, cy:0, radius:2, fx:0, fy:1, stop:0 rgba(14, 29, 160, 255), stop:1 rgba(255, 255, 255, 255));")
        self.centralwidget = QtWidgets.QWidget(CalculateDist)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 540, 1621, 241))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(110, 30, 600, 200))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255)")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(900, 30, 600, 200))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("color: rgb(255, 255, 255)")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(500, 270, 600, 200))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("color: rgb(255, 255, 255)")
        self.pushButton_3.setObjectName("pushButton_3")
        CalculateDist.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(CalculateDist)
        self.statusbar.setObjectName("statusbar")
        CalculateDist.setStatusBar(self.statusbar)

        self.retranslateUi(CalculateDist)
        QtCore.QMetaObject.connectSlotsByName(CalculateDist)

    def retranslateUi(self, CalculateDist):
        _translate = QtCore.QCoreApplication.translate
        CalculateDist.setWindowTitle(_translate("CalculateDist", "Расчёт расстояний между прямоугольниками"))
        self.label.setText(_translate("CalculateDist", "Здесь будет результат"))
        self.pushButton.setText(_translate("CalculateDist", "Посчитать расстояние между центрами\n"
"           тяжести двух прямоугольникво"))
        self.pushButton_2.setText(_translate("CalculateDist", "Посчитать сумму расстояние между\n"
"        верхними левыми и нижними правыми углами \n"
"          двух прямоугольников"))
        self.pushButton_3.setText(_translate("CalculateDist", "Выйти"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CalculateDist = QtWidgets.QMainWindow()
    ui = Ui_CalculateDist()
    ui.setupUi(CalculateDist)
    CalculateDist.show()
    sys.exit(app.exec_())
