# main.py
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from UI.AuthenticationUI.authenticationUI import Ui_MainWindow
from UI.AuthenticationUI.profileEmployeeUI import ProfileWindow
from BLL.Authentication.authentication import check_credentials
from BLL.Authorization.profilSQL import get_employee_info as profileSQL


class LoginWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.login_function)

    def login_function(self):
        if check_credentials(self.login_label.text(), self.password_label.text()):

            user_name, work_inf, full_work = profileSQL(self.login_label.text(), self.password_label.text())
            self.profile_window = ProfileWindow(user_name, work_inf, full_work)
            self.profile_window.show()
            self.login_label.clear()
            self.password_label.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    app.exec_()
