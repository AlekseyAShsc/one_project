# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Aleksey\PycharmProjects\voltaz_nomer\main_window_voltage.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 850)
        MainWindow.setMaximumSize(QtCore.QSize(1200, 1000))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.LE_input_nomer = QtWidgets.QLineEdit(self.centralwidget)
        self.LE_input_nomer.setEnabled(True)
        self.LE_input_nomer.setGeometry(QtCore.QRect(260, 10, 411, 60))
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
        self.L_Description.setGeometry(QtCore.QRect(20, 30, 211, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.L_Description.setFont(font)
        self.L_Description.setObjectName("L_Description")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 740, 771, 81))
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.B_Search = QtWidgets.QPushButton(self.centralwidget)
        self.B_Search.setGeometry(QtCore.QRect(680, 10, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.B_Search.setFont(font)
        self.B_Search.setObjectName("B_Search")
        self.B_exit = QtWidgets.QPushButton(self.centralwidget)
        self.B_exit.setGeometry(QtCore.QRect(680, 70, 111, 51))
        self.B_exit.setObjectName("B_exit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 651, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_2.setFont(font)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 140, 771, 591))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
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
