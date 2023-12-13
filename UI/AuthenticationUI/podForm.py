from PyQt5.QtWidgets import (
    QLineEdit, QLabel, QMainWindow,
    QMessageBox, QWidget, QPushButton, QDateEdit)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QDate
from datetime import datetime
import os
import xml.etree.ElementTree as ET
from BLL.Accounting.form32 import generate_account_request

current_directory = os.path.dirname(__file__)
xml_file_path = os.path.join(current_directory, '..', 'Style', 'styles.xml')
tree = ET.parse(xml_file_path)
root = tree.getroot()
font = QFont()
class Ui_Frame(QMainWindow):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.setup_ui()

    def setup_ui(self):

        self.setWindowTitle('Податкова форма. Для III групи 2%')
        self.setGeometry(0, 0, 1366, 768)
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.label = QLabel(self.central_widget)
        self.label.setGeometry(500, 60, 331, 61)
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.pushButton = QPushButton(self.central_widget)
        self.pushButton.setGeometry(280, 590, 161, 61)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet(root.find('QPushButton_style/value').text)
        self.pushButton.clicked.connect(self.exit_clicked)

        self.pushButton_2 = QPushButton(self.central_widget)
        self.pushButton_2.setGeometry(910, 590, 161, 61)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setStyleSheet(root.find('QPushButton_Profile_style/value').text)


        self.label_4 = QLabel(self.central_widget)
        self.label_4.setGeometry(60, 250, 771, 21)
        font.setPointSize(13)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.lineEdit_3 = QLineEdit(self.central_widget)
        self.lineEdit_3.setGeometry(1090, 240, 161, 41)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.label_5 = QLabel(self.central_widget)
        self.label_5.setGeometry(60, 200, 771, 21)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.dateEdit = QDateEdit(self.central_widget)
        self.dateEdit.setGeometry(1090, 190, 161, 41)
        self.dateEdit.setFont(font)
        current_date = datetime.now().date()
        self.dateEdit.setDate(QDate(current_date.year, current_date.month, current_date.day))

        self.label_6 = QLabel(self.central_widget)
        self.label_6.setGeometry(60, 300, 991, 51)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        self.lineEdit_4 = QLineEdit(self.central_widget)
        self.lineEdit_4.setGeometry(1090, 310, 161, 41)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setObjectName("lineEdit_4")

        self.label_7 = QLabel(self.central_widget)
        self.label_7.setGeometry(60, 380, 991, 41)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")

        self.lineEdit_5 = QLineEdit(self.central_widget)
        self.lineEdit_5.setGeometry(1090, 380, 161, 41)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setObjectName("lineEdit_5")

        self.label.setText("Податкова форма. Для III групи 2%")
        self.pushButton.setText("Назад")
        self.pushButton_2.setText("Відправити")
        self.label_4.setText("Обсяг доходу за податковий (звітний) місяць, що оподатковується за ставкою 2 відсотки доходу:")
        self.label_5.setText("Податковий (звітний) період, який уточнюється:")
        self.label_6.setText("Позитивне значення різниці між сумою загального мінімального\n"
                             "податкового зобов’язання та загальною сумою сплачених податків, зборів, "
                             "платежів та витрат на оренду земельних ділянок:")
        self.label_7.setText("Уточнена сума податкових зобов’язань за податковий (звітний) період, у якому виявлена помилка:")

        line_edits = [self.lineEdit_3, self.lineEdit_4, self.lineEdit_5]
        self.lineEdit_4.editingFinished.connect(lambda: self.are_line_edits_filled(line_edits))
        self.lineEdit_5.editingFinished.connect(lambda: self.are_line_edits_filled(line_edits))
        self.lineEdit_3.editingFinished.connect(lambda: self.are_line_edits_filled(line_edits))
        self.pushButton_2.clicked.connect(lambda: self.are_line_edits_filled(line_edits))


        self.show()

    def exit_clicked(self):
        self.close()


    def are_line_edits_filled(self, line_edits):
        for line_edit in line_edits:
            if line_edit.text().strip() == "":
                return False
        self.pushButton_2.setStyleSheet(root.find('QPushButton_styleVacation/value').text)
        self.pushButton_2.clicked.connect(self.sendForm)
        return True

    def sendForm(self):
       if generate_account_request(
               self.name,
               self.dateEdit.date().toString("MM"),
               self.dateEdit.date().toString("yyyy"),
               self.lineEdit_3.text(),
               self.lineEdit_4.text(),
               self.lineEdit_5.text()
                                    ):
           dialog = QMessageBox()
           dialog.setWindowTitle("Форма відправлена")
           dialog.setText("Податкова форма відправленна.")
           self.close()
           dialog.exec_()