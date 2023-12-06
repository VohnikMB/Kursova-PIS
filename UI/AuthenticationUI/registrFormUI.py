from PyQt5.QtWidgets import QMainWindow, QLabel, QWidget, QPushButton
import os
import xml.etree.ElementTree as ET


class RegistrationWindow(QMainWindow):
    def __init__(self):
        super().__init__()
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
        self.show()