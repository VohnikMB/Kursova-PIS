from PyQt5.QtWidgets import QMessageBox
import os


def jobInstructions_box(work_SQL_inf):
    dialog = QMessageBox()
    try:
        file_content = None
        if work_SQL_inf == "HR_менеджер":
            fileHR_path = os.path.abspath('Data/jobInstructions/jobInstructionsHRM.txt')
            with open(fileHR_path, 'r', encoding='utf-8') as file:
                file_content = file.read()

        elif work_SQL_inf == "Робочий":
            fileEM_path = os.path.abspath('Data/jobInstructions/jobInstructionsEmploy.txt')
            with open(fileEM_path, 'r', encoding='utf-8') as file:
                file_content = file.read()

        elif work_SQL_inf == "HR":
            file_path = os.path.abspath('Data/jobInstructions/jobInstructionsHR.txt')
            with open(file_path, 'r', encoding='utf-8') as file:
                file_content = file.read()

        elif work_SQL_inf == "Головний_бухгалтер":
            file_path = os.path.abspath('Data/jobInstructions/jobInstructionsAccountantM.txt')
            with open(file_path, 'r', encoding='utf-8') as file:
                file_content = file.read()

        elif work_SQL_inf == "Бухгалтер":
            file_path = os.path.abspath('Data/jobInstructions/jobInstructionsAccountant.txt')
            with open(file_path, 'r', encoding='utf-8') as file:
                file_content = file.read()

        elif work_SQL_inf == "Директор":
            file_path = os.path.abspath('Data/jobInstructions/jobInstructionsDirector.txt')
            with open(file_path, 'r', encoding='utf-8') as file:
                file_content = file.read()

        else:
            file_content = "Виникла помилка, зверніться до HR спеціалістів."

        dialog.setText(file_content)
        dialog.setWindowTitle("Посадові інструкції")
        dialog.exec_()

    except Exception as e:
        print(f"Помилка при зчитуванні файлу: {e}")
        import traceback
        traceback.print_exc()
