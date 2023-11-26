import os
import sys
import xml.etree.ElementTree as ET

from PyQt5 import QtCore, QtGui, QtWidgets

sys.path.insert(0, '..')
from BLL.Authentication.authentication import check_credentials

#from UI.Style.style import line_edit_style, QPushButton_style
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1371, 926)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(450, 500, 411, 71))
        self.pushButton.setObjectName("pushButton")
        self.password_label = QtWidgets.QLineEdit(self.centralwidget)
        self.password_label.setGeometry(QtCore.QRect(590, 390, 271, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.password_label.setFont(font)
        self.password_label.setObjectName("password_label")
        self.login_label = QtWidgets.QLineEdit(self.centralwidget)
        self.login_label.setGeometry(QtCore.QRect(590, 300, 271, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.login_label.setFont(font)
        self.login_label.setText("")
        self.login_label.setObjectName("login_label")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(450, 310, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(450, 400, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        current_directory = os.path.dirname(__file__)
        xml_file_path = os.path.join(current_directory, '..',  'Style', 'styles.xml')
        tree = ET.parse(xml_file_path)
        root = tree.getroot()

        self.login_label.setStyleSheet(root.find('line_edit_style/value').text)
        self.password_label.setStyleSheet(root.find('line_edit_style/value').text)
        self.pushButton.setStyleSheet(root.find('QPushButton_style/value').text)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Увійти"))
        self.label.setText(_translate("MainWindow", "Логін:"))
        self.label_2.setText(_translate("MainWindow", "Пароль:"))


if __name__ == "__main__":
    import sys

    print(check_credentials("user1","password1"))

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
