import sys
sys.path.insert(0, '..')
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QApplication
import os
import xml.etree.ElementTree as ET
from BLL.Authentication.authentication import check_credentials

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 768)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setGeometry(450, 500, 411, 71)
        self.pushButton.setObjectName("pushButton")

        self.password_label = QLineEdit(self.centralwidget)
        self.password_label.setGeometry(590, 390, 271, 61)
        font = self.password_label.font()
        font.setPointSize(16)
        self.password_label.setFont(font)
        self.password_label.setObjectName("password_label")

        self.login_label = QLineEdit(self.centralwidget)
        self.login_label.setGeometry(590, 300, 271, 61)
        font = self.login_label.font()
        font.setPointSize(16)
        self.login_label.setFont(font)
        self.login_label.setText("")
        self.login_label.setObjectName("login_label")

        self.label = QLabel(self.centralwidget)
        self.label.setGeometry(450, 310, 91, 51)
        font = self.label.font()
        font.setPointSize(25)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setGeometry(450, 400, 121, 51)
        font = self.label_2.font()
        font.setPointSize(25)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = MainWindow.statusBar()
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        current_directory = os.path.dirname(__file__)
        xml_file_path = os.path.join(current_directory, '..', 'Style', 'styles.xml')
        tree = ET.parse(xml_file_path)
        root = tree.getroot()
        self.password_label.setEchoMode(QLineEdit.Password)
        self.login_label.setStyleSheet(root.find('line_edit_style/value').text)
        self.password_label.setStyleSheet(root.find('line_edit_style/value').text)
        self.pushButton.setStyleSheet(root.find('QPushButton_style/value').text)
        self.loginFunction()
        self.retranslateUi(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Логін:"))
        self.label_2.setText(_translate("MainWindow", "Пароль:"))
        self.pushButton.setText(_translate("MainWindow", "Увійти"))

    def loginFunction(self):
        self.pushButton.clicked.connect(lambda: check_credentials(self.login_label.text(),
                                                                      self.password_label.text()))
