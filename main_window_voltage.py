# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Aleksey\PycharmProjects\valtage_nomer_sait\main_window_voltage.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(794, 195)
        MainWindow.setMaximumSize(QtCore.QSize(1200, 300))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.LE_input_nomer = QtWidgets.QLineEdit(self.centralwidget)
        self.LE_input_nomer.setEnabled(True)
        self.LE_input_nomer.setGeometry(QtCore.QRect(260, 10, 521, 60))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LE_input_nomer.sizePolicy().hasHeightForWidth())
        self.LE_input_nomer.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(False)
        font.setWeight(50)
        self.LE_input_nomer.setFont(font)
        self.LE_input_nomer.setText("")
        self.LE_input_nomer.setObjectName("LE_input_nomer")
        self.L_Description = QtWidgets.QLabel(self.centralwidget)
        self.L_Description.setGeometry(QtCore.QRect(20, 40, 211, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.L_Description.setFont(font)
        self.L_Description.setObjectName("L_Description")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 80, 761, 51))
        self.label.setText("")
        self.label.setObjectName("label")
        self.B_Search = QtWidgets.QPushButton(self.centralwidget)
        self.B_Search.setGeometry(QtCore.QRect(310, 130, 150, 35))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.B_Search.setFont(font)
        self.B_Search.setObjectName("B_Search")
        self.B_exit = QtWidgets.QPushButton(self.centralwidget)
        self.B_exit.setGeometry(QtCore.QRect(630, 130, 150, 35))
        self.B_exit.setObjectName("B_exit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.L_Description.setText(_translate("MainWindow", "Введите номер детали:"))
        self.B_Search.setText(_translate("MainWindow", "Поиск"))
        self.B_exit.setText(_translate("MainWindow", "Закрыть"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
