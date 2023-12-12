from PyQt5.QtWidgets import (
    QLineEdit, QLabel, QMainWindow,
    QRadioButton, QButtonGroup, QMessageBox,
    QWidget, QPushButton, QTextBrowser)
from PyQt5.QtGui import QFont
from BLL.Registration.registrationALL import *
import os
import xml.etree.ElementTree as ET


class RegistrationWindow(QMainWindow):
    def __init__(self, password):
        super().__init__()
        self.password = password
        self.init_ui()

    def init_ui(self):
        current_directory = os.path.dirname(__file__)
        xml_file_path = os.path.join(current_directory, '..', 'Style', 'styles.xml')
        tree = ET.parse(xml_file_path)
        root = tree.getroot()
        font = QFont()
        font.setPointSize(14)

        self.setWindowTitle('Реєстрація користувача')
        self.setGeometry(0, 0, 1366, 768)
        self.centralwidget = QWidget()
        self.setCentralWidget(self.centralwidget)

        self.radioButtonEmp = QRadioButton(self.centralwidget)
        self.radioButtonEmp.setGeometry(60, 220, 121, 21)
        self.radioButtonEmp.setFont(font)
        self.radioButtonEmp.setObjectName("1")
        self.radioButtonEmp.setText("Працівник")

        self.buttonGroup = QButtonGroup(self.centralwidget)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.radioButtonEmp)

        self.radioButton_2 = QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(190, 220, 91, 21)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("2")
        self.buttonGroup.addButton(self.radioButton_2)
        self.radioButton_2.setText("HR")

        self.radioButton_3 = QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(260, 210, 121, 41)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName("4")
        self.buttonGroup.addButton(self.radioButton_3)
        self.radioButton_3.setText("Бухгалтер")

        self.buttonGroupName = self.buttonGroup.buttonClicked.connect(self.get_button_object_name)

        self.label = QLabel(self.centralwidget)
        self.label.setGeometry(60, 70, 61, 31)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label.setText("Логін")

        self.linePassword = QLineEdit(self.centralwidget)
        self.linePassword.setGeometry(180, 150, 201, 31)
        self.linePassword.setObjectName("linePassword")
        self.linePassword.setStyleSheet(root.find('line_edit_style/value').text)
        self.linePassword.setFont(font)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setGeometry(60, 144, 71, 41)
        self.label_2.setText("Пароль")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.lineLogin = QLineEdit(self.centralwidget)
        self.lineLogin.setGeometry(180, 70, 201, 31)
        self.lineLogin.setObjectName("lineLogin")
        self.lineLogin.setStyleSheet(root.find('line_edit_style/value').text)
        self.lineLogin.setFont(font)

        self.lineIPP = QLineEdit(self.centralwidget)
        self.lineIPP.setGeometry(180, 276, 201, 31)
        self.lineIPP.setObjectName("lineIPP")
        self.lineIPP.setStyleSheet(root.find('line_edit_style/value').text)
        self.lineIPP.setFont(font)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setText("ІПП")
        self.label_3.setGeometry(60, 270, 71, 41)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.line_full_title_position = QLineEdit(self.centralwidget)
        self.line_full_title_position.setGeometry(180, 346, 201, 31)
        self.line_full_title_position.setObjectName("full_title_position")
        self.line_full_title_position.setStyleSheet(root.find('line_edit_style/value').text)
        self.line_full_title_position.setFont(font)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setGeometry(60, 330, 121, 51)
        self.label_4.setText("Повна назва")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setGeometry(60, 350, 71, 41)
        self.label_5.setText("посади")
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setGeometry(60, 403, 111, 41)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_6.setText("Ваш пароль")

        self.line_HR_Password = QLineEdit(self.centralwidget)
        self.line_HR_Password.setGeometry(180, 410, 201, 31)
        self.line_HR_Password.setStyleSheet(root.find('line_edit_style/value').text)
        self.line_HR_Password.setObjectName("line_HR_Password")
        self.line_HR_Password.setFont(font)
        self.line_HR_Password.setEchoMode(QLineEdit.Password)

        self.textEdit = QTextBrowser(self.centralwidget)
        self.textEdit.setGeometry(560, 70, 671, 511)
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setStyleSheet(root.find('line_edit_style/value').text)
        self.textEdit.setFont(font)

        self.exitButton = QPushButton(self.centralwidget)
        self.exitButton.setGeometry(60, 510, 121, 71)
        self.exitButton.setObjectName("exitButton")
        self.exitButton.setText("Назад")
        self.exitButton.setStyleSheet(root.find('QPushButton_style/value').text)

        self.regButton = QPushButton(self.centralwidget)
        self.regButton.setGeometry(190, 510, 201, 71)
        self.regButton.setObjectName("regButton")
        self.regButton.setText("Зареєструвати")
        self.regButton.setStyleSheet(root.find('QPushButton_Profile_style/value').text)

        self.exitButton.clicked.connect(self.exit_clicked)

        self.linePassword.installEventFilter(self)
        self.line_HR_Password.installEventFilter(self)
        self.lineLogin.installEventFilter(self)
        self.lineIPP.installEventFilter(self)
        self.line_full_title_position.installEventFilter(self)

        self.setTabOrder(self.lineLogin, self.linePassword)
        self.setTabOrder(self.linePassword, self.radioButtonEmp)
        self.setTabOrder(self.radioButtonEmp, self.lineIPP)
        self.setTabOrder(self.lineIPP, self.line_full_title_position)
        self.setTabOrder(self.line_full_title_position, self.line_HR_Password)

        self.lineIPP.editingFinished.connect(self.check_info)
        self.line_HR_Password.editingFinished.connect(self.check_info)
        self.line_full_title_position.editingFinished.connect(self.check_info)
        self.lineLogin.editingFinished.connect(self.check_info)
        self.linePassword.editingFinished.connect(self.check_info)
        self.show()

    def check_info(self):
        current_directory = os.path.dirname(__file__)
        xml_file_path = os.path.join(current_directory, '..', 'Style', 'styles.xml')
        tree = ET.parse(xml_file_path)
        root = tree.getroot()

        if (
                (not check_username_exists(self.lineLogin.text()))
                and (len(self.lineLogin.text()) > 4)
                and (validate_password(self.linePassword.text()))
                and (self.password == self.line_HR_Password.text())

        ):
            self.regButton.setStyleSheet(root.find('QPushButton_styleST/value').text)
            self.regButton.clicked.connect(self.register_worker)
        else:
            self.regButton.setStyleSheet(root.find('QPushButton_Profile_style/value').text)

    def register_worker(self):
        selected_button = self.buttonGroup.checkedButton()
        if not selected_button:
            selected_button = 1
        if register_new_worker(
                self.lineLogin.text(),
                self.linePassword.text(),
                int(selected_button.objectName()),
                self.lineIPP.text(),
                self.line_full_title_position.text()
        ):
            dialog = QMessageBox()
            dialog.setText("Успішна реєстрація")
            dialog.setWindowTitle("Успішна реєстрація")
            self.close()
            dialog.exec_()


    def eventFilter(self, obj, event):
        self.odj_name(obj)
        return super().eventFilter(obj, event)

    def odj_name(self, text):
        from BLL.Registration.textEditDef import object_nameDef
        object_name = text.objectName()
        self.textEdit.setText(object_nameDef(object_name))

    def exit_clicked(self, event):
        self.close()

    @staticmethod
    def get_button_object_name(button):
        #print(button.objectName())
        return button.objectName()
