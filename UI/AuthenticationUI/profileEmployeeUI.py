from PyQt5.QtWidgets import QMainWindow, QLabel, QWidget, QPushButton
from PyQt5.QtGui import QPixmap, QFont
from BLL.Authorization.job_instruktion import jobInstructions_box
from PyQt5 import QtCore
import os
from UI.AuthenticationUI.registrFormUI import RegistrationWindow
from UI.AuthenticationUI.podForm import Ui_Frame
from UI.AuthenticationUI.vacation import Ui_Vacation
import xml.etree.ElementTree as ET


class ProfileWindow(QMainWindow):
    def __init__(self, user_name, work_SQL_inf, full_work, password):
        super().__init__()
        self.password = password
        self.full_work = full_work
        self.work_SQL_inf = work_SQL_inf
        self.user_name = user_name

        self.init_ui()

    def init_ui(self):
        current_directory = os.path.dirname(__file__)
        xml_file_path = os.path.join(current_directory, '..', 'Style', 'styles.xml')
        tree = ET.parse(xml_file_path)
        root = tree.getroot()

        self.setWindowTitle('Профіль користувача')
        self.setGeometry(0, 0, 1366, 768)
        self.centralwidget = QWidget()
        self.setCentralWidget(self.centralwidget)

        self.ico = QLabel(self.centralwidget)
        self.ico.setGeometry(1250, 0, 111, 111)
        self.ico.setMaximumSize(122, 125)
        image_path = os.path.abspath('Shared/ICO/Default_Profile_Picture.png')
        pixmap = QPixmap(image_path)
        self.ico.setPixmap(pixmap)
        self.ico.setScaledContents(True)

        self.name = QLabel(self.centralwidget)
        self.name.setGeometry(1240, 120, 131, 20)
        font = QFont()
        font.setPointSize(11)
        self.name.setFont(font)
        self.name.setScaledContents(False)
        self.name.setAlignment(QtCore.Qt.AlignCenter)
        self.name.setObjectName("name")

        self.exit = QLabel(self.centralwidget)
        self.exit.setGeometry(1240, 180, 131, 20)

        self.exit.setFont(font)
        self.exit.setStyleSheet("color: rgb(255, 0, 0);")
        self.exit.setScaledContents(False)
        self.exit.setAlignment(QtCore.Qt.AlignCenter)
        self.exit.setObjectName("exit")
        self.exit.setText("Exit")

        self.work = QLabel(self.centralwidget)
        self.work.setGeometry(1240, 150, 131, 20)

        self.work.setFont(font)
        self.work.setScaledContents(False)
        self.work.setAlignment(QtCore.Qt.AlignCenter)
        self.work.setObjectName("work")

        self.jobInstructions = QPushButton(self.centralwidget)
        self.jobInstructions.setGeometry(440, 40, 371, 71)
        self.jobInstructions.setObjectName("jobInstructions")

        self.vacationSchedule = QPushButton(self.centralwidget)
        self.vacationSchedule.setGeometry(440, 150, 371, 71)
        self.vacationSchedule.setObjectName("vacationSchedule")

        self.staffList = QPushButton(self.centralwidget)
        self.staffList.setGeometry(440, 260, 371, 71)
        self.staffList.setObjectName("staffList")

        self.reqSpecification = QPushButton(self.centralwidget)
        self.reqSpecification.setGeometry(440, 370, 371, 71)
        self.reqSpecification.setObjectName("reqSpecification")

        if self.work_SQL_inf in [4, 5]:
            self.taxReporting = QPushButton(self.centralwidget)
            self.taxReporting.setGeometry(440, 480, 371, 71)
            self.taxReporting.setObjectName("taxReporting")
            self.taxReporting.setText("Податкова форма")
            self.taxReporting.setStyleSheet(root.find('QPushButton_style/value').text)
            self.taxReportingUI = Ui_Frame(self.user_name)
            self.taxReportingUI.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
            self.taxReporting.clicked.connect(self.taxReportingUI.show)

        if self.work_SQL_inf == 3:
            self.registrButton = QPushButton(self.centralwidget)
            self.registrButton.setGeometry(440, 480, 371, 71)
            self.registrButton.setObjectName("taxReporting")
            self.registrButton.setText("Зареєструвати працівника")
            self.registrButton.setStyleSheet(root.find('QPushButton_style/value').text)
            self.registrWindow = RegistrationWindow(self.password)
            self.registrWindow.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)  # Зроблено вікно завжди зверху
            self.registrButton.clicked.connect(self.registrWindow.show)
        self.work.setText(self.full_work)
        self.name.setText(self.user_name)
        self.jobInstructions.setText("Посадові інструкції")
        self.vacationSchedule.setText("Заява на відпустку")
        self.staffList.setText("Штатний розпис і витяг")
        self.reqSpecification.setText("Отримати характеристику")

        self.jobInstructions.setStyleSheet(root.find('QPushButton_style/value').text)
        self.vacationSchedule.setStyleSheet(root.find('QPushButton_style/value').text)
        self.staffList.setStyleSheet(root.find('QPushButton_styleNOTWORK/value').text)
        self.reqSpecification.setStyleSheet(root.find('QPushButton_styleNOTWORK/value').text)

        self.vacationForm = Ui_Vacation(self.user_name, self.full_work)
        self.vacationForm.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.vacationSchedule.clicked.connect(self.vacationForm.show)

        self.jobInstructions.clicked.connect(lambda: jobInstructions_box(self.work_SQL_inf))
        self.show()

        self.exit.mousePressEvent = self.exit_clicked

    def exit_clicked(self, event):
        self.close()