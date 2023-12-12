from PyQt5.QtWidgets import (
    QLineEdit, QLabel, QMainWindow,
    QRadioButton, QButtonGroup, QMessageBox,
    QWidget, QPushButton, QDateEdit)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QDate
from BLL.Vacation.vacationForm import generate_leave_request
from datetime import datetime
import os
import xml.etree.ElementTree as ET

current_directory = os.path.dirname(__file__)
xml_file_path = os.path.join(current_directory, '..', 'Style', 'styles.xml')
tree = ET.parse(xml_file_path)
root = tree.getroot()


class Ui_Vacation(QMainWindow):

    def __init__(self, user_name, full_work):
        super().__init__()
        self.user_name = user_name
        self.full_work = full_work
        self.init_ui()

    def init_ui(self):
        font = QFont()
        font.setPointSize(14)

        self.setWindowTitle('Відпустка')
        self.setGeometry(0, 0, 1366, 768)
        self.centralwidget = QWidget()
        self.setCentralWidget(self.centralwidget)

        self.label = QLabel(self.centralwidget)
        self.label.setGeometry(550, 90, 181, 61)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label.setText("Заява на відпустку.")

        self.radioButton = QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(280, 180, 131, 51)
        font.setPointSize(13)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("1")

        self.radioButton2 = QRadioButton(self.centralwidget)
        self.radioButton2.setGeometry(280, 240, 141, 41)
        self.radioButton2.setFont(font)
        self.radioButton2.setObjectName("2")

        self.buttonGroup = QButtonGroup(self.centralwidget)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.radioButton2)
        self.buttonGroup.addButton(self.radioButton)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setGeometry(880, 195, 51, 21)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setGeometry(870, 255, 47, 21)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setGeometry(540, 340, 101, 21)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(640, 330, 161, 41)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet(root.find('line_edit_style/value').text)
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.dateEdit = QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(930, 185, 141, 41)
        self.dateEdit.setFont(font)
        self.dateEdit.setObjectName("dateEdit")
        current_date = datetime.now().date()
        self.dateEdit.setDate(QDate(current_date.year, current_date.month, current_date.day))

        self.dateEdit_2 = QDateEdit(self.centralwidget)
        self.dateEdit_2.setGeometry(930, 245, 141, 41)
        self.dateEdit_2.setFont(font)
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.dateEdit_2.setDate(QDate(current_date.year, current_date.month, current_date.day + 1))

        self.dateEdit_2.setStyleSheet(root.find('line_edit_style/value').text)
        self.dateEdit.setStyleSheet(root.find('line_edit_style/value').text)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setGeometry(280, 500, 161, 61)
        self.pushButton.setObjectName("pushButton")
        self.radioButton.setChecked(True)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(910, 500, 161, 61)
        self.pushButton_2.setObjectName("pushButton_2")

        self.radioButton.setText("Оплачувана")
        self.radioButton2.setText("Неоплачувана")

        self.label_2.setText("З:")
        self.label_3.setText("До:")
        self.label_4.setText("У зв\'язку з:")
        self.pushButton.setText("Назад")
        self.pushButton_2.setText("Відправити")
        self.pushButton.setStyleSheet(root.find('QPushButton_style/value').text)
        self.pushButton_2.setStyleSheet(root.find('QPushButton_Profile_style/value').text)
        self.lineEdit_3.editingFinished.connect(self.sendVacation)
        self.pushButton.clicked.connect(self.exit_clicked)

        self.show()

    def sendVacation(self):
        self.pushButton_2.setStyleSheet(root.find('QPushButton_styleVacation/value').text)
        self.pushButton_2.clicked.connect(self.sendTrue)

    def sendTrue(self):
        selected_button = self.buttonGroup.checkedButton()
        selected_date = self.dateEdit.date()
        selected_date2 = self.dateEdit_2.date()
        if generate_leave_request(
                                  self.user_name,
                                  self.full_work,
                                  int(selected_button.objectName()),
                                  selected_date.toString("dd-MM-yyyy"),
                                  selected_date2.toString("dd-MM-yyyy"),
                                  self.lineEdit_3.text()
        ):
            dialog = QMessageBox()
            dialog.setWindowTitle("Заява відправлена")
            dialog.setText("Ваша заява на відпустку відправленна.")
            self.close()
            dialog.exec_()

    def exit_clicked(self, event):
        self.close()
