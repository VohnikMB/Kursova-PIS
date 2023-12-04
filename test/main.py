# main.py
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from login_window import Ui_MainWindow
from profile_window import ProfileWindow
from BLL.Authentication.authentication import check_credentials


class LoginWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.login_function)

    def login_function(self):
        # if check_credentials(self.login_label.text(), self.password_label.text()):

        user_name = self.login_label.text()
        self.profile_window = ProfileWindow("2")
        self.profile_window.show()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    login_window = LoginWindow()
    login_window.show()

    sys.exit(app.exec_())
