from PyQt5.QtWidgets import QMainWindow, QLabel, QWidget, QVBoxLayout, QPushButton, QMessageBox
from PyQt5.QtGui import QPixmap, QFont
from BLL.Authorization.job_instruktion import jobInstructions_box
from PyQt5 import QtCore
from PyQt5 import *
import pdb
import os
import xml.etree.ElementTree as ET

from functools import partial


class ProfileWindow(QMainWindow):
    def __init__(self, user_name, work_SQL_inf):
        super().__init__()
        self.work_SQL_inf = work_SQL_inf
        self.user_name = user_name
        self.init_ui()

    def init_ui(self):
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
        self.jobInstructions.setGeometry(440, 60, 371, 71)
        self.jobInstructions.setObjectName("jobInstructions")

        self.vacationSchedule = QPushButton(self.centralwidget)
        self.vacationSchedule.setGeometry(440, 170, 371, 71)
        self.vacationSchedule.setObjectName("vacationSchedule")
        self.staffList = QPushButton(self.centralwidget)
        self.staffList.setGeometry(440, 280, 371, 71)

        self.staffList.setObjectName("staffList")
        self.reqSpecification = QPushButton(self.centralwidget)
        self.reqSpecification.setGeometry(440, 390, 371, 71)
        self.reqSpecification.setObjectName("reqSpecification")

        self.work.setText(self.work_SQL_inf)
        self.name.setText(self.user_name)
        self.jobInstructions.setText("Посадові інструкції")
        self.vacationSchedule.setText("Графік відпусток")
        self.staffList.setText("Штатний розпис і витяг")
        self.reqSpecification.setText("Отримати характеристику")

        current_directory = os.path.dirname(__file__)
        xml_file_path = os.path.join(current_directory, '..', 'Style', 'styles.xml')
        tree = ET.parse(xml_file_path)
        root = tree.getroot()

        self.jobInstructions.setStyleSheet(root.find('QPushButton_style/value').text)
        self.vacationSchedule.setStyleSheet(root.find('QPushButton_style/value').text)
        self.staffList.setStyleSheet(root.find('QPushButton_style/value').text)
        self.reqSpecification.setStyleSheet(root.find('QPushButton_style/value').text)
        self.jobInstructions.clicked.connect(lambda: jobInstructions_box(self.work_SQL_inf))

        self.show()



