from PyQt5.QtWidgets import QMainWindow, QLabel

class ProfileWindow(QMainWindow):
    def __init__(self, user_name):
        super().__init__()
        self.user_name = user_name
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Профіль користувача')
        label = QLabel(f"Ласкаво просимо, {self.user_name}!", self)