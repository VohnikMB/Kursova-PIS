# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'profilEmployee.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1371, 926)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ico = QtWidgets.QLabel(self.centralwidget)
        self.ico.setGeometry(QtCore.QRect(1250, 0, 111, 111))
        self.ico.setMaximumSize(QtCore.QSize(122, 125))
        self.ico.setText("")
        self.ico.setTextFormat(QtCore.Qt.RichText)
        self.ico.setPixmap(QtGui.QPixmap("../../Shared/ICO/Default_Profile_Picture.png"))
        self.ico.setScaledContents(True)
        self.ico.setWordWrap(False)
        self.ico.setObjectName("ico")
        self.name = QtWidgets.QLabel(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(1240, 120, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.name.setFont(font)
        self.name.setScaledContents(False)
        self.name.setAlignment(QtCore.Qt.AlignCenter)
        self.name.setObjectName("name")
        self.exit = QtWidgets.QLabel(self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(1240, 180, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.exit.setFont(font)
        self.exit.setStyleSheet("color: rgb(255, 0, 0);")
        self.exit.setScaledContents(False)
        self.exit.setAlignment(QtCore.Qt.AlignCenter)
        self.exit.setObjectName("exit")
        self.work = QtWidgets.QLabel(self.centralwidget)
        self.work.setGeometry(QtCore.QRect(1240, 150, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.work.setFont(font)
        self.work.setScaledContents(False)
        self.work.setAlignment(QtCore.Qt.AlignCenter)
        self.work.setObjectName("work")
        self.jobInstructions = QtWidgets.QPushButton(self.centralwidget)
        self.jobInstructions.setGeometry(QtCore.QRect(440, 60, 371, 71))
        self.jobInstructions.setObjectName("jobInstructions")
        self.vacationSchedule = QtWidgets.QPushButton(self.centralwidget)
        self.vacationSchedule.setGeometry(QtCore.QRect(440, 170, 371, 71))
        self.vacationSchedule.setObjectName("vacationSchedule")
        self.staffList = QtWidgets.QPushButton(self.centralwidget)
        self.staffList.setGeometry(QtCore.QRect(440, 280, 371, 71))
        self.staffList.setObjectName("staffList")
        self.reqSpecification = QtWidgets.QPushButton(self.centralwidget)
        self.reqSpecification.setGeometry(QtCore.QRect(440, 390, 371, 71))
        self.reqSpecification.setObjectName("reqSpecification")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.loginFunction()
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.name.setText(_translate("MainWindow", "[name]"))
        self.exit.setText(_translate("MainWindow", "Exit"))
        self.work.setText(_translate("MainWindow", "[work]"))
        self.jobInstructions.setText(_translate("MainWindow", "Посадові інструкції"))
        self.vacationSchedule.setText(_translate("MainWindow", "Графік відпусток"))
        self.staffList.setText(_translate("MainWindow", "Штатний розпис і витяг"))
        self.reqSpecification.setText(_translate("MainWindow", "Отримата характеристику"))

    def loginFunction(self):
        self.pushButton.clicked.connect(lambda: check_credentials(self.login_label.text(),
                                                                  self.password_label.text()))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
